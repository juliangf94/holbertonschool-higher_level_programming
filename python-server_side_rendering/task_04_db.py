import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Reading functions ---
def read_json(filename):
    """ Read and returns data from JSON file """
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv(filename):
    """ Read and returns data from CSV file as a dict"""
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Transform ID to int so that is the same as the data in JSON
            row['id'] = int(row['id'])
            # Price changed to float
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Access the columns by name
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        # Converts each row in a dict
        for row in rows:
            products.append(dict(row))

        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # We try to read the json file
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Extract the list from "items" key
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn´t exist, we send an empty list
        items_list = []
    # We use the list as an argument
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source', default='json')
    product_id = request.args.get('id', type=int)
    # Validate `source`
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    # Read the data
    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
        elif source == 'sql':
            data = read_sql()
    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    except Exception as e:
        return render_template('product_display.html', error=f"Data error: {str(e)}")   
    # Filter by ID if provided
    if product_id:
        # Search the product with that ID
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")
    # Render the template with data
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
