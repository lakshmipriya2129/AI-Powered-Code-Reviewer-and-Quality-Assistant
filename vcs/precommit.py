import sys

from parser.analyzer import analyze_file
from metrics.metrics_engine import MetricsEngine
from vcs.git_utils import get_staged_files
from vcs.quality_gate import evaluate_quality


def run_precommit():

    staged_files = get_staged_files()

    if not staged_files:
        print(" No Python files staged")
        return 0

    engine = MetricsEngine()

    failed = False

    for file in staged_files:

        print(f"\n Reviewing {file}")

        analysis = analyze_file(file)

        metrics = engine.analyze_file(
            file,
            analysis
        )

        failures = evaluate_quality(metrics)

        if failures:
            failed = True

            print(" Quality Gate Failed:")
            for f in failures:
                print(" -", f)

    if failed:
        print("\n Commit blocked ❌")
        return 1

    print("\n Quality Gate Passed ✅")
    return 0


if __name__ == "__main__":
    sys.exit(run_precommit())