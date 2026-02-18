# Holberton School - RESTful API Project

## Description
This project focuses on the development and security of RESTful APIs using Python. It covers everything from consuming external data via the `requests` library to building custom backends using both the low-level `http.server` module and the **Flask** framework. The final stages implement industry-standard security measures, including **Password Hashing**, **HTTP Basic Authentication**, and **JSON Web Tokens (JWT)** for Role-Based Access Control (RBAC).

## Learning Objectives
* Understand the structure and lifecycle of HTTP requests and responses.
* Consume and process external API data using the `requests` library.
* Build a basic web server from scratch without external frameworks.
* Develop a robust API using **Flask**.
* Implement API security, authentication, and authorization mechanisms.
* Differentiate between Authentication (Who are you?) and Authorization (What can you do?).
* Handle in-memory data persistence using Python dictionaries.

## Technologies & Libraries
* **Python 3.10+**
* **Flask**: Web framework for the API development.
* **Flask-HTTPAuth**: Extension for HTTP Basic Authentication.
* **Flask-JWT-Extended**: Extension for JWT management and security.
* **Requests**: Library for consuming external APIs.
* **Werkzeug**: Utilities for secure password hashing and verification.

---

## Tasks Overview

### Task 0: Console Application
A Python script that fetches and displays data from the JSONPlaceholder API to understand basic API consumption.

### Task 2: Consuming and Processing Data
A script that fetches posts from an external API, processes the information, and exports the data into a structured CSV file.

### Task 3: Simple HTTP Server
A low-level implementation of a web server using Python's built-in `http.server` module to handle GET requests and return JSON responses manually.

### Task 4: Flask API Development
Development of a Flask-based API featuring:
* CRUD operations managed through a user dictionary.
* Dynamic routing (`/users/<username>`).
* Implementation of proper HTTP status codes (200, 201, 400, 404, 409).

### Task 5: API Security and Authentication
The final stage of the project, focusing on advanced security:
* **Password Hashing**: Secure storage using `generate_password_hash`.
* **Basic Auth**: Protected routes requiring valid credentials in the header.
* **JWT Authentication**: Token-based login system for session management.
* **RBAC (Role-Based Access Control)**: Admin-only routes using JWT claims.
* **Custom Error Handlers**: Implementation of consistent 401 Unauthorized responses for all authentication failures (expired, invalid, or missing tokens).

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your_username/holbertonschool-higher_level_programming.git](https://github.com/your_username/holbertonschool-higher_level_programming.git)
cd restful-api
``` 
2.  **Install the required dependencies**:
```bash
pip install Flask Flask-HTTPAuth Flask-JWT-Extended requests
```
---
### How to Run the Servers
**Run Task 4 (Flask API)**:
```Bash
python3 -m flask --app task_04_flask.py run
```
**Run Task 5 (Secure API)**:
```Bash
python3 task_05_basic_security.py
Testing the Secure API (Task 5)
```
---
##  Testing the Secure API (Task 5)
1. **Basic Authentication**
Test the basic auth route using curl:

```Bash
curl -u user1:password [http://127.0.0.1:5000/basic-protected](http://127.0.0.1:5000/basic-protected)
```
2. **JWT Login (Obtain Token)**
Send a POST request with credentials to receive your access token:

```Bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"admin1", "password":"password"}' \
     [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
```

3. **Accessing JWT Protected Routes**
Use the token received in the previous step to access protected areas:
```Bash
curl -H "Authorization: Bearer <YOUR_JWT_TOKEN>" [http://127.0.0.1:5000/jwt-protected](http://127.0.0.1:5000/jwt-protected)
```

4. **Role-Based Access (Admin Only)**
Verify that only users with the "admin" role can access the restricted endpoint:
```Bash
curl -H "Authorization: Bearer <YOUR_ADMIN_TOKEN>" [http://127.0.0.1:5000/admin-only](http://127.0.0.1:5000/admin-only)
```
---
##  Author
-   Julian GONZALEZ - [GitHub Profile](https://github.com/juliangf94)
