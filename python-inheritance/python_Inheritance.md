#   General
---
---
#   What is a superclass, baseclass or parentclass?
These three terms are synonyms.  
A superclass, base class, or parent class is a class from which another class inherits attributes and methods.
It acts as the "blueprint" that provides its attributes and methods to other classes.
-   The superclass defines common behavior.
-   The subclass inherits that behavior automatically.
-   A subclass can add new methods or override inherited ones.
-   In Python, a class can inherit from one or multiple superclasses.
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass

d = Dog()
print(d.speak())  # Output: Some sound
```
-   Animal is the superclass / base class / parent class
-   Dog is the subclass / child class
-   Dog inherits the speak() method from Animal

---

#   What is a subclass?
A Subclass (or Child Class) is a class that inherits from another class.  
it gains all the functionality of the parent class but can also add its own unique features or modify existing ones.
---
#   How to list all attributes and methods of a class or instance?
-   `dir(object)`:  
    Returns a list of all valid attributes and methods (including inherited and "dunder" methods).
-   `object.__dict__`:        
    Returns only the instance attributes currently stored in that specific object.
---
#   When can an instance have new attributes?
In Python, you can add new attributes to an instance at any time simply by assigning a value to a new name (e.g., my_instance.new_var = 10).  
This usually happens inside the __init__ method, but it can happen anywhere in the code unless the class uses __slots__.
---
#   How to inherit class from another?
Inheritance is essentially a mechanism where a Subclass (the child) takes on the attributes and methods of a Base Class (the parent).

-   Single Inheritance: Pass the parent class in parentheses during definition.
```python
class Child(Parent):
    pass
```
The `super()` function: This is the proxy object that allows you to refer to the parent class without naming it explicitly.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # super() calls the __init__ of Animal
        super().__init__(name) 
        self.breed = breed
```
---
#   How to define a class with multiple base classes?
-   Multiple Base Classes: Python allows a class to inherit from multiple parents.
    +   MRO (Method Resolution Order): Python uses an algorithm called C3 Linearization to determine the "search path" for methods.
        *   The Order Matters: In **class Android(Robot, Human)**:
            Python looks for a method in `Android` first, then `Robot`, then `Human`.
        *   Checking the path: 
            You can always see this order by calling `Android.mro()` or `help(Android)`.
```python
class Android(Robot, Human):
    pass
```
```python
class Robot:
    def greet(self):
        print("Beep Boop")

class Human:
    def greet(self):
        print("Hello!")

class Android(Robot, Human):
    pass

# Since Robot was listed first, the Android says "Beep Boop"
my_droid = Android()
my_droid.greet()
```
---
#   What is the default class every class inherit from?
In Python 3, every class you create automatically inherits from the `object` class.  
This is the root of all classes and provides default methods like __str__ and __repr__.
Even if you write a "naked" class like 
    `class MyClass:`
Python secretly sees it as 
    `class MyClass(object):`
This is why every object you create, no matter how simple, already knows how to:
    -   Be represented as a string (__str__).
    -   Compare itself to others (__eq__).
    -   Be initialized (__init__).
---
#   How to override a method or attribute inherited from the base class?
To override something, you simply redefine it in the subclass with the exact same name.
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self): # This overrides the Parent method
        print("Hi from Child!")
```

---
#   Which attributes or methods are available by heritage to subclasses?
All non-private attributes and methods are available to subclasses.  
In Python, even "private" attributes (starting with __) are inherited, but they are "name-mangled," making them harder to access.
---
#   What is the purpose of inheritance?
The primary goals of inheritance are:
    -   Code Reusability: Write code once in a parent class and use it in many subclasses.
    -   Logical Hierarchy: Organize code to reflect real-world relationships (e.g., a Square is a Rectangle).
    -   Extensibility: Add new features to existing code without modifying the original class.
---
#   What are, when and how to use isinstance, issubclass, type and super built-in functions?
-   `isinstance(obj, Class)`: Checks if an object is an instance of a class (or its subclasses). It´s used for **input validation** within functions to ensure the data passed is of a compatible type.
    +   Example_1:
        **isinstance(obj, int)** will be True only if obj.__class__ is int or some class derived from int.
    +   Example_2:
        **isinstance(my_dog, Animal)**
    +   Example_3: Using a tuple of classes to check for multiple types.
```python
def calculate_area(shape):
    # Check if the object is either a Square or a Circle
    if isinstance(shape, (Square, Circle)):
        return shape.area()
    return "Unknown shape type"
```
-   `issubclass(A, B)`: 
    Checks if class A inherits from class B.  
    It´s useful when you are working with classes themselves (the "blueprints") rather than specific objects.
    +   Example_1:
        **issubclass(bool, int)** is True since bool is a subclass of int. 
        *   However, **issubclass(float, int)** is False since float is not a subclass of int.
    +   Example_2:
        **issubclass(Square, Rectangle)**
    +   Example_3: Checking custom hierarchy.
```python
class Vehicle: pass
class Truck(Vehicle): pass
class Food: pass

print(issubclass(Truck, Vehicle)) # True
print(issubclass(Truck, Food))    # False
```
-   `type(obj)`: 
    Returns the exact class type of an object (ignores inheritance).  
    It´s used when you need **strict identity**.  
    +   Example_1:  
        **type(my_obj) == Rectangle**
    +   Example_2: Distinguishing between a parent and a child.
```python
class Parent: pass
class Child(Parent): pass

c = Child()

print(isinstance(c, Parent)) # True (Inheritance counts)
print(type(c) == Parent)     # False (Identity only: c is a Child, not a Parent)
```
-   `super()`:  
    Used to call a method from the parent class inside a subclass.  
    It´sused to **extend** a parant´s method instead of completely replacing it.
    +   Example_1: 
        **super().__init__(width, height)**
    +   Example_2: Extending a method other than __init__.
```python
class Worker:
    def work(self):
        print("Doing general tasks...")

class Manager(Worker):
    def work(self):
        super().work() # Do the general tasks first
        print("Also managing the team.") # Then add specific logic
```
---
---
#  Quiz
## Question #0

**What do these lines print?**

```python
b = Base()
print(b.id)
```

* [ ] None
* [ ] 0
* [x] 1

**Explanation:** `__nb_instances` starts at 0 and is incremented in `__init__` before assigning `id`, so the first instance gets `id = 1`.

---

## Question #1

**What do these lines print?**

```python
for i in range(3):
    b = Base()
print(b.id)
```

* [ ] None
* [x] 3
* [ ] 4
* [ ] 2

**Explanation:** Three instances are created, incrementing `__nb_instances` to 3. `b` refers to the last instance.

---

## Question #2

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [ ] None
* [ ] 0
* [x] 1
* [ ] 2

**Explanation:** `User` inherits from `Base` and does not override `__init__`, so `Base.__init__` is called once.

---

## Question #3

**What do these lines print?**

```python
for i in range(4):
    u = User()
print(u.id)
```

* [x] 4
* [ ] 3
* [ ] 5
* [ ] None

**Explanation:** Four `User` instances are created, each calling `Base.__init__`. The last instance has `id = 4`.

---

## Question #4

**What do these lines print?**

```python
b = Base()
u = User()
print(u.id)
```

* [ ] 0
* [ ] 1
* [x] 2
* [ ] 3

**Explanation:** First `Base()` sets the counter to 1, then `User()` increments it to 2.

---

## Question #5

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [x] 89
* [ ] 90
* [ ] 1

**Explanation:** `User.__init__` overrides `Base.__init__` and does not call `super()`, so `id` is manually set to 89.

---

## Question #6

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [ ] None
* [ ] 0
* [x] 1
* [ ] 2

**Explanation:** `super().__init__()` calls `Base.__init__`, creating the first instance and assigning `id = 1`.

---

## Question #7

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [ ] 89
* [ ] 90
* [x] 1

**Explanation:** Although `id` is first set to 89, `super().__init__()` runs after and overwrites it with `id = 1`.

---

## Question #8

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [x] 89
* [ ] 90
* [ ] 1

**Explanation:** `super().__init__()` sets `id = 1`, then `self.id = 89` overwrites it.

---

## Question #9

**What do these lines print?**

```python
u = User()
print(u.id)
```

* [ ] 99
* [x] 100
* [ ] 1

**Explanation:** `super().__init__()` sets `id = 1`, then `self.id += 99` results in `id = 100`.

---
---
#   Exercises
##  0. Lookup
Write a function that returns the list of available attributes and methods of an object:
`0-main.py`
```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

```
`0-lookup.py`
```python
#!/usr/bin/python3
"""
This module provides a function to look up attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)

```
-   
**Output**
```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```
---

##  1. My list
Write a class MyList that inherits from list
`1-main.py`
```python
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

```
`tests/1-my_list.txt`
```

```
`1-my_list.py`
```python
#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that provides a method to print sorted elements.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))

```
-   
**Output**
```bash
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

python3 -m doctest ./tests/*
---
##  2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
`2-main.py`
```python
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

```
`2-is_same_class.py`
```python
#!/usr/bin/python3
"""
This module contains a function that checks if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if it is the exact same class, False otherwise.
    """
    return type(obj) is a_class

```
**Why not use isinstance()**:
-   `isinstance(obj, a_class)`: 
    Returns True if the object is an instance of the class or any subclass of that class.  
    For example, if you have a Square that inherits from Rectangle, isinstance(my_square, Rectangle) would be True.

-   `type(obj) is a_class`: 
    Returns True only if the object was created directly from that specific class.  
    It ignores the inheritance chain completely.

In **2-main.py** example, an integer `a = 1` is technically an instance of object (because everything in Python inherits from object), but `is_same_class(a, object)` must return False because 1 is exactly an int, not an object.

**Output**
```bash
1 is an instance of the class int
```
---

##  3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
`3-main.py`
```python
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

```
`3-is_kind_of_class.py`
```python
#!/usr/bin/python3
"""
This module contains a function to vertify if an object is an instance of,
or inherited from, a specific class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance or inherited from a_class;
        otherwise False.
    """
    return isinstance(obj, a_class)

```
`isinstance(obj, a_class)`: This function returns True if obj is an instance of a_class OR if it is an instance of a subclass of a_class. 
**Output**
```bash
1 comes from int
1 comes from object
```
---

##  4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
`4-main.py`
```python
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

```
`4-inherits_from.py`
```python
#!/usr/bin/python3
"""
This module contains a function to vertify if an object is an instance of
a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj inherited from a_class and is not an exact instance
        of a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

```
**Logic**
In 4-main.py example with `a = True`:
    -   In Python, bool is a subclass of int.
    -   `inherits_from(a, int)` is True because bool inherits from int.
    -   `inherits_from(a, bool)` is False because a is exactly a bool.  
        It didn't "inherit" from itself; it is that class.
    -   `inherits_from(a, object)` is True because bool eventually inherits from object.  
**Compare**
| Task	| Function Logic | Purpose |
| :.. | :.. | :.. |
| 2. Same Class	| type(obj) is a_class	| Exact match only.
| 3. Kind of	| isinstance(obj, a_class)	| Match or Inherited (General).
| 4. Inherits from	| isinstance AND type is not	| Inherited only  (Excludes exact match).

**Output**
```bash
True inherited from class int
True inherited from class object
```
---

##  5. Geometry module
Write an empty class BaseGeometry.
`5-main.py`
```python
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

```
`5-base_geometry.py`
```python
#!/usr/bin/python3
"""
This module contains an empty class named BaseGeometry
"""


class BaseGeometry:
    """
    An empty class that will serve as a base for geometry shapes.
    """
    pass

```
-   
**Output**
```bash
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
---

##  6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).
`6-main.py`
```python
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`6-base_geometry.py`
```python
#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class used to represent geometry
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always, because it is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

```
-   
**Output**
```bash
[Exception] area() is not implemented
```
---

##  7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).
`7-main.py`
```python
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`7-base_geometry.py`
```python
#!/usr/bin/python3
"""
This module defines a class BaseGeometry with area and integer validator
"""


class BaseGeometry:
    """
    A class used to represent geometry
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always, because it is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

```
-   
**Output**
```bash
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```
---
python3 -m doctest ./tests/*

##  8. Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
`8-main.py`
```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

```
`8-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance, inherith from BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

```
-   
**Output**
```bash
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
```
---

##  9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
`9-main.py`
```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

```
`9-rectangle.py`
```python
#!/usr/bin/python3
"""
This module defines a class Rectangle with area and str
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance, inherith from BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle description in format
            [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

```
**Logic**
-      
**Output**
```bash
[Rectangle] 3/5
15
```
---

##  10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py):
`10-main.py`
```python
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

```
`10-square.py`
```python
#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

```
**Logic**
Using `super()`:
    The line `super().__init__(size, size)` is the most important part of this task.  
    It calls the __init__ method of the Rectangle class.  
    By passing the same size twice, we fulfill the rectangle's requirement for a width and a height while ensuring they are equal.
**Output**
```bash
[Rectangle] 13/13
169
```
---

##  11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
`11-main.py`
```python
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

```
`11-square.py`
```python
#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The square description in format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

```
**Logic**

-   
**Output**
```bash
[Square] 13/13
169
```
---
touch README.md 0-main.py 1-main.py 2-main.py 3-main.py 4-main.py 5-main.py 6-main.py 7-main.py 8-main.py 9-main.py 10-main.py 11-main.py

touch 0-lookup.py 1-my_list.py 2-is_same_class.py 3-is_kind_of_class.py 4-inherits_from.py 5-base_geometry.py 6-base_geometry.py 7-base_geometry.py 8-rectangle.py 9-rectangle.py 10-square.py 11-square.py

touch 1-my_list.txt 7-base_geometry.txt
