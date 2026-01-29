# Object-Oriented Programming (OOP) in Python
## What is OOP
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which bundle data (attributes) and behavior (methods) together. 
OOP helps organize code, improve reusability, and model real-world entities.

---

## “First-class everything”
In Python, “first-class everything” means that all entities (functions, classes, objects, variables) are treated as first-class citizens.  
They can be assigned to variables, passed as arguments, returned from functions, and stored in data structures.

---

## What is a class
A class is a blueprint for creating objects.  
It defines the attributes and methods that the objects created from it will have.
```python
class Person:
    pass # An empty block
p = Person()
print(p)
```
Output:
```bash
$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>
```

---

## What is an object and an instance
-   Object: 
    +   A concrete realization of a class.
    +   They can store data using ordinary variables that belong to the object.
    +   Variables that belong to an object or class are referred to as `fields`:
        *   Instance variables: They can belong to each instance/object of the class.
        *   Class variables: They can belong to the class itself.
    +   Objects can also have functionality by using functions (`methods`) that belong to a class.   
    +   Fields and methods can be refferred to as the `attributes` of that class.
-   Instance: 
    +   A specific object created from a class.
    +   
In practice, both terms are often used interchangeably.

---

## Difference between a class and an object or instance
-   Class:
    +   Is created using the `class` keyword.
    +   The fields and methods of the class are listed in an indented block.
    +   Defines structure and behavior.
    +   `Class variables`:
        *   They are shared, can be accessed by all instances of that class.
        *   There is only one copy of the class variable.
        *   When any one object makes a change to a class variable, that change will be seen by all the other instances.   
-   Object (or instance): 
    +   Is a specific realization of that structure in memory.
    +   `Object variabñes`:
        *   Are owned by each invidivual object/instance of the class.
        *   Each object has its own copy of the field.
```python
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```
Output:
```bash
$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.
```
-   You can see the use of docstrings for classes as well as methods. 
    We can access the class docstring at runtime using Robot.__doc__ and the method docstring as Robot.say_hi.__doc__


---

## What is an attribute
An attribute is a variable associated with a class or an object.  
It stores data that belongs to the object or class.

---

## Public, protected, and private attributes
* **Public attributes**: accessible from anywhere
  Example: `self.name`

* **Protected attributes**: intended for internal use (convention only)
  Example: `self._name`

* **Private attributes**: name-mangled to avoid accidental access
  Example: `self.__name`

Python enforces these by convention, not by strict access control.

---

## What is `self`
`self` is a reference to the current instance of the class. 
-   It is used to access instance attributes and methods inside the class.
-   A parameter thath you must add to the beginning of the list and don´t give a value to it.  
-   It will refer to the object itself.
---

## What is a method
A method is a function defined inside a class that operates on an instance or the class itself.
```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
```
Output:
```bash
$ python oop_method.py
Hello, how are you?
```

---

## What is the special `__init__` method
`__init__` is a special method called automatically when a new object is created.  
It is used to `initialize` instance attributes.
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
```
Output:
```bash
$ python oop_init.py
Hello, my name is Swaroop
```
-   The `self.name` means that there is something called "name" that is part of the object called "self".
-   The `name` is a local variable.


---

## Data Abstraction, Encapsulation, and Information Hiding
-   **Data Abstraction**: 
    +   The process of hiding the complex implementation details of a system and showing only the necessary features (functionality) to the user. 
    +   It focuses on what an object does rather than how it does it.
    +   Exposing only what the user needs to know
-   **Encapsulation**: 
    +   The bundling of data (attributes) and the methods (functions) that operate on that data into a single unit or class. 
    +   It keeps the data safe from external interference.
    +   bundling data and methods together, the methods are:
        *   `Getter`: For retrieving the data.
        *   `Setter`: For changing the data.
-   **Information Hiding**: 
    +   A subset of encapsulation where the internal representation of an object is hidden from the outside. 
    +   In Python, this is achieved by using a double underscore prefix (e.g., __size) to make attributes private.
    +   Restricting direct access to internal data

These principles help reduce complexity and increase maintainability.

---

## What is a property
A property is a managed attribute that uses methods to control access to an attribute, while allowing attribute-like syntax.
### Example 1:
```python
class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
```
-   If the function had been called "f", we would have to decorate it with "@f.setter". 
-   Two things are noteworthy: 
    +   We just put the code line "self.x = x" in the __init__ method.
    +   The property method x is used to check the limits of the values. 
-   The second interesting thing is that we wrote "two" methods with the same name and a different number of parameters "def x(self)" and "def x(self,x)". 
### Example 2
```python
class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 
  
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
```
Output:
```bash
Seems to be okay!
I feel bad!
```


## Difference between an attribute and a property
An attribute stores data directly.
A property controls access to data using getter, setter, and deleter methods.

---

## Pythonic way to write getters and setters
The Pythonic way is to use the `@property` decorator instead of explicit `get_` and `set_` methods.  
We avoid writing get_size() or set_size().  
Instead, we use the property decorator.  
This allows you to enforce data validation when a value is assigned.
### Example 1:
```python
class Square:
    def __init__(self, size=0):
        self.size = size  # This calls the setter!

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```
```bash
```
---
---

## Dynamically creating new attributes
Python allows adding attributes to an instance at runtime using assignment:

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attr = "I am dynamic!" # Adding an attribute on the fly
```

---

## Binding attributes to objects and classes

* Instance attributes belong to individual objects
* Class attributes belong to the class and are shared by all instances

---

## What is `__dict__`

`__dict__` is a dictionary that stores an object’s or class’s attributes and their values.
-   An instance __dict__ contains attributes specific to that object.

-   A class __dict__ contains the methods and class-level attributes.   


---

## How Python finds attributes
Python looks for attributes in the following order:

1. Instance namespace
2. Class namespace
3. Parent classes (Method Resolution Order)

---

## How to use `getattr`
The `getattr(object, name[, default])` function allows you to access an attribute using a string name rather than a dot operator.
```python
# Equivalent to: value = obj.size
value = getattr(obj, "size")

# Safely get attribute with a default if it doesn't exist
status = getattr(obj, "missing_attr", "Not Found")
```
---
---

#   Quiz

##  Question #0
In this following code, what is User?
```Python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```            
-   [x] A class
-   [ ] A string
-   [ ] An attribute
-   [ ] A method
-   [ ] An instance

##  Question #1
In this following code, what is id?

```Python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
-   [ ] A public instance attribute
-   [x] A public class attribute
-   [ ] A public class method
-   [ ] A public instance method
-   [ ] A private class attribute
-   [ ] A protected class attribute

##  Question #2
In this following code, what is __password?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
-   [ ] A public class attribute
-   [ ] A public instance attribute
-   [ ] A protected class attribute
-   [ ] A protected instance attribute
-   [x] A private class attribute
-   [ ] A private instance attribute

Note: Because it is defined directly in the class body and has double underscores, it is a private class attribute.

##  Question #3
In this following code, what is is_new?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
-   [ ] A public class attribute
-   [x] A public instance attribute
-   [ ] A protected class attribute
-   [ ] A protected instance attribute
-   [ ] A private class attribute
-   [ ] A private instance attribute

##  Question #4
What do these lines print?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
u = User()
u.is_new
```
-   [ ] is_new
-   [ ] Nothing
-   [ ] False
-   [x] True

##  Question #5
What do these lines print?

```python
class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
u.id
```
-   [x] 89
-   [ ] id
-   [ ] User.id
-   [ ] Nothing

##  Question #6
What do these lines print?

```python
class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User("John")
u.name
```
-   [ ] name
-   [ ] None
-   [x] John
-   [ ] no name

##  Question #7
What do these lines print?

```python
class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
u.name
```
-   [ ] name
-   [ ] None
-   [ ] John
-   [x] no name


---
---

#   Exercises
## 0-square.py
`0-main.py`
```python
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

```
`0-square.py`
```python
#!/usr/bin/python3
"""
This module provides the class Square
"""


class Square:
    """
    An empty class that defines a square

    This class has no attributes ot methods.
    """
    pass

```
Output:
```bash

{}
```


---

##  1-square.py
Write a class Square that defines a square by: (based on 0-square.py)
`1-main.py`
```python
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

```
`1-square.py`
```python
#!/usr/bin/python3
"""
This module defines a square class.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size length of the square (private)
    """
    def __init__(self, size):
        """
        Initialize the square with a specific size

        Args:
            size: The size of the square´s side.
        """
        self.__size = size
```
Output:
```bash
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```


---

##  2-square.py
`2-main.py`
```python
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
```
`2-square.py`
```python
#!/usr/bin/python3
"""
This module defines a square class with size validation
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance

        Args:
            size(int): The side lenfth of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

```
Output:
```bash

{'_Square__size': 3}

{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```


---

##  3-square.py
`3-main.py`
```python
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

```
`3-square.py`
```python
#!/usr/bin/python3
"""
This module defines a square class that calculate its area
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

```
Output:
```bash
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```


---

##  4-square.py
`4-main.py`
```python
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

```
`4-square.py`
```python
#!/usr/bin/python3
"""
This module defines a square class with property getter and setter
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
        """
        self.__size = size
    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side of the length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size if the square with validation.

        Args:
            value (int): The new side length.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

```
Output:
```bash
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
```
---

##  5-square.py
`5-main.py`
```python
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

```
`5-square.py`
```python
#!/usr/bin/python3
"""
This module defines a square class with printing capabilities.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side of the length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size if the square with validation.

        Args:
            value (int): The new side length.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)

```
Output:
```bash
###
###
###
--
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
--

--
```


---

##  6-square.py
`6-main.py`
```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

```
`6-square.py`
```python
#!/usr/bin/python3
"""
This module defines a Square class with size and position properties.
"""


class Square:
    """
    A class used to represent a square

    Attributes:
        __size(int): The size lenth of the square (private)
        __position (tuple): The (x, y) coordinates of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side of the length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size if the square with validation.

        Args:
            value (int): The new side length.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with specific validation for a tuple
        of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print("")
            return
        #   Print vertical offset (y coordinate)
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        #   Print each row with horizontal offset (x coordinate)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

```
-   Constructor (`__init__`):
    +   Se ejecuta automáticamente cuando creas un objeto (ej. my_square = Square(3, (1, 1))).
    +   Al escribir self.size = size obligamos a python a pasar por el setter, asegurando que el tamaño se valide incluso desde el primer segundo de vida del objeto.
```python
def __init__(self, size=0, position=(0, 0)):
    self.size = size
    self.position = position
```
-   Encapsulación y Propiedades (`size`):
    +   `@property` (Getter): Permite leer el valor (print(my_square.size)) sin acceder directamente a la variable "secreta" __size.
    +   `@size.setter` (Setter): Es el "filtro de seguridad". Si alguien intenta poner un tamaño de -5 o un texto, el programa se detiene y lanza un error claro. Esto evita que tu objeto tenga datos absurdos.
```python
@property
def size(self):
    return self.__size

@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value
```
-   La lógica de la Posición (`position`)
    +   Aquí verificas 4 cosas en una sola condición:
        1)   ¿Es una tupla?
        2)   ¿Tiene exactamente 2 elementos?
        3)   ¿Son números enteros?
        4)   ¿Son mayores o iguales a cero?
    +   Si falla cualquiera de estas, el programa lanza el TypeError.
```python
@position.setter
def position(self, value):
    if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value
```
-   Dibujando el Cuadrado (`my_print`):
    +   Líneas vacías: 
        Si position es (0, 2), primero imprimirá dos líneas en blanco.
    +   Espacios horizontales: 
        " " * self.__position[0] crea un "margen" izquierdo.
    +   El cuadrado: 
        El bucle for repite la línea de # tantas veces como sea el size.
```python
def my_print(self):
    if self.__size == 0:
        print("")
        return

    # Eje Y (Saltos de línea verticales)
    if self.__position[1] > 0:
        for i in range(self.__position[1]):
            print("")

    # Eje X (Espacios a la izquierda) + El Cuadrado
    for i in range(self.__size):
        print(" " * self.__position[0] + "#" * self.__size)
```

Output:
```bash
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
```


---



touch 0-square.py 0-main.py 1-main.py 2-main.py 3-main.py 4-main.py 5-main.py 6-main.py 1-square.py 2-square.py 3-square.py 4-square.py 5-square.py 6-square.py README.md

pycodestyle *.py


---
---

#
## Quiz: Python - More Classes and Objects
### Question #0
**What is `__init__`?**
* [ ] A class attribute
* [ ] A class method
* [x] The instance method called when a new object is created
* [ ] The instance method called when a class is called for the first time

### Question #1
**What is `__str__`?**
* [x] Instance method that returns an “informal” and nicely printable string representation of an instance
* [ ] Instance method that returns the dictionary representation of an instance
* [ ] Instance method that prints an “informal” and nicely printable string representation of an instance

### Question #2
**What is `__repr__`?**
* [ ] Instance method that prints an “official” string representation of an instance
* [x] Instance method that returns an “official” string representation of an instance
* [ ] Instance method that returns the dictionary representation of an instance

### Question #3
**What is `__del__`?**
* [ ] Instance method that removes the last character of an instance
* [ ] Instance method that prints the memory address of an instance
* [x] Instance method called when an instance is deleted

### Question #4
**What is `__doc__`?**
* [x] The string documentation of an object (based on docstring)
* [ ] Prints the documentation of an object
* [ ] Creates man file

---

### Question #5
**What do these lines print?**
```python
class User:
    id = 1
print(User.id)
```
*   [ ] None
*   [x] 1
*   [ ] 89
*   [ ] 98

---

###  Question #6
**What do these lines print?**
```python
class User:
    id = 1

u = User()
print(u.id)
```
*   [ ] None
*   [x] 1
*   [ ] 89
*   [ ] 98

### Question #7
**What do these lines print?**
```python
class User:
    id = 1

u = User()
u.id = 89
print(u.id)
```
*   [ ] None
*   [ ] 1
*   [x] 89
*   [ ] 98

### Question #8
**What do these lines print?**
```python
class User:
    id = 1

User.id = 98
u = User()
print(u.id)
```
*   [ ] None
*   [ ] 1
*   [ ] 89
*   [x] 98

### Question #9
**What do these lines print?**
```python
class User:
    id = 1

u = User()
User.id = 98
print(u.id)
```
*   [ ] None
*   [ ] 1
*   [ ] 89
*   [x] 98 (Explicación: La instancia u no tiene su propio id todavía, así que busca el de la clase, que acaba de cambiar a 98)

### Question #10
**What do these lines print?**
```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(u.id)
```
*   [ ] None
*   [ ] 1
*   [x] 89
*   [ ] 98

### Question #11
* * What do these lines print?**
```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)
```
*   [ ] None
*   [ ] 1
*   [ ] 89
*   [x] 98 (Explicación: El atributo de clase User.id sigue siendo 98 aunque la instancia u haya creado su propio u.id = 89)

### Question #12
**What do these lines print?**

```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(User.id)
```
*   [ ] None
*   [ ] 1
*   [ ] 89
*   [x] 98

### Question #13
**What do these lines print?**
```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)
```
*   [ ] None
*   [ ] 1
*   [x] 89
*   [ ] 98 (Explicación: u.id ya existe como atributo de instancia independiente del de la clase)

--
--

#  Exercises
##  0.Simple rectangle
Write an empty class Rectangle that defines a rectangle:  
`0-main`
```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

```
`0-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines an empty Rectangle class.
"""


class Rectangle:
    """
    An empty class that represents a rectangle.
    """
    pass

```

Output:
```bash

{}
```

--
##  1.Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
`1-main`
```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

```
`1-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height.
"""


class Rectangle:
    """
    Representation of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

```

Output:
```bash
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
```

--
##  2.Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
`2-main`
```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

```
`2-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle with area and perimeter methods.
"""


class Rectangle:
    """
    Representation of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

```

Output:
```bash
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```

--
##  3. String representation
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
`3-main`
```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

```
`3-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with string representation.
"""


class Rectangle:
    """
    Representation of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using #.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

```

Output:
```bash
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
```

--

##  4. Eval is magic
`4-main`
```python
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

```
`4-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with with a string representation.
"""


class Rectangle:
    """
    Representation of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using #.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

```

Output:
```bash
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
```

--
##  5. Detect instance deletion
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
`5-main`
```python
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`5-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with a destructor method.
"""


class Rectangle:
    """
    Representation of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using #.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prinsta a message when the isntance is deleted.
        """
        print("Bye rectangle...")

```

Output:
```bash
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
```

--

##  6. How many instances
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
`6-main`
```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

```
`6-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with an instance counter.
"""


class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using #.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message and decrements the counter when deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

```

Output:
```bash
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
```

--

##  7. Change representation
Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
`7-main`
```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
```
`7-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with a customizable print symbol.
"""


class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation using the print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message and decrements the counter when deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

```

Output:
```bash
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
```

--

##  8. Compare rectangles
Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
`8-main`
```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

```
`8-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a rectangle class with a static comparison method.
"""


class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation using the print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message and decrements the counter when deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

```

Output:
```bash
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
```

--

##  9. A square is a rectangle
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
`9-main`
```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

```
`9-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a Rectangle class with a class method for squares.
"""


class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter 2 * (width + height).
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation using the print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message and decrements the counter when deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)

```

Output:
```bash
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

--

touch 0-main.py 1-main.py 2-main.py 3-main.py 4-main.py 5-main.py 6-main.py 7-main.py 8-main.py 9-main.py 0-rectangle.py 1-rectangle.py 2-rectangle.py 3-rectangle.py 4-rectangle.py 5-rectangle.py 6-rectangle.py 7-rectangle.py 8-rectangle.py 9-rectangle.py README.md
