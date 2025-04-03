import ast
import os

EXCLUDED_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    ".idea",
    ".pytest_cache",
    ".mypy_cache",
    ".eggs",
    "build",
    "dist",
}


def find_py_files(base_path):
    py_files = []
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in EXCLUDED_DIRS]
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def extract_import_statements(filepath):
    imports = []
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
        tree = ast.parse(source, filename=filepath)
        lines = source.splitlines()

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            lineno = getattr(node, "lineno", -1)
            line = lines[lineno - 1] if 0 < lineno <= len(lines) else ""
            module = get_module_name(node)
            if module:
                imports.append(
                    {
                        "file": filepath,
                        "line": lineno,
                        "import_code": line.strip(),
                        "module": module,
                    }
                )
    return imports


def get_module_name(node):
    if isinstance(node, ast.Import):
        return node.names[0].name
    elif isinstance(node, ast.ImportFrom):
        return node.module
    return None
