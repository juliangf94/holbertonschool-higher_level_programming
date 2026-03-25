# Python - Server-Side Rendering

This project focuses on **Server-Side Rendering (SSR)** using the **Flask** web framework. Throughout the tasks, I implemented various ways to serve dynamic content by fetching data from different sources such as **JSON** files, **CSV** files, and a **SQLite** database.

## 🚀 Project Overview

The application is a product management system that allows users to view product listings through a web interface. The core feature is the ability to toggle between different data backends using URL query parameters.

### Features
- **Dynamic Routing:** Handled home, about, contact, and product pages.
- **Data Integration:**
  - **JSON:** Parsing and displaying data from `products.json`.
  - **CSV:** Reading and formatting data from `products.csv`.
  - **SQL:** Connecting and querying a `SQLite` database (`products.db`).
- **Jinja2 Templating:** Used blocks, loops, and conditionals to create reusable HTML structures.
- **Error Handling:** Custom messages for "File not found", "Product not found", and "Wrong source".

## 🛠️ Requirements
- Python 3.x
- Flask
- SQLite3

## 📂 Directory Structure
```text
.
├── task_04_db.py           # Main Flask application
├── setup_db.py             # Script to initialize the SQLite database
├── products.json           # Sample JSON data
├── products.csv            # Sample CSV data
├── products.db             # SQLite database file
├── templates/
│   ├── index.html          # Home page
│   ├── about.html          # About page
│   ├── contact.html        # Contact page
│   ├── items.html          # Task 2: Item list demo
│   └── product_display.html # Main product table template
└── README.md
```

## ⚙️ Setup and Installation
1.  Clone the repository:

```Bash
git clone [https://github.com/your_username/holbertonschool-higher_level_programming.git](https://github.com/your_username/holbertonschool-higher_level_programming.git)
cd python-server_side_rendering
```
2.  Initialize the Database:

```Bash
python3 setup_db.py
```
3.  Run the Flask App:

```Bash
python3 task_04_db.py
```
4.  Access the application:
Open your browser and navigate to `http://127.0.0.1:5000/products?source=json`

## 🔗 Usage Examples
You can filter products by source or by specific ID:

-   JSON Source: /products?source=json
-   CSV Source: /products?source=csv
-   SQL Source: /products?source=sql
-   Filtered by ID: /products?source=sql&id=1

##  👨‍💻 Author
-   Julian Gonzalez - [juliangf94](https://github.com/juliangf94)
