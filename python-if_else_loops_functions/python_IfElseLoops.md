#   General
##  Why indentation is so important in Python

In Python, indentation is not just for readability; it is part of the syntax.  
It defines the grouping of statements (blocks of code).  
While C uses curly braces {}, Python uses a consistent level

##  How to use the if, if ... else statements

if, if ... else:   
Used for conditional branching.

```Python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```
##  How to use comments

Use the hash symbol `#` for single-line comments.  
For multi-line documentation, use triple quotes `"""Docstring"""`.

##  How to affect values to variables

You use the assignment operator = .  
For example, x = 5 .  
Python is dynamically typed, so you don't need to declare the data type.

##  How to use the while and for loops

while repeats as long as a condition is True.  
for iterates over a sequence (like a list or a range).

##  How to use the break and continues statements

break: Exits the loop entirely.

continue: Skips the rest of the current iteration and moves to the next one.

##  How to use else clauses on loops

A unique Python feature.  
The else block executes only if the loop finished normally (i.e., it did NOT hit a break).

##  What does the pass statement do, and when to use it

A null operation.  
It is used as a placeholder when a statement is syntactically required but you don’t want to execute any code yet.

##  How to use range

A function that generates a sequence of numbers.
```Python
range(start, stop, step).
```    
Remember: the stop value is never included.

##  What is a function and how do you use functions

A reusable block of code defined with the def keyword.

##  What does return a function that does not use any return statement

If a function does not have a return statement, it automatically returns None.

##  Scope of variables

Local: Variables defined inside a function (only accessible there).

Global: Variables defined outside functions (accessible throughout the file).

##  What’s a traceback

An error report that shows the "path" of the execution that led to a crash, including file names and line numbers.

##  What are the arithmetic operators and how to use them


+, -, *, / (Standard)

// (Floor division: returns the integer, discards decimals)

% (Modulo: returns the remainder)

** (Exponentiation: power)

----------------------------------------------------------------------------------------------------------------------------
#   Quiz
##  Question #0
What do these lines print?
```Python
if True:
    print("Holberton")
else:
    print("School")
```
-   [x]Holberton
-   [ ]School

##  Question #1
What do these lines print?
```Python
if 12 == 48/4:
    print("Holberton")
else:
    print("School")
```
-   [x]Holberton
-   [ ]School

##  Question #2
What do these lines print?
```Python
if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")
```
-   [ ]Holberton
-   [x]School

##  Question #3
What do these lines print?
```Python
if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")
```
-   [x]Holberton
-   [ ]School

##   Question #4
What do these lines print?
```Python
a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")
```
-   [x]Holberton
-   [ ]C is fun
-   [ ]School

##  Question #5
What do these lines print?
```Python
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")
```
-   [ ]Holberton
-   [x]C is fun
-   [ ]School

##  Question #6
What do these lines print?
```Python
for i in range(4):
    print(i, end=" ")
```
-   [ ]1 2 3 4
-   [ ]1 2 3
-   [x]0 1 2 3
-   [ ]0 1 2 3 4

##  Question #7
What do these lines print?
```Python
for i in range(2, 4):
    print(i, end=" ")
```
-   [ ]2 4
-   [x]2 3
-   [ ]2 3 4
-   [ ]3 4

##  Question #8
What do these lines print?
```Python
for i in range(2, 10, 2):
    print(i, end=" ")
```
-   [ ]2 3 4 5 6 7 8 9 10
-   [ ]2 3 4 5 6 7 8 9
-   [ ]4 6 8 10 12 14 16 18
-   [x]2 4 6 8

----------------------------------------------------------------------------------------------------------------------------
#   Exercises
Todos los archivos ejecutables: chmod +x *.py
##  0-positive_or_negative.py

```python
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
```

pycodestyle 0-positive_or_negative.py 

##  1-last_digit.py

```python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

print(f"Last digit of {number:d} is {last_digit:d}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

```
-   printf():
    -   Añáde automaticamente un salto de linea (\n) al final.
-   end=" " : 
    -   Le dice a Python: "No saltes de línea, termina con un espacio y quédate ahí"
```Bash
pycodestyle 1-last_digit.py
```
##  2-print_alphabet.py

```python
#!/usr/bin/python3
for i in range(97, 123):
    print("{:s}".format(chr(i)), end="")

```
-   Usamos range(97, 123) para representar las letras del abecedario.  
    Usamos 123 como limite superior ya que el valor final de un range es exclusivo
-   "{:s}".format(...):
    -   Usamos formato string.
-   chr(i):
    -   Esta funcion toma el numero y lo transforma en letra.
-   end="":
    -   print añade un salto de linea. Con esto le decimos que no añada nada.
```Bash
pycodestyle 2-print_alphabet.py
```
##  3-print_alphabt.py

```python
#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{:s}".format(chr(i)), end="")

```
```Bash
pycodestyle 3-print_alphabt.py
```
##  4-print_hexa.py

```python
#!/usr/bin/python3
for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i))

```
```Bash
pycodestyle 4-print_hexa.py
```
##  5-print_comb2.py

```python
#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))

```
```Bash
pycodestyle 5-print_comb2.py
```
##  6-print_comb3.py

```python
#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{:d}{:d}".format(digit1, digit2))
        else:
            print("{:d}{:d}".format(digit1, digit2), end=", ")

```
```Bash
pycodestyle 6-print_comb3.py
```
##  7-islower.py
`7-main.py`
```python
#!/usr/bin/python3
# Importamos la función desde tu archivo
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
```
`7-islower.py`
```python
#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

```
-   ord(c): 
    -   Convierte una letra en su codigo decimal ASCII.
```Bash
pycodestyle 7-islower.py
```
##  8-uppercase.py

```python
#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

```
```Bash
pycodestyle 8-uppercase.py
```
##  9-print_last_digit.py

`9-main.py`
```python
#!/usr/bin/python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

```
`9-print_last_digit.py`
```python
#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit

```
-   abs(): 
    -   Devuelve el valor absoluto
```Bash
pycodestyle 9-print_last_digit.py
```
##  10-add.py
`10-main.py`
```python
#!/usr/bin/python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
```
`10-add.py`
```python
#!/usr/bin/python3
def add(a, b):
    return (a + b)
```
```Bash
pycodestyle 10-add.py
```
##  11-pow.py
`11-main.py`
```python
#!/usr/bin/python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
```
`11-pow.py`
```python
#!/usr/bin/python3
def pow(a, b):
    return (a ** b)

```
```Bash
pycodestyle 11-pow.py
```
##  12-fizzbuzz.py
`12-main.py`
```python
#!/usr/bin/python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

```
`12-fizzbuzz.py`
```python
#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")

```
-   El comando cat -e sirve para "hacer visibles los caracteres invisibles".
-   El $ representa un salto de línea (\n).
```Bash
pycodestyle 12-fizzbuzz.py
```

##  100-print_tebahpla.py
`100-print_tebahpla.py`
```Python
#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(i if i % 2 == 0 else i - 32), end="")

```
Output:
```Bash
zYxWvUtSrQpOnMlKjIhGfEdCbAjuliangf94@DESKTOP-3UBL8O2:~
```
-   {:c}:
    -   Es el formateador que convierte un número entero en su carácter ASCII correspondiente.
-   Expresión condicional (i if i % 2 == 0 else i - 32):
    -   Evalúa si el índice es par o impar dentro del mismo print para decidir si resta 32 (convertir a mayúscula) o no.
-   range(122, 96, -1):
    -   Comienza en 122 ('z') y termina justo antes del 96 (en el 97, que es 'a'), restando uno en cada paso.

```Bash
pycodestyle 100-print_tebahpla.py
```

## 101-remove_char_at.py
`101-main.py`
```Python
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
```
`101-remove_char_at.py`
```Python
#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        return (str[:n] + str[n + 1:])
    return (str)

```
Output:
```Bash
Bes School
Chcago
 is fun!
School
Python
```
### Explicación:
-   Validación del índice (if n >= 0):
    -   El ejercicio pide tratar el índice como en C. Si n es negativo, el comportamiento esperado según el ejemplo de 101-main.py es devolver la cadena original sin cambios.
-   Slicing (str[:n]):
    -   Obtiene la parte de la cadena desde el inicio hasta justo antes de la posición n.
-   Slicing (str[n + 1:]):
    -   Obtiene la parte de la cadena desde la posición inmediatamente posterior a n hasta el final.
-   Concatenación (+):
    -   Une ambas partes, dejando fuera efectivamente el carácter que estaba en la posición n.

```Bash
pycodestyle 101-remove_char_at.py
```
