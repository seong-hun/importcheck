# 🧪 installcheck

**Check which Python modules your project actually needs – line by line.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🚀 What is this?

`installcheck` is a CLI tool that scans your Python codebase,  
**parses every `import` statement**, and **checks whether those modules are actually available** in your environment.

It helps you:
- Identify **missing dependencies** 🧩
- Clean up **broken or unused imports** 🧹
- Write better **CI/CD checks** 🛠
- Know exactly what you need to `pip install` 📦

---

## 📦 Installation

```bash
pip install installcheck
```

Or for development:

```bash
git clone https://github.com/seong-hun/installcheck.git
cd installcheck
pip install -e .
```

---

## ⚙️  Usage

```bash
installcheck ./your_project              # summary mode
installcheck ./your_project --verbose   # line-by-line failure details
```

---

## 🧪 Example Output

```bash
✅ All Good

✅ All imports succeeded!

❌ Failures Detected (with –verbose)

❌ Import Failures Detected:

src/foo.py:
  [12] from torch.nn import Linear
      → ModuleNotFoundError: No module named 'torch'

  [30] import non_existent_lib
      → ModuleNotFoundError: No module named 'non_existent_lib'

Total failed imports: 2 in 1 files

📦 Missing modules you might need to install:
   pip install torch non_existent_lib
```

---

## ✨ Features

	•	✅ Scans all .py files recursively
	•	✅ Ignores virtualenvs and hidden/system folders
	•	✅ Parses actual import statements via ast
	•	✅ Reports:
	•	Which files fail
	•	Which import lines fail (with --verbose)
	•	Which modules are missing (pip install ...)
	•	✅ Multiprocessing for speed ⚡

---

## 💡 Why?

Because ModuleNotFoundError should never be a surprise in CI.
And because import foo might look innocent… until it silently fails 😅

---

## 👩‍💻 Contributing

Pull requests welcome! Feel free to open issues or suggest improvements.

---

## 📄 License

MIT © 2025 Seong-hun Kim
