# VITyarthi-Project
# Console Task Manager

A minimal, lightning-fast terminal-based utility developed in Python to track, manage, and log daily activities directly within a command-line interface.

## Overview of the Project
This software application provides a zero-dependency, local-first environment for tracking items without the overhead of heavy graphical user interfaces. It uses a clean, modular structure that separates user interaction loops, task state logic, raw data validation, and text-based file persistence layers.

## Features
* **Interactive Command Menu:** Rapid option selection via key numeric selections.
* **Input Validation Shield:** Rejects blank lines to prevent system database fragmentation.
* **Inline Status Tracking:** Renders pending tasks as `[ ]` and completed tasks as `[X]`.
* **Data Persistence Engine:** Automatically syncs running operations with local file storage.
* **Indexed Modifiers:** Selects, completes, or purges records using unique line identifiers.

## Technologies/Tools Used
* **Programming Language:** Python 3.x
* **Core APIs:** Native Python standard file input/output modules.
* **Testing Library:** Pytest automated assertion testing suite.

## Steps to Install & Run the Project
1. Clone or copy the project files to a single local workspace folder.
2. Open a standard terminal window inside that folder path.
3. Start the application loop execution by running the following command:
   ```bash
   python main.py
   ```

## Instructions for Testing
To execute the suite of unit tests and verify module functionality across input boundaries, type the following command in the terminal prompt:
```bash
pytest test_project.py
```
*(If pytest is missing globally on your computer, execute using `python test_project.py` instead.)*

## Screenshots
* **Main Working Flow Screen:** Displays choice routes available to the operator.
* **Input Gate Error Capture:** Displays the validation exception engine intercepting empty text inputs.
