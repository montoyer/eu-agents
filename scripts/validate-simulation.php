<?php
declare(strict_types=1);

/**
 * CLI validator for a produced simulation. Gates publish: a simulation that does
 * not pass here will not render a usable page.
 *
 *   php scripts/validate-simulation.php <slug>
 *   php scripts/validate-simulation.php --all
 *
 * Reuses load_simulation() so the validator and the renderer share one definition
 * of "valid" — they can never drift apart.
 */

require __DIR__ . '/../lib/simulations.php';

const ALLOWED_COLORS = ['blue', 'red', 'green', 'yellow', 'default'];

/** @return string[] list of problems; empty array means the slug is publishable. */
function validate_slug(string $slug): array
{
    $errors = [];

    if (!is_valid_slug($slug)) {
        return ["slug '$slug' is malformed (must match ^[a-z0-9][a-z0-9-]{0,99}$)"];
    }

    $dir = SIMULATIONS_DIR . '/' . $slug;
    $jsonPath = $dir . '/simulation.json';

    if (!is_file($jsonPath)) {
        return ["missing $jsonPath"];
    }

    $raw = (string) file_get_contents($jsonPath);
    try {
        $data = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        return ['simulation.json is not valid JSON: ' . $e->getMessage()];
    }
    if (!is_array($data)) {
        return ['simulation.json did not decode to an object'];
    }

    // Core structural gate — identical to the renderer's.
    if (!is_simulation_valid($data)) {
        $errors[] = 'fails core contract (needs title, summary, source_tweet.text, non-empty messages)';
    }

    // source_tweet completeness — text is the only hard requirement, but warn on
    // the fields the page displays so previews are not blank.
    foreach (['url', 'author', 'author_name', 'text'] as $key) {
        if (empty($data['source_tweet'][$key] ?? null)) {
            $errors[] = "source_tweet.$key is empty (renders blank on the page)";
        }
    }

    // Build the agent id set so messages can be checked against it.
    $agentIds = [];
    foreach (($data['agents'] ?? []) as $i => $agent) {
        if (!is_array($agent) || empty($agent['id'])) {
            $errors[] = "agents[$i] has no id";
            continue;
        }
        $agentIds[(string) $agent['id']] = true;
        $color = (string) ($agent['color'] ?? 'default');
        if (!in_array($color, ALLOWED_COLORS, true)) {
            $errors[] = "agents[$i].color '$color' is not whitelisted (will render grey)";
        }
    }

    // Messages must reference known agents and carry text.
    foreach (($data['messages'] ?? []) as $i => $msg) {
        if (!is_array($msg) || !isset($msg['text']) || trim((string) $msg['text']) === '') {
            $errors[] = "messages[$i] has empty text";
        }
        $agent = (string) ($msg['agent'] ?? '');
        if ($agent !== '' && $agentIds !== [] && !isset($agentIds[$agent])) {
            $errors[] = "messages[$i].agent '$agent' is not declared in agents[] (renders grey, raw id)";
        }
    }

    // Disclaimer must be present and non-empty.
    if (trim((string) ($data['disclaimer'] ?? '')) === '') {
        $errors[] = 'disclaimer is empty (a disclaimer is mandatory on every page)';
    }

    // published should be a parseable date for correct archive ordering.
    $published = (string) ($data['published'] ?? '');
    if ($published === '' || strtotime($published) === false) {
        $errors[] = "published '$published' is missing or unparseable (archive will sort it last)";
    }

    return $errors;
}

// ── CLI entry ────────────────────────────────────────────────────────────────
$arg = $argv[1] ?? '';

if ($arg === '' || $arg === '-h' || $arg === '--help') {
    fwrite(STDERR, "usage: php scripts/validate-simulation.php <slug>\n");
    fwrite(STDERR, "       php scripts/validate-simulation.php --all\n");
    exit(2);
}

$slugs = [];
if ($arg === '--all') {
    foreach (scandir(SIMULATIONS_DIR) ?: [] as $entry) {
        if ($entry === '.' || $entry === '..') {
            continue;
        }
        if (is_dir(SIMULATIONS_DIR . '/' . $entry)) {
            $slugs[] = $entry;
        }
    }
    if ($slugs === []) {
        fwrite(STDOUT, "no simulations found in simulations/\n");
        exit(0);
    }
} else {
    $slugs = [$arg];
}

$failed = 0;
foreach ($slugs as $slug) {
    $errors = validate_slug($slug);
    if ($errors === []) {
        fwrite(STDOUT, "OK   $slug — renders at simulation.php?slug=$slug\n");
    } else {
        $failed++;
        fwrite(STDOUT, "FAIL $slug\n");
        foreach ($errors as $e) {
            fwrite(STDOUT, "       - $e\n");
        }
    }
}

exit($failed > 0 ? 1 : 0);
