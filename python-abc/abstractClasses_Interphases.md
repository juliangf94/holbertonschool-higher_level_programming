# Learning Objectives:
##  Abstract Classes: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
An Abstract Class is a blueprint for other classes.  
It allows you to define methods that must be created within any child classes.  
You cannot create an instance of an abstract class;  
its only purpose is to ensure that subclasses follow a specific structure.

Key Tool: Python's abc (Abstract Base Classes) module.

##  Interfaces and Duck Typing: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
-   Interfaces: A "contract" that defines what methods a class should have, without providing the logic.

-   Duck Typing: A philosophy in Python that says: "If it walks like a duck and it quacks like a duck, then it must be a duck." This means Python cares about whether an object has the required methods, not what the actual type of the object is.
##  Subclassing Standard Base Classes: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
Python allows you to inherit from built-in classes like `list`, `dict`, or `str`.  
This is useful when you want to create a custom data structure that behaves like a standard one but has extra features (e.g., a list that automatically sorts itself when items are added).
##  Method Overriding: Employ method overriding to alter or enhance the behavior of base class methods.
**Method Overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. This allows the subclass to change or enhance the behavior of that method while keeping the same name.
##  Multiple Inheritance: Understand and apply multiple inheritance to form complex relationships between classes.
This is a feature where a class can inherit attributes and methods from more than one parent class.

-   Challenge: It can lead to complexity (the Diamond Problem).

-   Resolution: Python uses MRO (Method Resolution Order) to decide which parent's method to call first
##  Mixins: Utilize mixins to compose behavior across unrelated classes.
A Mixin is a specialized type of multiple inheritance. It is a small class that provides a specific set of "plug-in" methods to other classes. Mixins are not meant to stand alone; they are designed to add specific behaviors (like "logging" or "serialization") to unrelated classes without creating a complex hierarchy.


---
---
#   Exercises
##  0. Abstract Animal Class and its Subclasses
1) Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
2) Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.  
`main_00_abc.py `
```python
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

```
`task_00_abc.py`
```python
#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
It demonstrates the use of Abstract Base Classes (ABC) to enforce method
implementation in derived classes.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an Animal.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        Returns:
            The sound of the animal.
        """
        pass

class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """
    def sound(self):
        """
        Implementation of the sound method for a Dog.
        Returns:
            str: The string "Bark".
        """
        return "Bark"

class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """
    def sound(self):
        """
        Implementation of the sound method for a Cat.
        Returns:
            str: The string "Meow".
        """
        return "Meow"

```
**Logic**

**Ouput**
```bash
Bark
Meow
Traceback (most recent call last):
  File "main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```
---
##  1. Shapes, Interfaces, and Duck Typing
1) Create an abstract class named Shape with two abstract methods: area and perimeter.
2) Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
3) Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
4) Test the shape_info function with instances of both Circle and Rectangle.  
`main_01_duck_typing.py `
```python
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
```
`task_01_duck_typing.py`
```python
#!/usr/bin/env python3
"""
This module defines the Shape abstract class and its subclasses,
Circle and Rectangle, to demonstrate duck typing and interfaces.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class defining the blueprint for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Concrete class representing a Circle.
    """
    def __init__(self, radius):
        """
        Initializes the circle with a radius.
        """
        self.radius = radius
    
    def area(self):
        """Returns the area of the circle: pi * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle: 2 * pi * r"""
        return 2 * math.pi * self.radius
        
class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter: 2 * (width + height)"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Standalone function that uses Duck Typing to print
    information about any object that has area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

```
**Logic**

**Ouput**
```bash
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```
---

##  2. Extending the Python List with Notifications
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).  
`main_02_verboselist.py `
```python
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

```
`task_02_verboselist.py`
```python
#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in list.
It provides notifications when items are added or removed.
"""


class VerboseList(list):
    """
    A custom list class that prints a message when modified.
    """

    def append(self, item):
        """
        Adds an item and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends the list and prints a notification with the count.
        """
        item_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item):
        """
        Prints a notification and removes an item.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Prints a notification and pops an item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

```
**Logic**

**Ouput**
```bash
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```
---
##  3. CountedIterator - Keeping Track of Iteration
Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.  
`main_03_countediterator.py`
```python
#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

```
`task_03_countediterator.py`
```python
#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator to keep track of how many items have been processed.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.

        Returns:
            int: The iteration count.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.

        Returns:
            The next item from the sequence.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

```
**Logic**

**Ouput**
```bash
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```
---

##  4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Construct a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.  
`main_04_flyingfish.py `
```python
#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

```
`task_04_flyingfish.py`
```python
#!/usr/bin/python3
"""
This module explores multiple inheritance through Fish, Bird,
and the hybrid FlyingFish classes.
"""


class Fish:
    """
    Class representing a fish
    """
    def swim(self):
        """
        Prints swimming behavior.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird
    """
    def fly():
        """
        Prints flying behavior.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, inheriting from both Fish and Bird.
    """
    def fly(self):
        """
        Overrides Bird's fly method.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides Fish's swim method.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides both parent habitat methods.
        """
        print("The flying fish lives both in water and the sky!")

```
**Logic**

**Ouput**
```bash
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```
---

##  5. The Mystical Dragon - Mastering Mixins
Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.  
`main_05_dragon.py `
```python
#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

```
`task_05_dragon.py`
```python
#!/usr/bin/python3
"""
This module demonstrates the Mixin pattern by creating specialized
classes for swimming and flying, then combining them into a Dragon class.
"""


class SwimMixin:
    """
    Provides swimming functionality.
    """
    def swim(self):
        """
        Prints a swimming message.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Provides flying functionality.
    """
    def fly(self):
        """
        Prints a flying message.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors from SwimMixin and FlyMixin.
    """
    def roar(self):
        """
        Prints a roar message unique to the Dragon.
        """
        print("The dragon roars!")

```
**Logic**

**Ouput**
```bash
The creature swims!
The creature flies!
The dragon roars!
```
---

##  

` `
```python

```
` `
```python

```
**Logic**

**Ouput**
```bash

```
---

##  

` `
```python

```
` `
```python

```
**Logic**

**Ouput**
```bash

```
---
**files**  
touch README.md task_00_abc.py task_01_duck_typing.py task_02_verboselist.py task_03_countediterator.py task_04_flyingfish.py task_05_dragon.py
**main**  
touch main_00_abc.py main_01_duck_typing.py main_02_verboselist.py main_03_countediterator.py main_04_flyingfish.py main_05_dragon.py 
**test**  
pycodestyle *.py
