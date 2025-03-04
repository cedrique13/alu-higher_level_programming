# Python - Exceptions

## Description

This directory contains solutions to tasks related to **Python Exceptions**. The objective of this project is to understand and practice how to handle errors and exceptions in Python using `try`, `except`, and `finally` blocks. Each task is aimed at building a deeper understanding of exception handling while writing clean and robust Python code.

## Learning Objectives

- Understand the difference between errors and exceptions.
- Use `try` and `except` blocks to handle exceptions.
- Raise built-in exceptions.
- Implement clean-up actions with the `finally` block.
- Handle multiple exceptions gracefully.

## Technologies

- Language: Python 3.8.5
- OS: Ubuntu 20.04 LTS
- Style Guide: PEP 8 (pycodestyle 2.7.\*)
- All files are executable and end with a new line.

## Files

| Filename                        | Description                                                                                                |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `0-safe_print_list.py`          | Function that prints `x` elements from a list with exception handling.                                     |
| `1-safe_print_integer.py`       | Function that prints an integer using `{:d}.format()` with exception handling.                             |
| `2-safe_print_list_integers.py` | Function that prints the first `x` elements of a list, only integers, and skips other data types silently. |
| `3-safe_print_division.py`      | Function that divides two integers and prints the result in the `finally` block.                           |
| `4-list_division.py`            | Function that divides element by element two lists, handles exceptions, and returns a new list.            |
| `5-raise_exception.py`          | Function that raises a `TypeError` exception.                                                              |
| `6-raise_exception_msg.py`      | Function that raises a `NameError` exception with a custom message.                                        |

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your_username/alu-higher_level_programming.git
```

2. Navigate to the project directory:

```bash
cd alu-higher_level_programming/python-exceptions
```

3. Make the files executable:

```bash
chmod +x *.py
```

4. Run the test scripts:

```bash
./0-main.py
./1-main.py
```

