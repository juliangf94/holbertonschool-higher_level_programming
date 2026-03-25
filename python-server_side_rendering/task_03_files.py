import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    """Lee y retorna datos desde un archivo JSON."""
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv(filename):
    """Lee y retorna datos desde un archivo CSV como una lista de diccionarios."""
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convertimos el ID a entero para que coincida con el tipo de dato de JSON
            row['id'] = int(row['id'])
            # El precio también suele ser mejor como float si vas a hacer cálculos
            row['price'] = float(row['price'])
            products.append(row)
    return products


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
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    # Read the data
    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    # Filter by ID if provided
    if product_id:
        # Search the product with that ID
        filtered_data = [p for p in data if p.get('id') == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data
    # Render the template with data
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
