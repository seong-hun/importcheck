import importlib
from multiprocessing import Pool, cpu_count

from installcheck.utils import extract_import_statements, find_py_files


def test_single_import(item):
    try:
        importlib.import_module(item["module"])
        return {**item, "status": "success", "error": None}
    except Exception as e:
        return {
            **item,
            "status": "fail",
            "error": f"{type(e).__name__}: {str(e).splitlines()[0]}",
        }


def run_line_level_import_checks(base_path, max_workers=None):
    py_files = find_py_files(base_path)
    all_imports = []
    for file in py_files:
        all_imports.extend(extract_import_statements(file))

    max_workers = max_workers or cpu_count()
    with Pool(processes=max_workers) as pool:
        results = pool.map(test_single_import, all_imports)

    return results
