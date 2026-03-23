

##  Que signifie OOP ?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which bundle data (attributes) and behavior (methods) together. 
OOP helps organize code, improve reusability, and model real-world entities.

##  C'est quoi une classe ?
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

##  C'est quoi une instance ?
A specific object created from a class.


##  C'est quoi la différence entre une classe, un objet et une instance ?
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



##  Qu'est ce qu'une méthode (method) en Python ?
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


##  C'est quoi la méthode init ?
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



##  C'est quoi le mot self en python ?
`self` is a reference to the current instance of the class. 
-   It is used to access instance attributes and methods inside the class.
-   A parameter thath you must add to the beginning of the list and don´t give a value to it.  
-   It will refer to the object itself.


##  C'est quoi la différence entre une attribue (attribute) et une propriété (property) en Python ?
An attribute stores data directly.
A property controls access to data using getter, setter, and deleter methods.

##  C'est quoi le dict en Python ?
`__dict__` is a dictionary that stores an object’s or class’s attributes and their values.
-   An instance __dict__ contains attributes specific to that object.

-   A class __dict__ contains the methods and class-level attributes.   



##  Le  getattr() est quoi et elle sert à quoi ?
The `getattr(object, name[, default])` function allows you to access an attribute using a string name rather than a dot operator.
```python
# Equivalent to: value = obj.size
value = getattr(obj, "size")

# Safely get attribute with a default if it doesn't exist
status = getattr(obj, "missing_attr", "Not Found")
```


##  C'est quoi la méthode str en python?
__str__: Used for creating a "pretty," user-friendly string representation of the object (used by print()).




##  C'est quoi la méthode repr en python ?
__repr__: Used for an "official," technical string representation. It is meant for developers and should ideally be a string that can be used to recreate the object (used by eval()).


##  Quelle est la  différence entre instance method (méthode d'instance), class method (méthode de classe) et static method (méthode statique) en Python ?
-   Instance method:
    +   This is the default type of method.
        *   Decorator:
            None
        *   First argument: 
            Always self, which points to the specific instance (the object) calling the method.
        *   Capability:
            It can read and modify both instance attributes (like `self.width`) and class attributes.
        *   Example:
            `def area(self):`
-   Class Method:
    +   A classs method is bound to the class rather than the object.
        *   Decorator:  
            `@classmethod`
        *   First Argument: 
            Always takes `cls` as the first argument, which points to the **Class**, not the instance.
        *   Capability:
            It can modify **class attributes** (like `number_of_instances`) but cannot access instance attributes (like `self.width`) because the class doesn´t know about specific objects.  
            It is often used as a "factory" to create new objects.
        *   Example:
            `def square(cls, size):`
-   Static Method:
    +   A static method is a "namespace" method.
    +   It lives inside the class because it relates to it, but it doesn´t need to know anything about the class or the object.
        *   Decorator:
            `@staticmethod`
        *   First Argument:
            None (it takes no special first argument like `self` or `cls`).
        *   Capability:
            It acts like a regular function. 
            It cannot modify the state of the class or the instance. 
            It is used for utility functions that perform a task related to the class (like comparing two objects).
        *   Example:
            `def bigger_or_equal(rect_1, rect_2):`
```python
class MyClass:
    class_attr = 0

    def instance_method(self):
        return f"I can see {self}"

    @classmethod
    def class_method(cls):
        return f"I can see class attributes of {cls}"

    @staticmethod
    def static_method(a, b):
        return a + b
```
Ejemplo de self y cls:
```python
class Habitante:
    poblacion_total = 0  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia
        Habitante.poblacion_total += 1

    # Usa self porque le interesa el nombre de CADA uno
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    # Usa cls porque le interesa la clase entera
    @classmethod
    def mostrar_poblacion(cls):
        print(f"Hay {cls.poblacion_total} habitantes en total")
```

##  Quelle est la différence entre class attribute et instance attribute (attribut d'une classe et attribut d'une instance) ?
-   Class Attribute: Shared by all instances of a class (e.g., all humans belong to the species "Homo Sapiens"). Defined directly under the class header.
    +   A Class Attribute is a variable that belongs to the Class itself, not to any specific object.
        *   Definition: 
            It is defined directly inside the class body, outside of any methods.
        *   Ownership: 
            It is shared by all instances of that class.
        *   Behavior: 
            If you change the value of a class attribute (via the class name), that change is reflected in every single object of that class.
        *   Typical Use Case: 
            Storing constants, default settings, or counters (like your `number_of_instances` variable).

-   Instance Attribute: Unique to each object (e.g., every person has a different name). Defined inside __init__.
    +   An Instance Attribute is a variable that belongs to a specific object.
        *   Definition: 
            It is usually defined inside the `__init__` method using the `self` keyword (e.g., `self.width`).
        *   Ownership: 
            It belongs only to the specific instance created.
        *   Behavior: 
            Changing an instance attribute in one object does not affect other objects of the same class.
        *   Typical Use Case: 
            Storing data that should be unique to each object (like the specific `width` and `height` of a rectangle).
```python
class Dog:
    species = "Canine"  # Class Attribute (All dogs are canines)

    def __init__(self, name):
        self.name = name  # Instance Attribute (Each dog has its own name)

# Creating instances
dog1 = Dog("Fido")
dog2 = Dog("Rex")

print(dog1.species) # Canine
print(dog2.species) # Canine

# Changing a Class Attribute affects everyone
Dog.species = "Lupine"
print(dog1.species) # Lupine (It changed for Fido too!)

# Changing an Instance Attribute affects only that object
dog1.name = "Sparky"
print(dog2.name)    # Rex (Remains unchanged)
```
