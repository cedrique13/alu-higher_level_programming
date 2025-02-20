# Python - Import & Modules

## Description

This project focuses on learning how to import functions, use modules, and handle command-line arguments in Python. By the end of the project, you should be able to effectively use and create Python modules, work with built-in functions like `dir()`, and ensure that scripts are not executed when imported.

## Learning Objectives

By completing this project, you will:

- Understand why Python programming is awesome.
- Learn how to import functions from another file.
- Know how to use imported functions.
- Learn how to create a module.
- Understand how to use the built-in function `dir()`.
- Learn how to prevent code in your script from being executed when imported.
- Understand how to use command-line arguments with Python programs.

## Requirements

- All files must be written in Python 3.8.5 and executed on Ubuntu 20.04 LTS.
- Your Python scripts should begin with `#!/usr/bin/python3`.
- Your code must follow `pycodestyle` (version 2.7.\*).
- All files must be executable.
- The length of your files will be tested using `wc`.

## Project Structure

```
├── 0-add.py              # Imports function from add_0.py and prints addition result
├── 1-calculation.py      # Imports functions from calculator_1.py and performs operations
├── 2-args.py            # Prints number of arguments and their values
├── 3-infinite_add.py    # Adds all arguments and prints the result
├── 4-hidden_discovery.py # Prints names from hidden_4.pyc (excluding those starting with __)
├── 5-variable_load.py   # Imports variable from variable_load_5.py and prints it
├── add_0.py             # Contains the add(a, b) function
├── calculator_1.py      # Contains basic mathematical functions
├── variable_load_5.py   # Contains a simple variable a = 98
└── README.md            # Project documentation
```

## Usage

To run any script, use:

```sh
./script_name.py
```

Ensure that the necessary files are in the same directory.

## Example Commands

```sh
$ ./0-add.py
1 + 2 = 3

$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

$ ./2-args.py Hello World
2 arguments:
1: Hello
2: World

$ ./3-infinite_add.py 10 20 30
60

$ ./4-hidden_discovery.py
my_secret_santa
print_hidden
print_school

$ ./5-variable_load.py
98
```

## Author

Cedrick Bienvenue


