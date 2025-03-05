# Python Classes - Object-Oriented Programming (OOP)

This directory contains Python exercises focused on understanding Object-Oriented Programming (OOP) concepts, specifically related to creating and manipulating classes, objects, and attributes.

## Project Overview

The goal of this project is to familiarize yourself with the basic principles of OOP, such as classes, instances, attributes, and methods. You'll build classes and implement specific functionality as described in the tasks below.

### Learning Objectives

- Understand the concept of OOP.
- Define classes and create objects (instances).
- Work with attributes (public, protected, private) and validate them.
- Use the special `__init__` method for class initialization.
- Implement methods and properties within classes.
- Control access to class attributes using getters and setters.
- Create methods to interact with object data.

## Tasks

### Task 0: My First Square

- **Objective**: Create an empty class `Square` that defines a square.
- **Details**: The class should not have any attributes or methods yet.

### Task 1: Square with Size

- **Objective**: Define a `Square` class with a private attribute `size` to represent the size of the square.
- **Details**: The class should be instantiated with a `size` argument.

### Task 2: Size Validation

- **Objective**: Ensure that the `size` attribute is an integer and greater than or equal to 0.
- **Details**: Raise `TypeError` if the `size` is not an integer and `ValueError` if it is less than 0.

### Task 3: Area of a Square

- **Objective**: Implement a method `area` to return the area of the square.
- **Details**: The method should compute and return the square's area.

### Task 4: Access and Update Private Attribute

- **Objective**: Use properties to access and set the value of `size` safely.
- **Details**: Implement getter and setter methods for the `size` attribute and validate its value.

### Task 5: Printing a Square

- **Objective**: Implement a `my_print` method to print a square using the `#` character.
- **Details**: The `size` of the square will determine how many rows and columns of `#` are printed.

### Task 6: Coordinates of a Square

- **Objective**: Implement a `position` attribute that defines the coordinates where the square will be printed.
- **Details**: The `position` attribute should be a tuple of two positive integers, representing the (x, y) coordinates.

## Requirements

- Python 3.8.5
- All scripts should be executed on Ubuntu 20.04 LTS using Python 3.
- All Python files must end with a new line.
- All scripts must follow `pycodestyle` guidelines.
- Documentation is mandatory for all modules, classes, and methods.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/alu-higher_level_programming.git
   ```

