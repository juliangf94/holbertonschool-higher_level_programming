# Python Exceptions – Overview
## Why Python programming is awesome

Python is considered an awesome programming language because it is **simple, readable, and powerful**. Its clear syntax allows developers to focus on solving problems rather than dealing with complex language rules. Python supports multiple programming paradigms (procedural, object‑oriented, and functional), has a massive standard library, and a very large ecosystem of third‑party packages. This makes Python suitable for web development, automation, data science, scripting, and system programming.

---

## What’s the difference between errors and exceptions

* **Errors** are serious problems that usually cannot be handled by the program (e.g., syntax errors).
* **Exceptions** are runtime issues that occur during execution and **can be handled** using exception handling mechanisms.

**all exceptions are errors, but not all errors are exceptions**.

---

## What are exceptions and how to use them

Exceptions are events that occur when something unexpected happens during program execution (such as dividing by zero or accessing a missing key in a dictionary).
They are used with the `try` / `except` blocks:

* Code that might fail is placed inside `try`
* Code that handles the failure is placed inside `except`

This allows the program to continue running instead of crashing.

---

## When do we need to use exceptions

Exceptions should be used when:
* An error is **expected but not guaranteed** to happen
* You want to prevent the program from stopping abruptly
* You need to handle invalid input, missing resources, or runtime failures

They should **not** be used for normal control flow.

---

## How to correctly handle an exception

To correctly handle an exception:

* Catch **specific exceptions**, not generic ones when possible
* Provide a meaningful response or fallback behavior
* Avoid silently ignoring exceptions

This improves reliability, debugging, and code readability.

---

## What’s the purpose of catching exceptions

Catching exceptions allows a program to:

* Avoid crashing
* Handle errors gracefully
* Provide useful error messages
* Ensure the program remains stable

It gives the developer control over how failures are managed.

---

## How to raise a builtin exception

Python allows raising built‑in exceptions explicitly using the `raise` keyword. This is useful when you detect an invalid state in your program and want to stop execution with a clear reason.

Raising exceptions helps enforce rules and signal errors clearly.

---

## When do we need to implement a clean‑up action after an exception

A clean‑up action is needed when resources must be released regardless of whether an error occurs, such as:

* Closing files
* Releasing locks
* Closing network connections

This is typically done using a `finally` block or context managers to ensure proper resource management even when exceptions happen.

--------------------------------------------------------------------------------------------------------------------------
#   Quiz

--------------------------------------------------------------------------------------------------------------------------
#   Exercises
## 0-safe_print_list.py
Write a function that prints x elements of a list.
`0-main.py`
```python
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

```
`0-safe_print_list.py`
```python
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count


```
*   `end=""`: se imprime usando para que el siguiente elemento se imprima en la misma línea.  
*   `print("")`: Una vez fuera del bucle, imprimimos una línea vacía para cumplir con el requisito de "followed by a new line".  

Output:
```bash
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 1-safe_print_integer.py
Write a function that prints an integer with "{:d}".format().
`1-main.py`
```python
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

```
`1-safe_print_integer.py`
```python
#!/usr/bin/python3
def safe_print_integer(value):
        try:
            print("{:d}".format(value))
            return True
        except (ValueError, TypeError):
            return False

```
*   `except (ValueError, TypeError)`:
    -   Si pasas un string como "School", Python lanzará un `ValueError` (porque el formato no coincide).
    -   Si pasas algo más complejo que no se puede convertir, podría lanzar un `TypeError`.  
    
Output:
```bash
89
-89
School is not an integer
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 2-safe_print_list_integers.py
Write a function that prints the first x elements of a list and only integers.
`2-main.py`
```python
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

```
`2-safe_print_list_integers.py`
```python
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count

```
 *  `for i in range(x)`: usamos range(x) ya que intentamos acceder a los priemros x elementos.
    -   Si x es menor que la lista: Imprimes hasta x y te detienes.
    -   Si x es mayor que la lista: Sigues intentando hasta que te acabas la lista y, en ese momento, ocurre el IndexError.
*   Cuando `"{:d}".format()` encuentra un string como "School" o una lista [1, 2, 3], lanza uno de estos dos errores

Output:
```bash
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in 
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 3-safe_print_division.py
Write a function that divides 2 integers and prints the result.
`3-main.py`
```python
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
```
`3-safe_print_division.py`
```python
#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b        
    except ZeroDivisionError:
        pass    
    finally:
        print("Inside result: {}".format(result))
    return result
 
```
*   `result = None`: Inicializamos la variable fuera del try. Si la división falla, result mantendrá este valor.
*   `except ZeroDivisionError`: Capturamos específicamente el error de dividir por cero.
*   `finally` : Corre siempre
Output:
```bash
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 4-list_division.py
Write a function that divides element by element 2 lists.
`4-main.py`
```python
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

```
`4-list_division.py`
```python
#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            res = elem_1 / elem_2
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list

```
Output:
```bash
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 5-raise_exception.py
Write a function that raises a type exception.
`5-main.py`
```python
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

```
`5-raise_exception.py`
```python
#!/usr/bin/python3
def raise_exception():
    raise TypeError

```
*   `raise`: Es la instrucción que le dice a Python: "Detén todo, ha ocurrido un problema".
*   `TypeError`: Es una de las excepciones integradas de Python. Se suele lanzar cuando una operación o función se aplica a un objeto de tipo inapropiado.
*   Cuando el archivo 5-main.py llama a tu función, esta lanza el error. El bloque try...except del main captura ese TypeError específico e imprime "Exception raised".  

Output:
```bash
Exception raised
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##
Write a function that raises a name exception with a message.
`6-main.py`
```python
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
 
```
`6-raise_exception_msg.py`
```python
#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)

```
*   NameError: Esta excepción normalmente ocurre cuando Python no encuentra un nombre de variable local o global.
*   `message`: Las excepciones en Python son clases. Al poner paréntesis después del nombre de la excepción (NameError(message)), estamos creando una instancia de esa clase y pasando el string como argumento.
*   En el archivo 6-main.py, verás la línea except NameError as ne:. La variable `ne` contiene la instancia de la excepción, y al hacer print(ne), Python extrae e imprime el mensaje que tú guardaste dentro.  

Output:
```bash
C is fun
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##
`-main.py`
```python

```
``
```python


```
Output:
```bash

```

touch 0-safe_print_list.py 0-main.py 1-safe_print_integer.py 1-main.py 2-safe_print_list_integers.py 2-main.py 3-safe_print_division.py 3-main.py 4-list_division.py 4-main.py 5-raise_exception.py 5-main.py 6-raise_exception_msg.py 6-main.py README.md

pycodestyle *.py
