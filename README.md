# Getting Started with the NIST Statistical Test Suite

This guide walks you through the process of installing and using the NIST Statistical Test Suite for evaluating random and pseudorandom number generators for cryptographic applications.

I am using Visual Studio Code with Windows

## Prerequisites:

- Windows Subsystem for Linux (WSL): Ensure you have WSL set up on your Windows machine. Follow the official tutorial for installation: https://code.visualstudio.com/docs/remote/wsl-tutorial

- Visual Studio Code: Install Visual Studio Code, a versatile code editor with WSL integration. Download it here: https://code.visualstudio.com/

- VS Code WSL Extension: Install the "Remote - WSL" extension within VS Code to enable working with WSL environments directly within VS Code.

## Installation Steps:

1. **Open WSL Terminal in VS Code:**

    - Launch VS Code.
Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the Command Palette.
Type "Remote-WSL: New WSL Window" and select the command.
Choose your preferred Linux distribution when prompted.

2. **Install Required Packages:**

    - Update package lists: sudo apt-get update
```console
Install make: sudo apt install make
Install gcc: sudo apt install gcc
```

3. **Build the Test Suite:**

    - Navigate to the directory containing the NIST Statistical Test Suite source code using the WSL terminal.
Run make to build the test suite.

- **Running the Test Suite:**

    - Execute the assess Program:
Once the build is complete, you'll find an executable named assess in the directory.
Run it with a specified sequence length: ``` ./assess <sequence_length> ``` with the actual length of the random or pseudorandom sequence you want to evaluate.

**Example:**

To test a sequence of 1000000 bits, run:

Bash
```./assess 1000000```
Use code with caution. Learn more
The test suite will execute a battery of statistical tests and generate a report with the results, indicating the randomness quality of the tested sequence.