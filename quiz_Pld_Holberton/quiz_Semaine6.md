#   Quiz
---
---
##  0. What is a module?
Score: 1.0

-   [x]A file containing definitions and statements.
-   [ ]A folder with python files.
-   [ ]A file with source code to be compiled.
-   [ ]A folder to store libraries.
-   [ ]I don't know

---
##  1. Which of the following are true for class methods in Python?
Score: 1.0

Please select all valid answers.

-   [x]They are bound to a class rather than its object.
-   [x]They don't require creation of a class instance, much like static methods.
-   [x]They work with the class since its parameter is always the class itself.
-   [ ]I don't know

---
##  2. What is __str__ in Python?
Score: 1.0

-   [ ]It is a special attribute that contains the documentation string for a module, class, function, or method.
-   [x]It returns a human-readable, or informal, string representation of an object.
-   [ ]It returns a more information-rich, or official, string representation of an object.
-   [ ]It represents a dictionary or any mapping object that is used to store the attributes of the object.
-   [ ]I don't know

---
##  3. Which of the following statements correctly describe how to define and implement an interface in Python using abstract base classes ?
Score: 0.0

Select all the correct answers.

-   [x]An interface in Python is typically defined using a class that inherits from ABC and includes only abstract methods.
-   [ ]A class that implements an interface must provide concrete implementations for all abstract methods (meaning; defining the functions logic).
-   [ ]Abstract methods are marked with the @classmethod decorator.
-   [x]Abstract methods are marked with the @abstractmethod decorator.
-   [x]The abc module provides tools to define interfaces using abstract base classes.
-   [ ]I don't know

##  4. What do these lines print?
Score: 1.0
```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)
```
-   [ ]1
-   [ ]99
-   [x]100
-   [ ]Throws exception
-   [ ]I don't know

##  5. What is self in Python?
Score: 1.0

-   [x]It is a reference to the current instance of the class.
-   [ ]It is a reference to the current class.
-   [ ]It is a reference to an objects' id.
-   [ ]I don't know

##  6. What do these lines print?
Score: 0.0
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
-   [ ]'name'
-   [ ]None
-   [ ]'John'
-   [x]'no name'
-   [ ]I don't know

##  7. What does the acronym "ABC" stand for in Python’s abstract class context ?
Score: 1.0

Select the correct answer.

-   [ ]Abstract Built-in Class
-   [x]Abstract Base Class
-   [ ]Abstract Basic Constructor
-   [ ]Abstract Behavior Control
-   [ ]I don't know

##  8. What is __dict__ in Python?
Score: 0.0

-   [x]It represents a dictionary or any mapping object that is used to store the attributes of the object.
-   [ ]It returns a human-readable, or informal, string representation of an object.
-   [ ]It returns a more information-rich, or official, string representation of an object.
-   [ ]It is a special attribute that contains the documentation string for a module, class, function, or method.
-   [ ]I don't know

##  9. Select all the correct answers, regarding the following code example :
Score: 1.0
```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("The animal is sleeping.")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


my_dog = Dog()
my_dog.make_sound()
my_dog.sleep()
```
-   [x]Animal is an abstract class because it inherits from ABC and because it contains a concrete implementation of the method sleep().
-   [ ]Animal is an interface.
-   [x]The implementation of the Dog subclass is correct.
-   [ ]The implementation of the Dog subclass is not correct because it needs to have the concrete implementation of the method sleep().
-   [ ]I don't know

##  10. Which of the following statements are true regarding abstract classes in Python ?
Score: 0.0

Select all the correct answers.

-   [x]Abstract classes can contain both abstract methods and concrete (fully implemented) methods.
-   [x]To create an abstract class, it must inherit from the ABC class provided by the abc module.
-   [ ]Abstract methods must be defined with an implementation, even if it's a pass statement.
-   [x]A subclass of an abstract class must implement all its abstract methods to be instantiable.
-   [ ]I don't know

##  11. In this following code, what is __password?
Score: 1.0
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
-   [x]A private class attribute
-   [ ]A private instance attribute
-   [ ]A protected instance attribute
-   [ ]A protected class attribute
-   [ ]A public instance attribute
-   [ ]A public class attribute
-   [ ]I don't know

##  12. What is __repr__ in Python?
Score: 1.0

-   [ ]It represents a dictionary or any mapping object that is used to store the attributes of the object.
-   [ ]It returns a human-readable, or informal, string representation of an object.
-   [x]It returns a more information-rich, or official, string representation of an object.
-   [ ]It is a special attribute that contains the documentation string for a module, class, function, or method.
-   [ ]I don't know

##  13. Which of the following are true for __init__ in Python?
Score: 1.0

Please select all valid answers.

-   [x]is used to initialize (assign values) to the data members of the class when an object of the class is created
-   [x]is executed at the time of object creation
-   [ ]it is a private method
-   [x]it is a constructor method
-   [ ]I don't know

##  14. What are the pillars of OOP?
Score: 0.0

Please select all valid answers.

-   [x]Abstraction
-   [x]Polymorphism
-   [x]Encapsulation
-   [x]Inheritance
-   [ ]Data hiding
-   [ ]Efficiency
-   [ ]Collaboration
-   [ ]I don't know

##  15. Based on this code, what should all the test cases be?
Score: 0.0
```python
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```
Select all valid answers

-   [x]empty list
-   [x]list with one element (any type)
-   [x]list with 2 different elements (same type)
-   [x]list with the same element twice (same type)
-   [x]list with more than 2 times the same element (same type)
-   [ ]list with multiple types (integer, string, etc...)
-   [x]not a list argument (ex: passing a dictionary to the method)
-   [ ]I don't know

##  16. What would happen if we run this code?
Score: 1.0
```python
class Animal:
    def Walk(self):
        print('Hello, I am the parent class')

class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')

r = Dog()
r.Walk()
```
-   [x]The text Hello, I am the child class would be displayed
-   [ ]The text Hello, I am the parent class would be displayed.
-   [ ]Throws an exception
-   [ ]I don't know

##  17. Which of the following is a feature of Python DocString?
Score: 1.0

Please select all valid answers.

-   [x]In Python all functions should have a docstring.
-   [x]Docstrings can be accessed by the __doc__ attribute on objects.
-   [x]It provides a convenient way of associating documentation with Python modules, functions, classes, and methods.
-   [ ]Docstrings can be accessed by the __str__ attribute on objects.
-   [ ]I don't know
