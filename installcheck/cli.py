import argparse

from installcheck.checker import run_line_level_import_checks
from installcheck.reporter import print_summary_report, print_verbose_report


def main():
    parser = argparse.ArgumentParser(
        description="🧪 Import Checker with Line-level Verbose Option"
    )
    parser.add_argument("base_path", help="Path to your codebase")
    parser.add_argument(
        "--verbose", action="store_true", help="Show each failed import line"
    )
    parser.add_argument(
        "--max-workers", type=int, default=None, help="Number of parallel workers"
    )
    args = parser.parse_args()

    results = run_line_level_import_checks(args.base_path, args.max_workers)

    if args.verbose:
        print_verbose_report(results)
    else:
        print_summary_report(results)

    has_failures = any(r["status"] == "fail" for r in results)
    if has_failures:
        exit(1)
