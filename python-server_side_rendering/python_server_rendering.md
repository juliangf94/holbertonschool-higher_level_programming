# Python — Server Side Rendering

---

## ¿Qué es `Server-Side Rendering` (SSR)?

El **SSR** es una técnica donde el servidor genera el HTML completo y lo envía al cliente listo para mostrar.  
Esto contrasta con el **CSR (`Client-Side Rendering`)** donde el browser construye la página con JavaScript.

| | SSR | CSR |
|---|-----|-----|
| ¿Dónde se genera el HTML? | En el servidor | En el browser |
| SEO | ✅ Mejor | ❌ Más difícil |
| Primera carga | ✅ Más rápida | ❌ Más lenta |
| Interactividad | 🟡 Media | ✅ Alta |
| Ejemplo | Flask + Jinja | React, Vue |

---

## Stack de este proyecto

- **Python + Flask** — framework web del servidor
- **Jinja2** — motor de templates para generar HTML dinámico
- **JSON / CSV / SQLite** — fuentes de datos

---

---

# TASK 0 — Creating a Simple Templating Program
In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects.  
Each output file should be named sequentially, starting from 1.  
You will also implement specific error handling for various edge cases.
**Objective**
-   Understand how to use string templating in Python.
-   Implement file operations for reading templates and writing output files.
-   Handle various edge cases and errors gracefully.

---

## Código

**Archivo:** `task_00_intro.py`
```python
import logging

def generate_invitations(template, attendees):
    # Validar tipos de input
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # Validar que no estén vacíos
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Procesar cada attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", str(attendee.get("name") or "N/A"))
        output = output.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        output = output.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        output = output.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            logging.warning("File {} already exists, overwriting.".format(filename))

        try:
            with open(filename, 'w') as f:
                f.write(output)
        except Exception as e:
            logging.error("Failed to write file {}: {}".format(filename, e))
```

---

## Explicación línea por línea
### Import
```python
import logging
```
- Se importa `logging` para registrar mensajes de error en lugar de usar `print()`.
- **¿Por qué logging y no print?** En proyectos reales, `logging` permite controlar el nivel de los mensajes (ERROR, WARNING, INFO) y redirigirlos a archivos. Es la práctica estándar en Python.

---

### Validación de tipos
```python
if not isinstance(template, str):
    logging.error("Invalid input: template must be a string.")
    return
if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
    logging.error("Invalid input: attendees must be a list of dictionaries.")
    return
```
- `isinstance(template, str)` verifica que `template` sea un string.
- `isinstance(attendees, list)` verifica que sea una lista.
- `all(isinstance(a, dict) for a in attendees)` verifica que **cada elemento** de la lista sea un diccionario.
- **¿Por qué `return` después del error?** Para terminar la función inmediatamente sin continuar la ejecución.

---

### Validación de contenido vacío
```python
if not template:
    logging.error("Template is empty, no output files generated.")
    return
if not attendees:
    logging.error("No data provided, no output files generated.")
    return
```
- `not template` es `True` si el string está vacío (`""`).
- `not attendees` es `True` si la lista está vacía (`[]`).
- **¿Por qué separar esta validación de la anterior?** Porque el tipo puede ser correcto (string) pero el contenido vacío. Son dos errores distintos con mensajes distintos.

---

### Procesamiento de cada attendee
```python
for index, attendee in enumerate(attendees, start=1):
```
- `enumerate` itera sobre la lista y devuelve el índice + el elemento.
- `start=1` hace que el índice empiece en 1 (no en 0) para nombrar los archivos `output_1.txt`, `output_2.txt`, etc.

```python
output = template
output = output.replace("{name}", str(attendee.get("name") or "N/A"))
```
- Se copia el template en `output` para no modificar el original en cada iteración.
- `.get("name")` devuelve `None` si la clave no existe (en vez de tirar un `KeyError`).
- `or "N/A"` reemplaza `None` y valores falsy (como `""`) por `"N/A"`.
- `str(...)` convierte el valor a string por seguridad.
- **¿Por qué `attendee.get()` y no `attendee["name"]`?** Porque `dict["key"]` tira `KeyError` si la clave no existe. `.get()` devuelve `None` de forma segura.

---

### Escritura del archivo
```python
filename = f"output_{index}.txt"
if os.path.exists(filename):
    logging.warning("File {} already exists, overwriting.".format(filename))

try:
    with open(filename, 'w') as f:
        f.write(output)
except Exception as e:
    logging.error("Failed to write file {}: {}".format(filename, e))
```
- `f"output_{index}.txt"` crea el nombre del archivo con f-string.
-  `os.path.exists`:
    +   Antes de escribir, chequea si el archivo ya existe.
    +   Si existe, loguea un **warning** en vez de sobreescribir silenciosamente.
-   `try/except`:
    +   Envuelve el `open()` y el `write()`.
    +   Si por alguna razón falla la escritura (permisos, disco lleno, etc.), captura el error y lo loguea en vez de crashear el programa.
- `with open(...) as f` abre el archivo y lo cierra automáticamente al salir del bloque.
- `'w'` = modo escritura (crea el archivo si no existe, lo sobreescribe si ya existe).
- **¿Por qué `with`?** Garantiza que el archivo se cierre correctamente aunque ocurra un error.

---

## Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| `isinstance()` | Verifica el tipo de una variable |
| `logging.error()` | Registra un mensaje de error |
| `dict.get(key)` | Accede a un valor sin riesgo de KeyError |
| `enumerate(list, start=1)` | Itera con índice empezando desde 1 |
| `str.replace(old, new)` | Reemplaza texto en un string |
| `with open() as f` | Abre y cierra archivos de forma segura |

---

## Comando para testear

```bash
# Crear el archivo template.txt primero
cat > template.txt << 'EOF'
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
EOF

# Correr el main de prueba
python3 main_00_intro.py

# Ver los archivos generados
ls output_*.txt
cat output_1.txt
cat output_2.txt
cat output_3.txt
```

**Output esperado en `output_1.txt`:**
```
Hello Alice,

You are invited to the Python Conference on 2023-07-15 at New York.

We look forward to your presence.

Best regards,
Event Team
```

**Output esperado en `output_3.txt`** (con `event_date: None` → `N/A`):
```
Hello Charlie,

You are invited to the AI Summit on N/A at Boston.

We look forward to your presence.

Best regards,
Event Team
```

---

# TASK 1 — Creating a Basic HTML Template in Flask
In this task, you will build a basic Flask application that serves a web page using a Jinja template.  
You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask.  
Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.
**Objective**
-   Set up a Flask environment and create a basic Flask application.
-   Design HTML templates using Jinja for dynamic content rendering.
-   Implement reusable components in templates to maintain consistent layout across pages.
## Codigo
`task_01_jinja.py`
```python
```
`index.html`
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple Flask application demonstrating Server-Side Rendering.</p>
        <ul>
            <li>Flask</li>
            <li>HTML</li>
            <li>Templates (Jinja)</li>
        </ul>
    </main>

    {% include 'footer.html' %}
</body>
</html>
```
`about.html`
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>About Us</h1>
        <p>We are learning how to build scalable web applications using Python and Flask.</p>
    </main>

    {% include 'footer.html' %}
</body>
</html>
``` 
`contact.html`
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}
    
    <main>
        <h1>Contact Us</h1>
        <p>Feel free to reach out to us at contact@myflaskapp.com.</p>
    </main>

    {% include 'footer.html' %}
</body>
</html>
```

### **Logic**
1.   `Jinja2`: 
-   Es el motor de plantillas de Flask. 
-   Permite usar lógica de programación (if, for, include) dentro del HTML.

2.  `render_template`: 
-   Función de Flask que busca archivos dentro de la carpeta /templates, procesa las etiquetas de Jinja y devuelve HTML puro al navegador.

3.  `Dry Principle (Don't Repeat Yourself)`: 
-   Al usar **`{% include %}`**, evitamos copiar el mismo código del menú de navegación en cada archivo. 
-   Si cambias el header, se actualiza en todo el sitio.


---

# TASK 2 — Creating a Dynamic Template with Loops and Conditions in Flask
In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja's loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.
**Objective**
-   Use Jinja's loop and conditional constructs to dynamically render content in HTML templates.
-   Read and parse JSON data in Python.
-   Integrate dynamic content into your Flask application.
`task_02_logic.py`
```python
from flask import Flask, render_template
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)

```

**Logic**
1.  `json.load(f)`: 
-   Convierte el texto del archivo .json en un diccionario de Python automáticamente.

2.  `render_template(..., items=items_list)`: 
-   El primer `items` es el nombre que usaremos dentro del HTML. 
-   El segundo es la variable de Python que contiene los datos.

3.  El bucle `{% for item in items %}`: 
-   Jinja repetirá la etiqueta <li> tantas veces como elementos haya en la lista. 
-   Es idéntico a un `for` de Python pero dentro del HTML.

4.  El condicional `{% if items %}`: 
-   En Python (y Jinja), una lista vacía se evalúa como False. 
-   Si la lista tiene algo, muestra la <ul>; si está vacía, salta al `{% else %}` y muestra el mensaje de error.
**Output**
```bash

```

---

#  TASK 3 — Displaying Data from JSON or CSV Files in Flask
In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV.  
You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL.  
You will add functionality to your Flask application to filter product data based on an optional `id` query parameter.  
Additionally, you will handle edge cases such as invalid `source` parameter values or when the specified `id` is not found in the data.

**Objective**
-   Read and parse data from JSON and CSV files.
-   Use query parameters in Flask to determine data sources and filter criteria.
-   Implement error handling for invalid inputs and missing data.
-   Render dynamic data in HTML templates using Jinja.
## Codigo
### `products.json`
```json
```
### `product_display.html`
```html
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
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    # Validate `source`
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    # Read the data
    try:
        if source == 'json':
            data = read_json('products.json')
        else:
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

```
### `task_03_files.py`
```python
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

```

**Logic**
1.  `request.args.get('id', type=int)`: 
-   Esto es genial porque Flask intenta convertir el ID de la URL (que siempre es texto) a un número automáticamente.
2.  `csv.DictReader`: 
-   Transforma cada fila del CSV en un diccionario donde las llaves son los nombres de las columnas. ¡Súper útil!
3.  **List Comprehension**: 
-   Usamos `[p for p in data if p.get('id') == product_id]` para filtrar la lista de forma rápida y elegante.
4.  **Manejo de Errores**: 
-   En lugar de mostrar una página de error fea de Flask, le pasamos una variable `error` a nuestra propia plantilla para que se vea profesional.

**Output**
```bash

```

---

# TASK 4 — Extending Dynamic Data Display to Include SQLite in Flask
Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the source query parameter.
**Objective**
-   Set up and interact with a SQLite database in a Flask application.
-   Extend existing functionality to handle multiple data sources.
-   Implement error handling for database-related issues.
`task_04_db.py`
```python
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

```

**Logic**
### `task_04_db.py`
`sqlite3.Row`
Por defecto, SQLite devuelve los datos como tuplas (ej: `(1, 'Laptop', 799.99)`).  
Tu HTML espera diccionarios (ej: `product.name`).
-   Al usar `conn.row_factory = sqlite3.Row`, Python crea objetos que se comportan como diccionarios.  
-   Al hacer `dict(row)`, transformamos la fila de la base de datos en un formato idéntico al que devuelve el archivo JSON.  
Por eso no tienes que cambiar tu `product_display.html`.
**Output**
```bash

```

---
