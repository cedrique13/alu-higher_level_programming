
n - Network #1

## Description
This project introduces concepts of network programming in Python, focusing on fetching internet resources, making HTTP requests, and handling JSON data using `urllib` and `requests`.

## Learning Objectives
By the end of this project, you should be able to explain:
- How to fetch internet resources using `urllib`.
- How to decode `urllib` response bodies.
- How to use the `requests` package to perform HTTP requests.
- How to handle GET, POST, and other HTTP methods.
- How to retrieve and process JSON data from APIs.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`.
- All scripts will be tested on Ubuntu 14.04 LTS using Python 3.4.3.
- All scripts should end with a new line.
- The first line of all scripts should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project directory is mandatory.
- Code should follow PEP 8 style (version 1.7).
- All scripts must be executable.
- The length of scripts will be tested using `wc`.
- All modules should have proper documentation.
- Use `if __name__ == "__main__":` to prevent scripts from running when imported.

## Project Tasks

### 0. What's my status? #0
**File:** `0-hbtn_status.py`
- Fetches `https://alu-intranet.hbtn.io/status` using `urllib`.
- Displays response information with proper formatting.

### 1. Response header value #0
**File:** `1-hbtn_header.py`
- Takes a URL as input and retrieves the `X-Request-Id` header value using `urllib`.

### 2. POST an email #0
**File:** `2-post_email.py`
- Sends a POST request to a URL with an email parameter.
- Uses `urllib` to handle requests.

### 3. Error code #0
**File:** `3-error_code.py`
- Handles HTTP error responses and prints the appropriate status code.

### 4. What's my status? #1
**File:** `4-hbtn_status.py`
- Fetches `https://alu-intranet.hbtn.io/status` using `requests`.

### 5. Response header value #1
**File:** `5-hbtn_header.py`
- Retrieves the `X-Request-Id` header using `requests`.

### 6. POST an email #1
**File:** `6-post_email.py`
- Sends a POST request with an email parameter using `requests`.

### 7. Error code #1
**File:** `7-error_code.py`
- Handles HTTP error responses using `requests`.

### 8. Search API
**File:** `8-json_api.py`
- Sends a POST request with a letter parameter.
- Parses JSON response to display user information.

### 9. My GitHub!
**File:** `10-my_github.py`
- Uses the GitHub API to fetch user ID based on credentials.
- Implements authentication with a personal access token.

## Repository Structure
```
alu-higher_level_programming/
│── python-network_1/
│   ├── 0-hbtn_status.py
│   ├── 1-hbtn_header.py
│   ├── 2-post_email.py
│   ├── 3-error_code.py
│   ├── 4-hbtn_status.py
│   ├── 5-hbtn_header.py
│   ├── 6-post_email.py
│   ├── 7-error_code.py
│   ├── 8-json_api.py
│   ├── 10-my_github.py
│   ├── README.md
```

## Author
- **Cedrick Bienvenue**


