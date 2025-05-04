# Keylogger Cross-Platform

Background launchable keylogger that saves all keystrokes to "keyloggeroutput.txt".

starting this keylogger is easy on any OS:
- **Windows**, just change the file extension to `.pyw`, so clicking on it, the program will start in the background. To stop the execution, just open the task manager and kill all the "python" processes.
- **MacOS/Linux**, just launch a simple command from the terminal to start the process in the background and persist even after logging out:
```bash
nohup python3 keylogger.py > /dev/null 2>&1 &
```

to stop the process:
```bash
pkill -f "python3 keylogger.py"
```

---

## Requirements

- Python 3.x
- pynput library

---

## Installation

1. Clone the repository or download the Python file
2. Install the dependencies:
```bash
pip install pynput