
# 🐍 Cornsnake1 Python REPL


Cornsnake1 is a **custom interactive Python REPL** (Read-Eval-Print-Loop) built with
[`prompt_toolkit`](https://python-prompt-toolkit.readthedocs.io/) and [`pygments`](https://pygments.org/)
to provide syntax highlighting, command history, and advanced features.

⚡ Designed as an **experimental transpiling REPL** with optional safety and raw-terminal modes.

---

## ✨ Features

* 🖥️ **Custom REPL Shell** with syntax highlighting (thanks to `prompt_toolkit` + `pygments`).
* 🧠 **Code History Tracking** (`:code_history` shows all stored code).
* 🗑️ **Clear Code / Screen Commands** (`:clear_code`, `:clear_screen`).
* 🚀 **Transpiling Mode**: Save all accumulated code to `transpiled.py` automatically with `--active_transpiling`.
* 🛡️ **Safety Mode**: Prevents execution of dangerous commands like `sudo` (default ON). Override with `--unsafe`.
* 🎨 **Raw Terminal Mode**: Skip fancy UI banners and clear-screen resets with `--raw_terminal`.
* ⏳ **Automatic Reset**: Clears screen after 20 prompts to keep it fresh.
* 📄 **IR Serialization**: Execution history + metadata stored in `irserial.json`.
* 🐧 **Cross-platform Support**: Works on Linux, macOS, and Windows.

---

## 🔧 Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/MOHAPY24/Cornsnake.git
cd Cornsnake
pip install prompt_toolkit pygments colorama
```

---

## 🚀 Usage

Run the REPL:

```bash
python3 cornsnake.py [flags]
```

Optional flags:

* `--unsafe` → disables safety checks (⚠️ dangerous!)
* `--raw_terminal` → disables banners & fancy resets
* `--active_transpiling` → live-transpiles input into `transpiled.py`

---

## 💻 Commands inside REPL

| Command         | Action                                                       |
| --------------- | ------------------------------------------------------------ |
| `:quit`         | Exit the REPL                                                |
| `:clear_code`   | Clears all accumulated code                                  |
| `:transpile`    | Saves accumulated code to `transpiled.py`                    |
| `:code_history` | Prints all accumulated code                                  |
| `:clear_screen` | Clears the terminal (OS-specific) and reprints the banner    |
| `:run_code`     | Runs the accumulated code and logs results into IR structure |

---

## 🧾 Metadata Example (irserial.json)

```json
{
  "IR": {
    "code_ran": "print('hello')",
    "total_chars_code": 18,
    "last_command": "print('hello')",
    "output": "hello\n"
  },
  "metadata": {
    "repl_name": "Cornsnake1",
    "repl_version": "1.0.0",
    "python_version": "3.12.2",
    "safety": true,
    "raw_terminal": false,
    "os_name": "posix",
    "active_transpiling": false,
    "current_time": 1756440000.123456
  }
}
```

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to use, modify, and distribute this software under the terms of the GPL-3.0 license.
See the full license text in the [LICENSE](LICENSE) file.

© 2025 Mohammed Abdelaal
