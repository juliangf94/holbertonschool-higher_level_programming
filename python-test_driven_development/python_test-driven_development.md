# Python Testing and Documentation

## Why Python programming is awesome

Python is an excellent programming language because it emphasizes **readability, simplicity, and productivity**. Its clean syntax allows developers to write fewer lines of code while maintaining clarity. Python has a vast standard library and a strong ecosystem of third-party packages, making it suitable for automation, web development, data analysis, testing, and scripting. Its community and documentation further enhance its reliability and long-term usability.

---

## What’s an interactive test

An interactive test is a test that is written **inside documentation**, usually in a docstring, and can be executed automatically to verify that the documented examples behave as expected. In Python, these are commonly implemented using **doctest**.

Interactive tests look like real Python interpreter sessions and allow documentation and testing to be combined in a single place.

---

## Why tests are important

Tests are important because they:

* Ensure that code behaves as expected
* Help detect bugs early
* Prevent regressions when code is modified
* Improve code quality and confidence
* Serve as executable documentation

Well-tested code is easier to maintain, refactor, and debug.

---

## How to write Docstrings to create tests

Docstrings can include interactive tests by writing examples that mimic the Python interpreter prompt (`>>>`). These examples describe expected input and output.

When executed, Python checks whether the actual output matches the documented result. This ensures that examples in the documentation remain accurate and functional.

---

## How to write documentation for each module and function

* **Modules** should have a docstring at the top of the file explaining their purpose and usage.
* **Functions** should have docstrings that describe what the function does, its parameters, return values, and possible exceptions.

Clear documentation makes code easier to understand, reuse, and test.

---

## What are the basic option flags to create tests

When using `doctest`, common option flags include:

* `-v` for verbose output
* `-m doctest` to run doctests in a module

Option flags control how tests are executed and how results are displayed.

---

## How to find edge cases

Edge cases are unusual or extreme inputs that may cause unexpected behavior. They can be found by:

* Testing minimum and maximum values
* Testing empty or null inputs
* Testing invalid or unexpected data types
* Testing boundary conditions

Identifying edge cases helps ensure that code is robust and reliable.

---
--------------------------------------------------------------------------------------------------------------------------
#   Quiz
## Question #0

Is this a standardized way to comment a function in Python?

```python
/* Addition function */
def add(a, b):
    return a + b
```

*   [ ]Yes
*   [x]No

Motivo:
-   /* */ es sintaxis de comentarios de C/C++. No existe en Python.

---

## Question #1

Is this a standardized way to comment a function in Python?

```python
"""" Addition function """
def add(a, b):
    return a + b
```

*   [ ]Yes
*   [x]No

Motivo:
Cuatro comillas ("""") no son una docstring válida en Python.
Las docstrings usan triple comillas, no cuatro.

---

## Question #2

Is this a standardized way to comment a function in Python?

```python
##########
# Addition function
##########
def add(a, b):
    return a + b
```

*   [ ]Yes
*   [x]No


Motivo:
Esto es un comentario válido, pero no es el estándar para documentar funciones.
Python usa docstrings, no bloques de #.
---

## Question #3

Is this a standardized way to comment a function in Python?

```python
def add(a, b):
    """ Addition function """
    return a + b
```

*   [x]Yes
*   [ ]No
Motivo:
Esta es una docstring correcta, colocada inmediatamente después de la definición de la función.
---

## Question #4

Is this module correctly commented?

```python
#!/usr/bin/python3
"""
    My calculation module
"""
import sys
...
```

*   [x]Yes
*   [ ]No

Respuesta: ✅ Yes

Motivo:
-   La docstring del módulo:
-   Está justo después del shebang
-   Antes de cualquier código ejecutable
-   Cumple con el estándar PEP 25
---

## Question #5

Is this module correctly commented?

```python
#!/usr/bin/python3
import sys

"""
    My calculation module
"""
...
```

*   [ ]Yes
*   [x]No
Motivo:
La docstring del módulo debe ir antes de cualquier import.
Aquí aparece después de import sys, por lo que no es válida.
---

## Question #6

Based on this code, what should all the test cases be? (select multiple)

```python
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```

*   [x]* empty list
*   [x]* list with one element (any type)
*   [x]* list with 2 different element (same type)
*   [x]* list with twice the same element (same type)
*   [x]* list with more than 2 times the same element (same type)
*   [x]* list with multiple types (integer, string, etc…)
*   [x]* not a list argument (ex: passing a dictionary to the method)

Motivo:
Una buena batería de tests debe cubrir:
-   Casos normales
-   Casos límite
-   Casos inválidos
-------------------------------------------------------------
#   Exercises
## 0-add_integer.py, tests/0-add_integer.txt
`0-main.py`
```python
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
```
`0-add_integer.py`
```python


```
Output:
```bash
guillaume@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 2-matrix_divided.py, tests/2-matrix_divided.txt
Write a function that divides all elements of a matrix.
`2-main.py`
```python
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
```
``
```python


```
Output:
```bash
guillaume@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 3-say_my_name.py, tests/3-say_my_name.txt
Write a function that prints My name is <first name> <last name>
`-main.py`
```python
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

```
``
```python


```
Output:
```bash
guillaume@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 4-print_square.py, tests/4-print_square.txt
`4-main.py`
```python
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

```
`4-print_square.py, tests/4-print_square.txt`
```python


```
Output:
```bash
guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 5-text_indentation.py, tests/5-text_indentation.txt
`5-main.py`
```python
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

```
`5-text_indentation.py, tests/5-text_indentation.txt`
```python
#!/usr/bin/python3
"""
Module 5-text_indentation
Provides a function that indents text based on specific characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
```
*   ```python 
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ```
    -   Sirve para validar que recibimos un texto
*   ```python

    ```
    -   
*   ```python
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    ```
    -   Salta los espacios que puedan estar al puro principio de todo el texto.
    -   Incrementamos el índice c hasta que encontramos la primera letra real.
*   ```python
    while c < len(text):
        print(text[c], end="") # Imprimimos el carácter actual
    ```
    -   Imprimimos la letra actual y usamos end="" para que Python no salte de línea automáticamente, ya que nosotros queremos controlar cuándo ocurre eso.
*   ```python
    if text[c] in ".?:":
        print("\n") # Esto imprime DOS líneas nuevas (el salto actual + \n)
    ```
    -   Si la letra que acabamos de imprimir es un ., ? o :, entramos en el modo "limpieza". El print("\n") genera el espacio vertical que ves en el ejemplo de cat -e como $$.
*   ```python
    c += 1 # Pasamos al siguiente carácter
    while c < len(text) and text[c] == ' ':
        c += 1 # Si es un espacio, lo ignoramos y seguimos avanzando
    continue # Saltamos al inicio del bucle principal sin incrementar 'c' otra vez
    ```
    -   Después de un punto, suele haber un espacio (ej: Hola. Mundo). 
    -   El ejercicio dice que no debe haber espacios al inicio de la línea. 
    -   Este bucle "se come" todos los espacios que siguen al punto hasta encontrar la próxima letra (Mundo). 
    -   Al usar continue, evitamos que el código de abajo mueva el índice de nuevo.

///////////////////////////////////////////////////
Output:
```bash
guillaume@ubuntu:~/$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
```


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## tests/6-max_integer_test.py
`6-main.py`
```python
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

```
`6-max_integer.py`
```python
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

```
`6-max_integer_test.py`
```python


```
Output:
```bash

```

touch 0-add_integer.py 2-matrix_divided.py 3-say_my_name.py 4-print_square.py  5-text_indentation.py 0-main.py 2-main.py 3-main.py 4-main.py 5-main.py 6-main.py README.md

touch 0-add_integer.txt 2-matrix_divided.txt 3-say_my_name.txt 4-print_square.txt 5-text_indentation.txt 6-max_integer_test.py

pycodestyle *.py

python3 -m doctest ./tests/*


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')  

### Que es?
Es el docstring del archivo completo, describe para qué sirve el módulo.
## Donde va?
Siempre en la primera línea real del archivo, justo después del shebang.

```python
#!/usr/bin/python3
"""Module that provides a function to add two integers."""
```
Verificacion:
```bash
python3 -c 'print(__import__("0-add_integer").__doc__)'
```
Esto imprime el docstring del módulo, no de la función.
*   Holberton pide:
    -   Una frase completa
    -   Que explique el propósito del archivo
    -   No una sola palabra
    -   Longitud mínima (la miden con wc -l)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
##  Que es?
* Es el docstring de la función, explica:
    -   Qué hace
    -   Qué parámetros recibe
    -   Qué devuelve
    -   Qué errores puede lanzar

##  Donde va?
Va debajo de la definicion de la función
```python
def add_integer(a, b=98):
    """Adds two integers and returns the result."""
    return a + b

```
Verificacion:
```bash
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
```
Esto imprime solo el docstring de la función, no el del módulo.
