# Python - Test-driven Development

## Description
This directory contains Python projects focused on **Test-driven Development (TDD)**. The goal is to write tests before implementing functions to ensure correctness, handle edge cases, and improve code reliability.

## Learning Objectives
By completing these projects, I aim to:
- Understand the importance of writing tests in Python.
- Use **doctest** and **unittest** for testing.
- Write proper documentation for modules and functions.
- Identify and handle edge cases in Python programs.

## Project Requirements
- Code is written in **Python 3.8.5**.
- Follow **pycodestyle (2.7.*** for code formatting.
- Test files are stored in the `tests/` directory.
- Use `doctest` and `unittest` for verifying functionality.
- No external libraries are used.

## Files Overview
- `0-add_integer.py`: Function to add two integers.
- `2-matrix_divided.py`: Function to divide all elements in a matrix.
- `3-say_my_name.py`: Function that prints a formatted name.
- `4-print_square.py`: Function to print a square using `#`.
- `5-text_indentation.py`: Function to format text with specific rules.
- `6-max_integer.py`: Function to find the maximum integer in a list.
- `tests/`: Contains test cases for all implemented functions.

## Running Tests
To execute **doctests**, run:
```sh
python3 -m doctest -v tests/*.txt
```
To execute **unittests**, run:
```sh
python3 -m unittest discover tests/
```

## Author
Cedrick Bienvenue


