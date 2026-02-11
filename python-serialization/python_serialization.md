#   Mastering Data Transformation: Serialization & Marshaling1. 
##  What is Marshaling?
Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network.  
It involves packaging complex objects and their attributes into a simpler, often binary, format.  
This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.
##  What is Serialization?
Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network.  
The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere.  
This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

##   Differences
1)  Differences and Similarities: Marshaling vs. Serialization  
While often used interchangeably, these terms have distinct technical focuses.
**The Similarities**
    -   Purpose: Both aim to convert complex memory objects into a format (like a byte stream or text) that can be easily stored or transmitted.
    -   Result: The output is a flattened representation of the original data structure.
**The Differences**
| Feature | Serialization | Marshaling |
| :--- | :--- | :--- |
| Primary Goal | Data Persistence: Saving the state of an object to recreate it exactly later. | Communication: Sending objects to a different process or remote system. | 
| Focus | Focuses strictly on data structures and attributes. | Can include the object's code, methods, and interface definitions. | 
| Context | Files, Databases, Local caching. | Remote Procedure Calls (RPC), Network sockets, Distributed systems. |

2) Practical Implementation in Programming  
In the context of your current Python project, serialization follows a logical flow:
    -   Extraction: Accessing the internal state of a Class (often via self.__dict__).
    -   Transformation: Using a library (like json) to turn that dictionary into a string.
    -   Storage: Writing that string into a physical file on the disk using the with open() statement.
        +   Example: Converting a Python object Student("Julian", 30) into the string '{"name": "Julian", "age": 30}' is a practical implementation of serialization.

3) Real-World Applications
Serialized data is the "universal language" of modern computing:
    -   Web Applications: APIs use JSON to send data from a server (Python/Java) to a browser (JavaScript). The browser doesn't understand Python objects, but it understands the serialized JSON string.
    -   Databases: NoSQL databases like MongoDB store data in BSON (Binary JSON) format, which is a serialized version of your objects.
    -   Network Communications: When different systems (e.g., a Mac and a Linux server) communicate, they use a standard serialized format so that hardware architecture differences (endianness) don't corrupt the data.

4) Performance Implications of Formats  
Choosing the right format depends on whether you value human readability or computer efficiency.
Comparison Table
| Format | Readability | Size/Performance | Best Use Case | 
| :--- | :--- | :--- | :--- |
| JSON | High | Moderate | Web APIs, Configuration files, Small datasets. | 
| XML | Moderate | Heavy (verbose) | Legacy enterprise systems, Financial transactions. | 
| Binary | None | Fast & Compact | High-performance gaming, Real-time video streaming. |


---
---
#   Exercises
##  0. Basic Serialization
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
`0_main.py`
```python
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
```
`task_00_basic_serialization.py`
```python
#!/usr/bin/env python3
"""
Module for basic serialization.
Provides functions to save a dictionary to a JSON file and load it back.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

```
**Logic**
Tienes un "mueble" (un objeto en la memoria de Python, como un diccionario o una lista) que es útil pero ocupa un lugar específico en tu "casa" (la memoria RAM). Si quieres mandarle ese mueble a un amigo o guardarlo en el trastero (el disco duro), no puedes enviarlo armado porque no pasa por la puerta.

-   Serializar: Es desarmar el mueble y poner todas las piezas y el manual en una caja (un archivo .json o un flujo de datos). Ahora es solo una fila de piezas una tras otra.

-   Deserializar: Es cuando tu amigo recibe la caja, lee el manual y vuelve a armar el mueble exactamente como estaba en tu casa

| Función | ¿Cuándo se usa? | Destino / Origen |
| :--- | :--- | :--- |
| dump / load | Cuando trabajas con Archivos | El disco duro (archivo físico .json). |
| dumps / loads | Cuando trabajas con Strings | Una variable de texto en la memoria RAM. |
**Output**
```bash
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```
---
##  1. Pickling Custom Classes
Learn how to serialize and deserialize custom Python objects using the `pickle` module.
`1_main.py`
```python
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
```
`task_01_pickle.py`
```python
#!/usr/bin/env python3
"""
Module for custom object serialization using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with basic attributes.
    """

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads an instance of CustomObject from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None

```
**Logic**
Why Pickle is different from JSON
-   Binary Format: 
    +   JSON produces text (human-readable), but Pickle produces binary data.
    +   That's why we use 'wb' (write binary) and 'rb' (read binary).
-   State and Logic: 
    +   JSON only saves the data (the values). 
    +   Pickle saves the entire object structure. When you deserialize with Pickle, you get back an actual instance of CustomObject with all its methods ready to be called.
-   The @classmethod: 
    +   We use a class method for deserialize because at that moment, the object doesn't exist yet. 
    +   We are asking the Class to go to the disk, find the data, and "give birth" to a new instance.
**JSON vs Picke**
-   JSON (El Mensajero)
    +   Formato: Texto (parece un diccionario de Python).
    +   Idioma: Universal (lo entiende cualquier lenguaje).
    +   ¿Qué guarda?: Solo datos (números, texto, listas).
    +   Uso ideal: Enviar datos por internet o guardar configuraciones que quieras leer tú mismo.

-   Pickle (El Clonador)
    +   Formato: Binario.
    +   Idioma: Solo Python.
    +   ¿Qué guarda?: El objeto completo (datos + funciones + estructura de clase).
    +   Uso ideal: Guardar modelos de IA o estados de juegos complejos para usarlos luego en Python.

-   Resumen
    +   Usa JSON para compartir información con el mundo; usa Pickle para guardar cosas complejas de Python para ti mismo
**Output**
```bash
Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
```
---
##  2. Converting CSV Data to JSON Format
The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.
`main_02_csv.py `
```python
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```
`data.csv`
```csv
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```
`task_02_csv.py`
```python
#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts its content into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if successful, False if an error occurred.
    """
    try:
        data_list = []

        #   Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            #   DictReader transforms each line in a dict automatically
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        #   Write the dict's list in data.json
        #   We can use either mode="w" or "w"
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            #   indent=4 is use for jumps in line and space
            json.dump(data_list, json_file, indent=4)
        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False

```
**Logic**

**Output**
```bash
[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]
```
---
##  3. Serializing and Deserializing with XML
In this exercise we'll explore serialization and deserialization using XML as an alternative format to JSON.
`3_main.py`
```python
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
```
`data.xml`
```xml
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```
`task_03_xml.py`
```python

```
**Logic**
**serialize**
-   `ET.Element("data")`: 
    +   Aquí creas la etiqueta principal, la que encerrará todo. 
    +   Todo lo que guardemos debe estar dentro de esta "caja" raíz.
    +   En el archivo se verá como <data> ... </data>. 
-   `child = ET.SubElement(root, key)`: 
    +   Creas una "etiqueta hija" dentro de <data> usando la llave del diccionario.
    +   Ahora tienes <data><name></name></data>. 
    +   Por cada par clave-valor en tu diccionario, creamos una etiqueta con el nombre de la clave (ej: <name>) y le asignamos el contenido (John).
-    `child.text = str(value)`:
    +   XML trata todo como texto. 
    +   Le pones el contenido a esa etiqueta. 
    +   Es fundamental el str() porque XML no entiende de números o booleanos, solo de texto. 
    +   Ahora tienes <data><name>John</name></data>.
    +   Si guardas un número (28), al recuperarlo seguirá siendo un string ("28").
    +   En aplicaciones más complejas, tendrías que convertir los tipos manualmente.
---
-   `tree = ET.ElementTree(root)`: 
    +   Conviertes ese diseño que hiciste en un objeto "Árbol" que Python puede procesar como un archivo completo.
-   `tree.write(filename)`: 
    +   Python escribe todo ese árbol en el disco duro con el nombre que elegiste.
---
**deserialize**
-   `tree = ET.parse(filename)`: 
    +   Python abre el archivo y analiza la estructura para asegurarse de que el XML esté bien escrito.
-   `root = tree.getroot()`: 
    +   Le pides a Python que te dé acceso al elemento principal (<data>).
    +   Esto es necesario para poder ver qué hay dentro.
    +   Al deserializar, esto nos da acceso al elemento <data>, permitiéndonos iterar por sus "hijos" para sacar los nombres de las etiquetas (child.tag) y sus valores (`child.text`).
---
-   `deserialized_dict = {}`: 
    +   Creas un diccionario vacío donde irás guardando los datos recuperados.
-   `for child in root:`: 
    +   Recorres cada etiqueta que esté dentro de <data>.
    +   `child.tag`: 
        *   Es el nombre de la etiqueta (ej: "name"). 
        *   Esto se convierte en la llave de tu diccionario.
    +   `child.text`: 
        *   Es el contenido que está entre las etiquetas (ej: "John"). 
        *   Esto se convierte en el valor.
    +   `deserialized_dict[child.tag] = child.text`: 
        *   Metes la pareja llave-valor en tu diccionario.
-   `return deserialized_dict`: 
    +   Una vez que termina de leer todas las etiquetas, te entrega el diccionario armado.

**Output**
```bash
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```
**data-xml**
```bash
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```
