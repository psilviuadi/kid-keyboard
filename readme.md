# Kid Keyboard

A small, focused utility that captures all keyboard and mouse input so a child can safely press keys and click the mouse without affecting your running apps. The program runs locally and will exit when the preset key combination `Alt+F4` is pressed.

**Purpose**: Let a kid explore the keyboard and mouse while preventing unintended actions in your main session. Useful for supervised play, demos, or teaching basic input.

**Features**
- Captures keyboard input (all keys).
- Captures mouse clicks.
- Graceful exit via a preset key combo: `Alt+F4`.

**Requirements**
- Python 3.8+.
- Dependencies listed in `requirements.txt`.

Install dependencies:

```powershell
pip install -r requirements.txt
```

**Usage**

Run the program from the repository root:

```powershell
python run.py
```

While running, the program will capture keys and clicks. To stop and exit, press the preset key combination: `Alt+F4`.

**Safety & Privacy**
- This application captures input events. Do not run it on systems where sensitive information may be typed or entered (passwords, personal data).
- Review the source code before running to ensure it meets your privacy and security requirements.

**Notes**
- The exit shortcut is configurable in the code; `Alt+F4` is the current preset.
- If you want the program to run in a different mode (background, minimized, or with persistent logs), modify `run.py` accordingly.

If you'd like, I can add an examples section, screenshot, or an installer for Windows. Tell me which you'd prefer next.
