#   General
##  Why Python programming is awesome

Python is considered "awesome" because of its readability and simplicity. It uses a clean syntax that resembles English, allowing developers to express complex concepts in fewer lines of code compared to languages like C or Java. Additionally, it has a massive standard library and a supportive community, meaning there is a "module" for almost any task you want to perform.

##  How to import functions from another file

You use the import statement. 
If you have a file named calculator.py with a function add, you can bring it into your current script like this:
```Python
from calculator import add
# Or to import everything:
import calculator
```
##  How to use imported functions

Once imported, you call them by their name (if you used from...import) or by using the module prefix:

```Python
# If you used: import calculator
result = calculator.add(5, 5)

# If you used: from calculator import add
result = add(5, 5)
```

##  How to create a module

In Python, any .py file is a module. To create one, simply save your functions, classes, or variables in a file (e.g., mymodule.py). You can then import it into any other script in the same directory.


##  How to use the built-in function dir()

The dir() function is used to find out which names (functions, variables, classes) a module defines. It returns a sorted list of strings.
```Python
import math
print(dir(math)) # Shows all functions in the math module like sin, cos, pi, etc.
```

##  How to prevent code in your script from being executed when imported

This is a crucial concept in Python. You wrap the executable part of your code in an if statement that checks the special variable __name__:
```Python
if __name__ == "__main__":
    # This code only runs if the file is executed directly
    # It will NOT run if the file is imported as a module
    my_function()
```
##  How to use command line arguments with your Python programs

To handle arguments passed via the terminal (e.g., ./script.py arg1 arg2), you need the sys module:
```Python
import sys

# sys.argv is a list containing all arguments
# sys.argv[0] is the script name
# sys.argv[1] is the first argument
print(f"First argument: {sys.argv[1]}")
```

----------------------------------------------------------------------------------------------------------------------------
#   Quiz
##  Question #0
What do these lines print?
```Python
def my_function():
    print("In my function")

my_function()
```
-   [ ]“In my function”
-   [x]In my function
-   [ ]function my_function at …
-   [ ]Nothing

##  Question #1
What do these lines print?
```Python
    print("In my function")
def my_function():
```
-   [ ]my_function
-   [ ]“In my function”
-   [ ]In my function
-   [x]function my_function at …
-   [ ]Nothing

##  Question #2
What do these lines print?
```Python
def my_function(counter):
    print("Counter: {}".format(counter))

my_function(12)
```
-   [ ]Counter: counter
-   [ ]Counter: c
-   [x]Counter: 12

##  Question #3
What do these lines print?
```Python
def my_function(counter=89):
    print("Counter: {}".format(counter))

my_function(12)
```
-   [x]Counter: 12
-   [ ]Counter: 89
-   [ ]Counter: 101

##  Question #4
What do these lines print?
```Python
def my_function(counter=89):
    print("Counter: {}".format(counter))

my_function()
```
-   [ ]Counter: 12
-   [x]Counter: 89
-   [ ]Counter: 101

##  Question #5
What do these lines print?
```Python
def my_function(counter=89):
    return counter + 1

print(my_function())
```
-   [ ]1
-   [ ]89
-   [x]90
-   [ ]891

----------------------------------------------------------------------------------------------------------------------------
#   Exercises
## 0-add.py
`add_0.py`
```Python
#!/usr/bin/python3
def add(a, b):
    return (a + b)

```
`0-add.py`
```Python
#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

```
-   if __name__ == "__main__": 
    -   Evita que el código se ejecute si alguien importa tu archivo 0-add.py desde otro lugar. 
    -   Solo se ejecuta si corres el archivo directamente con ./0-add.py
-   from add_0 import add:
    -   Usamos from...import como pide la tarea.
    -   Aquí es donde aparece la palabra add_0. Según las reglas, no puedes volver a escribirla en ninguna otra parte del código

## 1-calculation.py
`calculator_1.py `
```Python
#!/usr/bin/python3
def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return int(a / b)
```
`1-calculation.py`
```Python
#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

```

## 2-args.py
`2-args.py`
```Python
#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{:d}: {:s}".format(i, argv[i]))
```

-   import sys: Para acceder a sys.argv
-   argc = len(argv) - 1: 
    -   Restamos 1 porque no queremos contar el nombre del archivo (2-args.py) como un argumento del usuario.
-   Lógica del Plural y Puntuación
    -   Si es 0: Usamos "arguments" y terminamos con punto (.).
    -   Si es 1: Usamos "argument" (singular) y terminamos con dos puntos (:).
    -   Si es más de 1: Usamos "arguments" (plural) y terminamos con dos puntos (:).
-   El Bucle for:
    -   Usamos range(1, argc + 1) para empezar desde el índice 1 (el primer argumento real) hasta el último.
    -   Imprimimos la posición y el valor usando el formato solicitado. 
-   argv es una lista y calculamos su tamaño con len().

## 3-infinite_add.py
`3-infinite_add.py`
```Python
#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # Empezamos desde el índice 1 para saltar el nombre del archivo
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{:d}".format(total))

```
-   total = 0: Inicializamos una variable acumuladora.
-   len(sys.argv):
    -   Si no hay argumentos, len será 1 (el nombre del script). El range(1, 1) no se ejecutará y el programa imprimirá 0.
    -   Si hay argumentos, el bucle recorrerá cada uno de ellos.
-   int(sys.argv[i]): Los argumentos de la línea de comandos siempre se reciben como strings. Es obligatorio convertirlos a enteros para poder sumarlos matemáticamente.
    
-   Python 3 no tiene un límite fijo para el tamaño de un entero
-   argv: Usamos sys.argv[1:] (slicing) o el rango desde 1 para ignorar el nombre del script
##  4-hidden_discovery.py
`4-hidden_discovery.py`
```Python
#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Obtenemos la lista de todos los nombres definidos en el módulo
    names = dir(hidden_4)

    # Filtramos e imprimimos
    for name in sorted(names):
        if not name.startswith("__"):
            print("{:s}".format(name))

```
-   import hidden_4: 
    -   Aunque el archivo sea un .pyc (bytecode), Python lo importa igual que un archivo .py. La extensión no se incluye en el import.
-   dir(hidden_4): 
    -   Esta función devuelve una lista de strings con todos los atributos, variables y funciones dentro del módulo.
-   sorted(names): 
    -   El ejercicio pide orden alfabético. sorted() toma la lista y devuelve una nueva versión ordenada.
-   if not name.startswith("__"): 
    -   En Python, los nombres que empiezan con doble guion bajo (como __name__ o __doc__) se consideran "built-in" o internos.

-   ¿Qué es un .pyc?: 
    Explica que es el archivo que genera Python después de "compilar" el código fuente a bytecode para que se ejecute más rápido la próxima vez.
-   Introspección: 
    -   Menciona que dir() es una herramienta de introspección, una característica de Python que permite al programa examinarse a sí mismo en tiempo de ejecución.
-   Filtro de Dunders: 
    -   Los nombres con __ se llaman comúnmente "Dunders" (Double Underscores). 
    -   Filtrarlos es una práctica común para ver solo la API pública de un módulo.
##  5-variable_load.py
`variable_load_5.py`
```Python
#!/usr/bin/python3
a = 98
```
`5-variable_load.py`
```Python
#!/usr/bin/python3
if __name__ == "__main__":
    from variable_load_5 import a

    print("{:d}".format(a))

```
-   from variable_load_5 import a:
    -   Estamos importando únicamente la variable a.
    -   Esto es más eficiente que importar todo el módulo si solo necesitamos un dato específico.
-   if __name__ == "__main__"::
    -   Como en las tareas anteriores, esto garantiza que el print solo se ejecute cuando corras el script directamente. 
    -   Si otro archivo importa 5-variable_load.py, no se imprimirá nada.

-   print("{:d}".format(a)):
    -   Usamos el formateo de cadena para asegurar que el valor se imprima como un entero decimal, siguiendo el estándar de los ejercicios anteriores.

-   Importancia del Namespace: 
    -   Explica que al usar from variable_load_5 import a, la variable a ahora existe directamente en tu archivo actual. No necesitas escribir variable_load_5.a.
-   Modularidad: 
    -   Este ejercicio demuestra cómo los archivos de configuración o de datos (como una lista de constantes) pueden mantenerse separados de la lógica principal del programa.
