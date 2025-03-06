# Python - Inheritance

This project is part of the ALU Higher Level Programming curriculum, focused on understanding inheritance in Python.

## Learning Objectives

- What is inheritance and why it is important.
- Difference between superclass (parent class) and subclass (child class).
- How to inherit attributes and methods from one class to another.
- How to override methods.
- How to use multiple inheritance.
- How to use built-in functions like `isinstance()`, `issubclass()`, `type()`, and `super()`.

## Requirements

- All scripts are written in Python 3.8.5.
- Code adheres to the PEP 8 style guide using `pycodestyle` (version 2.7.\*).
- All files are executable and end with a new line.
- Each module, class, and method contains documentation.
- Test cases are stored in the `tests` directory.

## Project Structure

```
python-inheritance/
│
├── 0-lookup.py            # Function to list available attributes and methods of an object
├── 1-my_list.py          # Class that inherits from list with print_sorted method
├── 2-is_same_class.py     # Function to check if object is an exact instance of a class
├── 3-is_kind_of_class.py  # Function to check if object is instance of or inherited from a class
├── 4-inherits_from.py     # Function to check if object is subclass of a class
├── 5-base_geometry.py     # Empty class BaseGeometry
├── 6-base_geometry.py     # BaseGeometry with area method raising Exception
├── 7-base_geometry.py     # BaseGeometry with integer_validator method
├── 8-rectangle.py        # Class Rectangle inheriting from BaseGeometry
└── tests/                # Test files for each task
```

## Usage

To run the test cases, use the following command:

```bash
python3 -m doctest ./tests/*
```

## Author

Cedrick Bienvenue

## License

This project is part of ALU's curriculum and is intended for educational purposes only.


