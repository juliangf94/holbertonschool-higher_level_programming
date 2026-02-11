# Python: File I/O and JSON Serialization
---
## 1. Why Python programming is awesome
Python is celebrated for its **readability** and **simplicity**. Its syntax mimics natural English, making it accessible for beginners. Additionally, Python has a massive ecosystem of libraries (for AI, web development, and data science), a supportive community, and it allows for rapid prototyping—you can write in a few lines what would take dozens in C++ or Java.

---
## 2. How to open a file
In Python, you use the built-in `open()` function, it returns a file object.  
It requires the file path and a **mode** (like 'r' for read, 'w' for write, 'a' for append).
```python
file = open("example.txt", "r")
```
-   The first argument is a string containing the filename.
-   The second argument is another string containing a few characters describing the way in which the file will be used. 
-   `mode` can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 
-   'r+' opens the file for both reading and writing. 
-   The mode argument is optional; 'r' will be assumed if it’s omitted.

---
##  3. How to write text in a file
To write text, open the file in 'w' (overwrite) or 'a' (append) mode and use the .write() method.

```Python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!")
```
---
##  4. How to read the full content of a file
You can use the .read() method without arguments to pull the entire file content into a single string.

```Python
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```
---
##  5. How to read a file line by line
The most memory-efficient way is to loop over the file object directly, or use .readlines() to get a list of strings.

```Python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```
---
##  6. How to move the cursor in a file
You use the .seek(offset) method. The offset represents the number of bytes from the beginning of the file. To find the current position, use .tell().

```Python

with open("example.txt", "r") as f:
    f.seek(5)  # Moves the cursor to the 6th byte
```   
---
##  7. How to make sure a file is closed after using it?
You can manually call `file.close()`.  
However, if an error occurs before that line, the file stays open.  
The best practice is to use the with statement.

##  8. What is and how to use the with statement?
The `with` statement creates a context manager.  
It ensures that resources (like file streams) are automatically closed as soon as the block of code is finished, even if an exception is raised.

##  9. What is JSON?
JSON (JavaScript Object Notation) is a lightweight, text-based data format used for data exchange.  
It is language-independent but uses a syntax similar to Python dictionaries and lists.  
In JSON, an object refers to any data wrapped in curly braces, similar to a Python dictionary.
We need to import it with `import json`
```python
import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
```
**Output**
```bash
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
"\"foo\bar"
"\u1234"
"\\"
{"a": 0, "b": 0, "c": 0}

'["streaming API"]'
```
**Decoding JSON**
```python
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
json.loads('"\\"foo\\bar"')
from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)
```
**Output**
```bash
['foo', {'bar': ['baz', None, 1.0, 2]}]
'"foo\x08ar'
['streaming API']

```

##  10. What is serialization?
Serialization is the process of converting a structured data object (like a Python dictionary) into a format that can be stored or transmitted (like a JSON string or a byte stream).

```python
import json
json.dump()
```
##  11. What is deserialization?
Deserialization is the reverse process: 
    -   Taking a stored format (like a JSON string) 
    -   Convert it back into a Python object (like a dictionary) that the program can manipulate.

##  12. How to convert a Python data structure to a JSON string?
Use the json module. The json.dumps() function (dump string) performs this conversion.

```Python
import json
data = {"name": "Julian", "age": 30}
json_string = json.dumps(data)
```
##  13. How to convert a JSON string to a Python data structure?
Use `json.loads()` (load string). This takes a JSON-formatted string and returns the corresponding Python object.

```Python
import json
json_string = '{"name": "Julian", "age": 30}'
data = json.loads(json_string)
```
##  14. How to access command line parameters in a Python script
You use the sys module, specifically sys.argv.

-   sys.argv[0] is the script name.
-   sys.argv[1] is the first argument provided.

```Python
import sys
print(f"First argument: {sys.argv[1]}")
```

---
---
#   Exercises
##  0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:  

`0-main.py`
```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

```
`0-read_file.py`
```python
#!/usr/bin/python3
"""
This module defines a function for reading a text file.
It contains the read_file function which handles UTF-8 encoding.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

```
**Logic**

**Output**
```bash
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
```

---
##  1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:  
`1-main.py`
```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

```
`1-write_file.py`
```python
#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file.
It returns the total number of characters written to the file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns character count.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

```
**Logic**

**Output**
```bash
24
```

---
##  2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:  
`2-main.py`
```python
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

```
`2-append_write.py`
```python
#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file.
It returns the number of characters added during the operation.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

```
**Logic**

**Output**
```bash
24
```

---
##  3. To JSON string
Write a function that returns the JSON representation of an object (string):  
`3-main.py`
```python
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`3-to_json_string.py`
```python
#!/usr/bin/python3
"""
This module defines a function that converts a Python object
to its JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The Python object to be serialized.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)

```
**Logic**

**Output**
```bash
[1, 2, 3]
<class 'str'>
{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
<class 'str'>
[TypeError] Object of type set is not JSON serializable
```

---
##  4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:  
`4-main.py`
```python
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`4-from_json_string.py`
```python
#!/usr/bin/python3
"""
This module defines a function that converts a JSON string
into a Python data structure.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The Python object (list, dict, str, etc.).
    """
    return json.loads(my_str)

```
**Logic**
-   Syntax Mapping: JSON's true, false, and null are automatically converted back to Python's True, False, and None.

-   The json.loads() Function: Unlike json.load() (which reads from a file object), json.loads() specifically takes a string as input.

-   Data Integrity: As shown in the 4-main.py output, if the JSON string is malformed (like missing quotes or using invalid Python-style set syntax), the function will naturally raise a json.decoder.JSONDecodeError. The task specifies we don't need to manage these exceptions manually.
**Output**
```bash
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```

---
##  5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:  
`5-main.py`
```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```
`5-save_to_json_file.py`
```python
#!/usr/bin/python3
"""
This module defines a function that writes an object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and saved.
        filename (str): The name of the file to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

```
**Logic**
-   `json.dumps()`:
    +   Este método toma un objeto de Python y lo convierte en una cadena de texto (string) en formato JSON. 
    +   No crea archivos; simplemente te entrega el texto para que lo uses en tu programa (por ejemplo, para enviarlo por una API o imprimirlo).
    +   Ejemplo:
        *   `json_texto = json.dumps(mi_diccionario)`
        +   Una variable de tipo str.

-   `json.dump()`:
    +   Este método toma un objeto de Python y lo escribe directamente en un archivo (o cualquier objeto que se comporte como un flujo de datos). 
    +   Requiere dos argumentos: el objeto y el archivo abierto.
    +   Ejemplo: 
        *   `json.dump(mi_diccionario, archivo_abierto)`
        +   El contenido se guarda en el disco duro.
**Output**
```bash
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]
```

---
##  6. Create object from a JSON file
Write a function that creates an Object from a "JSON file":  
`6-main.py`
```python
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`6-load_from_json_file.py`
```python
#!/usr/bin/python3
"""
This module defines a function that creates an Object from a JSON file.
It uses the json module to deserialize file content.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

```
**Logic**
-   `json.loads()`: From String
    +   Se utiliza cuando ya tienes el contenido JSON en una variable de texto (un string) dentro de tu programa y quieres transformarlo en un objeto de Python (diccionario o lista).
    +   Entrada: Objeto tipo `str`
    +   Ejemplo:
```python
json_string = '{"name": "Julian", "age": 30}'
data = json.loads(json_string)  # Convierte el texto a diccionario
```

-   `json.load()`: From File
    +   Se utiliza cuando el contenido JSON está guardado en un archivo físico en tu disco duro. 
    +   Lee el archivo y lo transforma directamente en un objeto de Python.
    +   Entrada: Un file object (el resultado de open())
    +   Se usa cuando necesitas leer configuraciones o bases de datos locales.
```python
with open("data.json", "r") as f:
    data = json.load(f)  # Lee directamente desde el archivo
```

**Output**
```bash
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[JSONDecodeError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
```

---
##  7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:  
`7-main.py`
```python

```
`7-add_item.py`
```python
#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves them to a JSON file named add_item.json.
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Checks if the file exists
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Only the words we use
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)

```
**Logic**

**Output**
```bash
["Best", "School", "89", "Python", "C"]
```

---
##  8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:  
`8-main.py`
```python
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

```
`8-class_to_json.py`
```python
#!/usr/bin/python3
"""
This module defines a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__

```
**Logic**

**Output**
```bash
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 8-my_class_2.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
```

---
##  9. Student to JSON
Write a class Student that defines a student by:  
`9-main.py`
```python
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

```
`9-student.py`
```python
#!/usr/bin/python3
"""
This module defines a Student class.
The class includes methods to represent the student as a dictionary.
"""


class Student:
    """
    Representation of a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance with specific attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary containing student attributes.
        """
        return self.__dict__

```
**Logic**

**Output**
```bash
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
```

---
##  10. Student to JSON with filter
Write a class Student that defines a student by: (based on 9-student.py)  
`10-main.py`
```python
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

```
`10-student.py`
```python
#!/usr/bin/python3
"""
This module defines a Student class with attribute filtering.
It allows converting the object to a dictionary with specific keys.
"""


class Student:
    """
    Representation of a student with filtering capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student.
        If attrs is a list of strings, only those attributes are included.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The filtered or full dictionary of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for a in attrs:
                if a in self.__dict__:
                    res[a] = self.__dict__[a]
            return res
        return self.__dict__

```
**Logic**
-   Primero verifica si recibiste una lista de strings. Si attrs es ['first_name'], el código entra en el if.

-   Crea un diccionario vacío (res). Luego recorre los nombres que pediste. Si el nombre existe en el objeto (if a in self.__dict__), lo copia al nuevo diccionario.

-   Si no te pasaron ninguna lista (o pasaron algo inválido), el código simplemente dice: "Toma todo lo que tengo" devolviendo self.__dict__.

**Output**
```bash
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
```

---
##  11. Student to disk and reload
Write a class Student that defines a student by: (based on 10-student.py)  
`11-main.py`
```python
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
```
`11-student.py`
```python
#!/usr/bin/python3
"""
This module defines a Student class with filtering and reloading.
It allows converting the object to a dictionary and updating it.
"""


class Student:
    """
    Representation of a student with reloading capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student.
        If attrs is a list of strings, only those attributes are included.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The filtered or full dictionary of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for a in attrs:
                if a in self.__dict__:
                    res[a] = self.__dict__[a]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        
        Args:
            json (dict): A dictionary where keys are attribute names
                         and values are the new values for those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)

```
**Logic**
-   json.items(): Toma el diccionario que le pasas (que suele venir de un archivo .json previamente leído) y lo descompone en parejas de clave y valor.

-   setattr(self, key, value): Esta es la función mágica de Python.
    +   self: El objeto que queremos modificar.
    +   key: El nombre del atributo (ej: "age").
    +   value: El nuevo valor (ej: 24).
    +   Resultado: Es exactamente igual a escribir self.age = 24, pero de forma automática para cualquier cantidad de datos que vengan en el diccionario.
**Output**
```bash
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
guillaume@ubuntu:~/$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
```

---
##  12. Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal's triangle of n:  
`12-main.py`
```python
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```
`12-pascal_triangle.py`
```python
#!/usr/bin/python3
"""
This module contains the function pascal_triangle.
It generates a Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle as a list of lists.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Start the new row with 1
        new_row = [1]

        # Calculate the numbers between the 1s
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # End the new row with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle

```
**Logic**

**Output**
```bash
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

---


python3 -m doctest ./tests/*
