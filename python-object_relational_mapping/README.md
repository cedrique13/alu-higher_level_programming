```markdown
# Python and MySQL ORM Project

## Background Context

In this project, I have combined two powerful worlds: **Databases** and **Python**. You will explore two approaches for interacting with MySQL databases:

1. **Using MySQLdb**: This approach involves writing raw SQL queries to interact with the database.
2. **Using SQLAlchemy ORM**: SQLAlchemy abstracts the database interactions and allows you to work with Python objects instead of writing SQL queries.

### Without ORM (Using MySQLdb):

In this approach, you must write SQL queries to interact with the database.

```python
import MySQLdb

# Connect to MySQL database
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()

# Execute SQL query
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch results
query_rows = cur.fetchall()

# Print results
for row in query_rows:
    print(row)

cur.close()
conn.close()
```

### With ORM (Using SQLAlchemy):

With SQLAlchemy, you no longer write SQL queries; you simply interact with Python objects.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Base, State  # Assuming State class is defined in model.py

# Create engine and session
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)

# Query the database without SQL, only using Python objects
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

session.close()
```

---

## Learning Objectives

By the end of this project, you should be able to:

- Understand why Python programming is awesome.
- Connect to a MySQL database from a Python script.
- Use Python to **SELECT** rows from a MySQL table.
- Use Python to **INSERT** rows into a MySQL table.
- Understand what **ORM** (Object Relational Mapping) means.
- Map a Python class to a MySQL table.

---

## Requirements

### General

- Allowed editors: **vi**, **vim**, **emacs**
- Files will be executed on **Ubuntu 20.04 LTS** using **python3** (version 3.8.5).
- The files should be executed with:
  - **MySQLdb** version 2.0.x
  - **SQLAlchemy** version 1.4.x
- Ensure all your files end with a new line.
- The first line of all files should be:  
  `#!/usr/bin/python3`
- Follow **pycodestyle** (version 2.7.*) for code style.
- All files must be executable.
- Documentation for modules, classes, and functions is required using docstrings.
- All your test files should be Python files (.py).

---

## Setup Instructions

Before you begin, ensure your MySQL server is running **version 8.0**. You can follow the instructions here to install MySQL 8.0 on Ubuntu 20.04.

### Installing MySQLdb Module (version 2.0.x)

To use **MySQLdb**, ensure you have MySQL installed and then follow these steps:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

You can verify the installation by running:

```python
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### Installing SQLAlchemy (version 1.4.x)

To install **SQLAlchemy**, use:

```bash
$ sudo pip3 install SQLAlchemy
```

Verify the installation by running:

```python
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

---

## Documentation

Ensure that all your modules, classes, and functions are documented using docstrings. You can check the documentation using the following commands:

```bash
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

---

## Resources

- [Object-relational mappers](https://realpython.com/python-sqlalchemy-orm/)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

---

## Conclusion

This project will give you a solid understanding of how to interact with a MySQL database both with traditional SQL and using an Object-Relational Mapper (ORM). It’s a great introduction to working with databases in Python and helps you understand the power and flexibility of SQLAlchemy.

---