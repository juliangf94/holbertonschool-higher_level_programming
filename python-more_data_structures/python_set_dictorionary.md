# Python: Sets, Dictionaries, and Functional Programming
## General
### Why Python programming is awesome
Python is considered one of the most powerful and popular languages because:
* **Readability:** Its syntax is clear and resembles the English language, making code easy to read and maintain.
* **Productivity:** You can write complex programs in fewer lines of code compared to languages like C or Java.
* **Versatility:** It is used in data science, web development, automation, AI, and more.
* **Vast Ecosystem:** It has a massive standard library and a global community developing packages for almost any need.

---

## Sets
### What are sets and how to use them
A **set** is an unordered collection of **unique** elements. 
* They do not allow duplicate values.
* They are defined using curly braces `{}` or the `set()` function.
* They are highly efficient for removing duplicates from other collections and performing mathematical set operations.

```python
# Usage example
my_set = {1, 2, 3, 3, 4} # The duplicate 3 is automatically removed
print(my_set) # Output: {1, 2, 3, 4}
```

###  What are the most common methods of set and how to use them
*   `add(value)`: Adds an element to the set.
*   `remove(value)`: Removes an element; raises a `KeyError` if it doesn't exist.
*   `discard(value)`: Removes an element; does NOT raise an error if it doesn't exist.
*   `union(other_set)` or |: Combines elements from both sets.
*   `intersection(other_set)` or `&`: Returns only elements common to both sets.
*   `difference(other_set)` or `-`: Returns elements in the first set but not the second.

### When to use Sets versus Lists
Use Sets if: You need to ensure elements are unique and order doesn't matter. They are extremely fast for membership testing (`x in set`).

Use Lists if: Order is important, you need to access elements by index, or you allow duplicate values.

### How to iterate over a Set
You can loop through a set using a `for` loop, but remember the order is unpredictable:

```Python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```
##  Dictionaries
### What are dictionaries and how to use them
A `dictionary` is a collection of `key-value` pairs. They are defined with curly braces `{}` and each pair is separated by a colon `:`. Think of it like a real-life dictionary where you look up a "word" (key) to find its "definition" (value).

```Python
user = {"name": "Julian", "age": 30}
print(user["name"]) # Accessing via the key "name" returns "Julian"
```
### When to use Dictionaries versus Lists or Sets
*   Dictionaries: Use when you need to associate labels (keys) with specific data for fast retrieval (e.g., database records or user profiles).
*   Lists/Sets: Use when you only need a simple sequence of values without an associated label for each individual item.

### What is a key in a dictionary
A `key` is the unique identifier that points to a specific value within the dictionary. It must be of an `immutable` type (like strings, numbers, or tuples). This immutability allows Python to find the value instantly regardless of the dictionary size.

### How to iterate over a dictionary
*   Iterate by Keys: for key in my_dict:
*   Iterate by Values: for val in my_dict.values():
*   Iterate by both (Items): for key, val in my_dict.items():

##  Functional Programming
### What is a lambda function
A lambda function is a small, anonymous function defined in a single line using the `lambda` keyword. Its structure is: `lambda arguments: expression`. It is often used for short-lived tasks where a full function definition isn't necessary.

```Python
square = lambda x: x * x
print(square(5)) # Output: 25
```
### What are the map, reduce and filter functions
These are higher-order functions used to transform and process collections efficiently:

1)  Map: Applies a function to every item in an iterable.
*   map(lambda x: x * 2, [1, 2, 3]) -> Result: [2, 4, 6]

2)  Filter: Creates a new list containing only elements that meet a specific condition.
*   filter(lambda x: x > 5, [2, 7, 3, 8]) -> Result: [7, 8]

3)  Reduce: (Requires from functools import reduce) Applies a function cumulatively to items, reducing the entire list to a single value.
*   reduce(lambda x, y: x + y, [1, 2, 3, 4]) -> Result: 10 (the sum)



-------------------------------------------------------------
#   Quiz
##  Question #0
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a['id']

*   [ ]id
*   [ ]‘id’
*   [ ]a[‘id’]
*   [x]89
*   [ ]John

##  Question #1
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')

*   [ ]id
*   [ ]‘id’
*   [ ]a[‘id’]
*   [x]89
*   [ ]John

##   Question #2
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')

*   [ ]‘age’
*   [ ]Not found
*   [ ]89
*   [ ]12
*   [x]Nothing

##   Question #3
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)

*   [ ]‘age’
*   [ ]Nothing
*   [x]0
*   [ ]89

##  Question #4
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')

*   [ ]‘projects’
*   [x][1, 2, 3, 4]
*   [ ][1]
*   [ ]list
*   [ ]Nothing

##  Question #5
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]

*   [x]4
*   [ ][4]
*   [ ][1, 2, 3, 4]
*   [ ]3
*   [ ][3]

##  Question #6
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")

*   [ ]89
*   [ ][ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]
*   [x]Amy
*   [ ]Bob
*   [ ]Nothing

##  Question #7
What do these lines print?

>>> for i in range(0, 3):
>>>     print(i, end=" ")

*   [ ]1 2 3
*   [ ]0 1 2 3
*   [x]0 1 2

##  Question #8
What do these lines print?

>>> for i in range(1, 4):
>>>     print(i, end=" ")

*   [x]1 2 3
*   [ ]0 1 2 3
*   [ ]1 2 3 4

##  Question #9
What do these lines print?

>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")

*   [ ]0 1 2 3
*   [ ]0 1 2 3 5
*   [ ]1 2 3
*   [x]1 2 3 4

##  Question #10
What do these lines print?

>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")

*   [ ]0 1 2 3
*   [ ]1 2 3 4
*   [x]1 3 4 2
*   [ ]1 3 4 2 0

##  Question #11
What do these lines print?

>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")

*   [ ]0 1 2 3
*   [ ]1 2 3 4
*   [x]Hello Holberton School 98

-------------------------------------------------------------
#   Exercises
##  0-square_matrix_simple.py
Write a function that computes the square value of all integers of a matrix.
`0-main.py`
```python
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

```
`0-square_matrix_simple.py`
```python
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

```
*   map(lambda x: x**2, row)
    -   row: Es una de las sub-listas (por ejemplo, [1, 2, 3]).
    -   lambda x: x**2: Es una función anónima que toma un número y lo eleva al cuadrado.
    -   map(...): Aplica esa función a cada número de esa fila.
    -   Resultado interno: Genera algo similar a [1, 4, 9].
*   list(...)
    -   El comando `map` en Python 3 devuelve un "objeto map" (un iterador), no una lista. Para que el resultado final sea una matriz real, envolvemos el map interno en `list()`.
*   map(lambda row: ..., matrix)
    -   Aquí, el `map` externo toma la matriz completa.
    -   Para cada `row` (fila) dentro de la matriz, ejecuta la lógica que explicamos en el punto 1.
    -   Esto asegura que procesamos la fila 1, luego la fila 2, y así sucesivamente.
*   list(...)
    -   Finalmente, convertimos el resultado del map externo en una lista. Esto nos devuelve la estructura de "lista de listas" que necesitamos.

```python
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]

```
Output:
```bash
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  1-search_replace.py
Write a function that replaces all occurrences of an element by another in a new list.
`1-main.py`
```python
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
```
`1-search_replace.py`
```python
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map (lambda x: replace if x == search else x, my_list))

```

o
```python
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]

```
Output:
```bash
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  2-uniq_add.py
Write a function that adds all unique integers in a list (only once for each integer).
`2-main.py`
```python
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

```
`2-uniq_add.py`
```python
#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(set(my_list))

```
*   `set(my_list)`: 
    -   Si le pasamos la lista `[1, 2, 3, 1, 4, 2, 5]`, el set resultante será `{1, 2, 3, 4, 5}`. Los números 1 y 2 que estaban repetidos desaparecen.
*   `sum(...)`:
    -   Esta es una función integrada de Python que toma un iterable (como nuestro nuevo set) y suma todos sus elementos.
Output:
```bash
Result: 15
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  3-common_elements.py
Write a function that returns a set of common elements in two sets.
`3-main.py`
```python
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

```
`3-common_elements.py`
```python
#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set_1 & set_2

```
*   Los `elementos comunes` son aquellos valores que se encuentran presentes en dos o más colecciones al mismo tiempo.
*   Cuando trabajas con `set` puedes usar:
    -   `&`: `set_1 & set_2` devuelve un nuevo conjunto con los elementos que existen en ambos
    -   `.intersection()`: Podrias escribilo como `return set_1.intersection(set_2)`
*   Los Sets utilizan una estructura llamada `Hash Table`, lo que permite que Python encuentre los elementos comunes de forma casi instantánea, incluso si los conjuntos tuvieran millones de elementos.
  

Output:
```bash
['C']
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  4-only_diff_elements.py
`4-main.py`
```python
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

```
`4-only_diff_elements.py`
```python
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2

```
*   El operador '^' realiza la diferencia simétrica

Output:
```bash
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  5-number_keys.py
Write a function that returns the number of keys in a dictionary.
`5-main.py`
```python
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
```
`5-number_keys.py`
```python
#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(a_dictionary)

```
Output:
```bash
Number of keys: 3
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  6-print_sorted_dictionary.py
Write a function that prints a dictionary by ordered keys.
`6-main.py`
```python
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

```
`6-print_sorted_dictionary.py`
```python
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary.get(key)))

```
*   `a_dictionary.keys()`: 
    -   Extrae una vista de todas las llaves del diccionario.
*   `sorted(...)`:
    -   Toma las llaves y crea una nueva lista con ellas ordenadas alfabéticamente (por valor ASCII, lo que significa que las mayúsculas como "Number" irán antes que las minúsculas como "ids").
*   `a_dictionary.get(key)`:
    -   Usamos el método .get() para recuperar el valor de cada llave mientras recorremos la lista ordenada.

Output:
```bash
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 7-update_dictionary.py 
Write a function that replaces or adds key/value in a dictionary.
`7-main.py`
```python
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

```
`7-update_dictionary.py`
```python
#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

```
*   `a_dictionary[key] = value`: 
    -   Usamos este metodo para reemplazar valores en el diccionario.      
Output:
```bash
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 8-simple_delete.py
Write a function that deletes a key in a dictionary.
`8-main.py`
```python
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

```
`8-simple_delete.py`
```python
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

```
Output:
```bash
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 9-multiply_by_2.py
Write a function that returns a new dictionary with all values multiplied by 2
`9-main.py`
```python
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

```
`9-multiply_by_2.py`
Option 1:
```python
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}

```
*   `a_dictionary.items()`: 
    -   Este método nos devuelve una lista de tuplas con la forma `(llave, valor)`
*   `{key: value * 2 ...}`:
    -   `key`: Mantenemos la llave original sin cambios.
    -   `value * 2`: Aplicamos la operación matemática al valor.
*   `return {}`: Python reserva un nuevo espacio de memoria.
Option 2:
```python
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {} # Creamos un diccionario vacío para no dañar el original
    for key in a_dictionary:
        value = a_dictionary[key]
        new_dict[key] = value * 2 # Guardamos el doble en el nuevo
    return new_dict

```
Output:
```bash
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 10-best_score.py
Write a function that returns a key with the biggest integer value.
`10-main.py`
```python
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

```
`10-best_score.py`
```python
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

```
*   `max(a_dictionary, key=a_dictionary.get)`:
    -   `max() ` por defecto compara las llaves alfabeticamente pero al usar `key=a_dictionary.get` compara el valor obtenido con `.get()`
Output:
```bash
Best score: Molly
Best score: None
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 11-multiply_list_map.py
Write a function that returns a list with all values multiplied by a number without using any loops.
`11-main.py`
```python
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

```
`11-multiply_list_map.py`
```python
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

```
Output:
```bash
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 12-roman_to_int.py
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
`12-main.py`
```python
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
```
`12-roman_to_int.py`
```python
#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }    
    total = 0
    length = len(roman_string)

    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)
        if i + 1 < length:
            next_val = roman_dict.get(roman_string[i + 1], 0)
            
            if current_val < next_val:
                total -= current_val 
            else:
                total += current_val
        else:
            total += current_val
    return total

```
*   `isinstance(roman_string, str)`: 
    -   Verificamos el tipo de dato para evitar errores si nos pasan un número o un objeto vacío.
*   `current_val = roman_dict.get(roman_string[i], 0)`
    -   Traduce la letra romana que estamos procesando.
    -   `roman_string[i]`: Accedemos a la letra que está en la posición i del texto. Si el texto es "XIV" y estamos en la primera vuelta (i = 0), esto devuelve `X`.
    -   `roman_dict.get(..., 0)`:
        +   Buscamos esa letra en nuestro diccionario. Si es 'X', el diccionario nos devuelve su valor: 10.
        +   El `0` al final es una medida de seguridad. Si por error el string tiene un carácter inválido (ej: "X1V"), en lugar de que el programa falle con un error, el método .get nos devolverá un 0.
*   `if i + 1 < length`: Asegurarse de que no es la ultima letra 
*   `next_val = roman_dict.get(roman_string[i + 1], 0)` :
    +   Traduce la siguiente letra romana a la que estamos procesando.
*   `if current_val < next_val:`:
    -   Confirmamos que no estamos en la ultima letra
*   `total -= current_val`:
    -   Si ves una I (1) antes de una X (10), significa que es un 9. Entonces, en lugar de sumar el 1, lo restamos del total.
*   `total += current_val` : Si la letra actual es mayor o igual a la que sigue (por ejemplo, VI, donde 5 es mayor que 1), simplemente la sumamos al total acumulado.


Output:
```bash
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```

touch 0-square_matrix_simple.py 0-main.py 1-search_replace.py 1-main.py 2-uniq_add.py 2-main.py 3-common_elements.py 3-main.py 4-only_diff_elements.py 4-main.py 5-number_keys.py 5-main.py 6-print_sorted_dictionary.py 6-main.py 7-update_dictionary.py 7-main.py 8-simple_delete.py 8-main.py 9-multiply_by_2.py 9-main.py 10-best_score.py 10-main.py 11-multiply_list_map.py 11-main.py 12-roman_to_int.py 12-main.py README.md
