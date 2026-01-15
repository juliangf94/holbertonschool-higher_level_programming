#   General
##   How to use the Python interpreter
The interpreter is the engine that executes your code. You can use it in two ways:
-   Interactive Mode:
    -    Simply type python3 in your terminal. 
    -    You will see the >>> prompt, where you can type code and get immediate results. 
    -    To exit, type exit() or press Ctrl + D.
-   Script Mode: 
    -    You write your code in a file ending in .py (e.g., myscript.py). 
    -    You run it by typing python3 myscript.py in the terminal, or by making the file executable and running ./myscript.py.

##   How to print text and variables using print
The print() function displays information on the screen:
-   Strings: 
    -    print("Hello World")
-   Variables: 
    -    name = "Julian" -> print(name)
-   Formatted Output: 
    -    Use f-strings for efficiency:            
```Python
    age = 30
    print(f"I am {age} years old.")
```
##   How to use strings
Strings are sequences of characters wrapped in single (') or double (") quotes:
-   Concatenation: 
    -    Combining strings using +.
-   Repetition:     
    -    Using * (e.g., "Holberton" * 3).
-   Immutability: 
    -    Once a string is created, its characters cannot be changed individually.

##   What are indexing and slicing in Python
-   Indexing: 
    -    Accessing a single character by its position. Indices start at 0.
```Python
    word = "Python"
    # word[0] is 'P', word[-1] is 'n' (last character)
```
-   Slicing: 
        Extracting a part of a string using the syntax [start:stop:step].
```Python
        word = "Python"
            # word[1:4] = 'yth'
            # word[0:2] = 'Py' (from index 0 up to, but NOT including, index 2)
            # word[2:] = ''
            # word[:4] = 'Pyth'
            # word[::2] = 'Pto'            
            # word[1::2] = 'yhn'
            # word[::-1] = 'nohtyP' (invierte la palabra completa)
        Indices negativos:
            # word[-3:] = 'hon'
            # word[:-2] = 'Pyth'
            # word[-4:-1] = 'tho' (Empieza en el t y llega hasta antes de n (-1))
        Casos "Extrños":
        # word[5:2] = '' (vacio) Si el inicio es mayor que el final y el paso es positivo no devuelve nada
        # word[0:100] = 'Python'
```
##   What is the official Python coding style and how to check your code with pycodestyle
-   Official Style: 
    -    It is called PEP 8 (Python Enhancement Proposal 8). 
    -    It provides guidelines for naming conventions (like using snake_case for variables), 
    indentation (4 spaces), and white space.
-   Checking with pycodestyle: 
    -    It is a tool that automatically checks your code for style violations. 
    -    To check a file, run:
```Python
    pycodestyle filename.py
```
---------------------------------------------------------------------------------------------------------------------
##   Question #0
What does this command line print?

```Python
print("Holberton school")
```

-   [ ]Holberton
-   [ ]“Holberton school”
-   [x]`Holberton school`
-   [ ]‘Holberton school’

##   Question #1
What does this command line print?

```Python
print(f"{98} Battery street")
```

-   [x]`98 Battery street`
-   [ ]f"98 Battery street"
-   [ ]9 Battery street
-   [ ]8 Battery street

##  Question #2
What does this command line print?

```Python
print(f"{98} Battery street, {'San Francisco'}")
```

-   [ ]“98 Battery street, San Francisco”
-   [ ]8 Battery street, San
-   [x]`98 Battery street, San Francisco`
-   [ ]San Francisco Battery street, 98

##  Question #3
What does this command line print?

```Python
a = "Python is cool"
print(a[4])
```

-   [ ]P
-   [ ]n
-   [x]`o`
-   [ ]h

##  Question #4
What does this command line print?

```Python
a = "Python is cool"
print(a[0:6])
```

-   [x]`Python`
-   [ ]Pytho
-   [ ]Python is
-   [ ]Python is cool

##  Question #5
What does this command line print?

```Python
a = "Python is cool"
print(a[:6])
```

-   [ ]Pytho
-   [x]`Python`
-   [ ]Python is
-   [ ]is cool

##  Question #6
What does this command line print?

```Python
a = "Python is cool"
print(a[7:])
```

-   [ ]Python is
-   [ ]Python i
-   [ ]cool
-   [x]`is cool`

##  Question #7
What does this command line print?

```Python
a = "Python is cool"
print(a[7:-5])
```

-   [ ]on
-   [ ]nohtyP
-   [ ]Python
-   [ ]si
-   [x]`is`

##  Question #8
What does this command line print?

```Python
a = "Python is cool"
print(a[-2])
```

-   [ ]ol
-   [ ]l
-   [x]`o`
-   [ ]Nothing
---------------------------------------------------------------------------------------------------------------------
# Exercises
## 2-print.py
`2-print.py`
```Python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

Output: 

```bash
"Programming is like building a multilingual puzzle
```
pycodestyle 2-print.py

## 3-print_number.py
`3-print_number.py`
```Python
#!/usr/bin/python3
number = 98
print(f"{number:d} Battery street")
```

Output: 

```bash
98 Battery street
```
-    :d : Indica a Python que debe tratar la variable como un entero decimal.

pycodestyle 3-print_number.py

## 4-print_float.py
`4-print_float.py` 
```Python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

Output: 

```bash
Float: 3.14
```
-    . indica que vamos a configurar la precisión decimal.
-    2 especifica que queremos exactamente dos dígitos después del punto.
-    f le indica a Python que trate el número como un float (punto flotante).


pycodestyle 4-print_float.py

## 5-print_string.py
`5-print_string.py`
```Python
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
```

Output: 

```bash
Holberton SchoolHolberton SchoolHolberton School
Holberton
```
pycodestyle 5-print_string.py

## 6-concat.py
`6-concat.py`
```Python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = f"Welcome to {str1} {str2}!"
print(str1)
```

Output: 

```bash 
Welcome to Holberton School!
```
pycodestyle 6-concat.py 

## 7-edges.py
`7-edges.py`
```Python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

Output: 

```bash
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```
pycodestyle 7-edges.py

## 8-concat_edges.py

`8-concat_edges.py`
```Python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```

Output: 

```bash
object-oriented programming with Python
```
pycodestyle 8-concat_edges.py

## 9-easter_egg.py
Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.
`9-easter_egg.py`
```Python
#!/usr/bin/python3
import this
```

Output: 

```bash
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
...
```
pycodestyle 9-easter_egg.py
