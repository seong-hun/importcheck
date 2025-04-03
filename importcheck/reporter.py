GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def group_failures(results):
    failures = [r for r in results if r["status"] == "fail"]
    grouped = {}
    for fail in failures:
        grouped.setdefault(fail["file"], []).append(fail)
    return grouped


def print_missing_modules_hint(results):
    missing = sorted(
        set(r["module"] for r in results if r["status"] == "fail" and r.get("module"))
    )
    if missing:
        print(
            f"\n📦 Missing modules you might need to install:\n   pip install {' '.join(missing)}"
        )


def print_verbose_report(results):
    grouped = group_failures(results)
    if not grouped:
        print(f"\n{GREEN}✅ All imports succeeded!{RESET}\n")
        return

    print(f"\n{RED}❌ Import Failures Detected:{RESET}\n")
    for file, failures in grouped.items():
        print(f"{YELLOW}{file}:{RESET}")
        for f in failures:
            print(
                f"  [{f['line']}] {f['import_code']}\n      → {RED}{f['error']}{RESET}"
            )
        print()

    print(
        f"{RED}Total failed imports: {sum(len(f) for f in grouped.values())} in {len(grouped)} files{RESET}\n"
    )
    print_missing_modules_hint(results)


def print_summary_report(results):
    files = sorted(set(r["file"] for r in results if r["status"] == "fail"))
    if files:
        print(f"\n{RED}❌ Failed imports in the following files:{RESET}")
        for f in files:
            print(f"  - {YELLOW}{f}{RESET}")
        print(f"\n{RED}Total: {len(files)} files{RESET}\n")
    else:
        print(f"\n{GREEN}✅ All imports succeeded!{RESET}\n")

    print_missing_modules_hint(results)
