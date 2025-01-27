# Keylogger using Python

## Overview
This script implements a simple keylogger using the `pynput` library to capture keyboard events. It listens for key presses and logs them to both the console and a file named `log.txt`.

## Features
- Captures keyboard events in real time.
- Logs each key press to a file (`log.txt`).
- Lightweight and straightforward implementation using Python.

## Functions
### `keyPressed(key)`
- **Description**: Callback function triggered whenever a key is pressed.
- **Behavior**:
  - Logs the key to the console.
  - Appends the key to the `log.txt` file.
  - Attempts to write the character representation of the key. If unsuccessful, an error message is printed to the console.

## Requirements
- Python 3.x
- `pynput` library (`pip install pynput`)

## Usage
1. Ensure Python and the `pynput` library are installed.
2. Save the script to a file, e.g., `keylogger.py`.
3. Run the script using:
   ```bash
   python keylogger.py
