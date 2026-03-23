#   Quiz 
#   Serialization / Deserialization + OOP + UML
##  0. In a UML Sequence Diagram, what does a dashed line between two objects indicate ?
Score: 1.0

Select the correct answer.

For clarification this is a dashed line:
- - - - - - - - - - - - - - - - - - - - - -

-   [ ]A random user
-   [ ]The creation of an object
-   [x]A return message
-   [ ]I don't know

##  1. Select the correct answer.
Score: 1.0

Given the following code, which class method greating is going to be called ?
```python
class A:
  def greating(self):
    print("Hello from class A")

class B(A):
  def greating(self):
    print("Hello from class B")

class C(B, A):
  pass

obj = C()
obj.greating()
```
-   [ ]The greating() method from the C class.
-   [ ]The greating() method from the A class.
-   [x]The greating() method from the B class.
-   [ ]None, there's an error in the class C and the code won't (will not) work.
-   [ ]I don't know

##  2. Select the correct answer.
Score: 1.0

Given the following code, which class method greating is going to be called ?
```python
class A:
  def greating(self):
    print("Hello from class A")

class B(A):
  def greating(self):
    print("Hello from class B")

obj = B()
obj.greating()
```
-   [ ]The greating() method from the A class.
-   [x]The greating() method from the B class.
-   [ ]There's a code error and no method is going to be called.
-   [ ]I don't know

##  3. Select all the correct statements about JSON.
Score: 1.0

-   [x]JSON stands for Javascript Object Notation.
-   [ ]JSON stands for Java Object Noting.
-   [ ]JSON stands for Javascript Objective Notation.
-   [x]JSON is a standard file format used mainly for data interchange.
-   [ ]JSON isn't a standard file format but a native python data type like int, list, tuples etc...
-   [ ]I don't know

##  4. What is data deserialisation and what are some of its valid examples ?
Score: 0.0

Select all the correct answers.

-   [x]Is the opposite of data serialization.
-   [ ]It's the same thing as data serialization, it's just another name.
-   [ ]Example: from Python Dictionary to JSON.
-   [x]Example: from JSON to Python Dictionary.
-   [ ]I don't know

##  5. Select all the correct statements
Score: 1.0

Select all the correct statements about the following functions json.dump() and json.dumps().

-   [ ]There's the same, they just have two different names.
-   [ ]The dumps() function doesn't exist.
-   [x]The json.dumps(dict, indent) function converts a Python object to a JSON string.
-   [ ]The json.dumps(dict, indent) function converts a JSON string to a Python object.
-   [x]The json.dump(dict, file) function is used for writing data into a JSON file.
-   [ ]I don't know

##  6. Select all the correct statements about the function below.
Score: 1.0
```python
def func(*argv):
    // some code here (not relevant)
    // ...
```
-   [ ]The function func can take only one argument at a time.
-   [x]The function funccan take a variable (changeable) number of non-keyword arguments.
-   [x]This is a correct way to use the function func: func("my name ", "is ", "Kyle").
-   [x]This is a correct way to use the function func: func("hello world").
-   [ ]This is a correct way to use the function func: func(name='James', age=35, job='programmer', level='senior').
-   [ ]I don't know

##  7. What does UML stand for ?
Score: 1.0

Select the correct answer.

-   [ ]Universal Modeling Language
-   [ ]Unified Markup Language
-   [x]Unified Modeling Language
-   [ ]Universal Markup Language
-   [ ]I don't know

##  8. Is the following statement correct ?
Score: 1.0

The json.load(file_object) function reads from a file JSON data and parses it into a Python object (usually a dictionary).

-   [x]True
-   [ ]False
-   [ ]I don't know

##  9. Select all the correct statements about the function below.
Score: 1.0
```python
def func(**kwargs):
    // some code here (irrelevant)
    // ...
```
-   [x]The function func can take a variable (changeable) number of keyword arguments.
-   [ ]The function's argument isn't correct and it will never work.
-   [ ]This is a correct way to use the function func: func("my name ", "is ", "Kyle").
-   [ ]This is a correct way to use the function func: func("hello ", name="Armin", job="DJ").
-   [x]This is a correct way to use the function func: func(name='James', age=35, job='programmer', level='senior').
-   [ ]I don't know

##  10. What is data serialisation and what are some of its valid examples ?
Score: 1.0

Select all the correct answers.

-   [x]Data serialization is the process of converting data objects into a format that can be easily stored, transmitted, or shared across different systems or platforms (like JSON, XML etc...).
-   [ ]Data serialization is the process of converting data from a standard format (like JSON, XML etc..) into a data object appropriate to a specific programming language.
-   [x]Example: from Python dictionary to JSON.
-   [x]Example: from Javascript object to XML.
-   [ ]Example: from JSON to Python dictionary.
-   [ ]I don't know

##  11. Select the correct answer.
Score: 1.0

Given the following code, which class method greating is going to be called ?
```python
class A:
  def greating(self):
    print("Hello from class A")

class B:
  def greating(self):
    print("Hello from class B")


class C(A, B):
  pass


class D(C, B):
  pass

obj = D()
obj.greating()
```
-   [x]The greating() method from the A class.
-   [ ]The greating() method from the B class.
-   [ ]The greating() method from the C class.
-   [ ]The greating() method from the D class.
-   [ ]The code won't work because there's an error.
-   [ ]I don't know

##  12. In UML, which diagram is used to show the dynamic interaction between objects over time ?
Score: 1.0

Select the correct answer.

-   [x]Sequence Diagram
-   [ ]Class Diagram
-   [ ]DataBase Diagram
-   [ ]Use Case Diagram
-   [ ]I don't know

##  13. Select the correct answer.
Score: 1.0

Given the following code, which class method greating is going to be called ?
```python
class A:
  def greating(self):
    print("Hello from class A")

class B(A):
  def greating(self):
    print("Hello from class B")

class C(B):
  def greating(self):
    print("Hello from class C")

obj = C()
obj.greating()
```
-   [ ]The greating() method from the B class.
-   [x]The greating() method from the C class.
-   [ ]The greating() method from the A class.
-   [ ]No method is going to be called because there's a code error.
-   [ ]I don't know

##  14. In a UML Class Diagram, which of the following is NOT a valid visibility symbol ?
Score: 1.0

Select the correct answer.

-   [ ]+
-   [ ]-
-   [x]&
-   [ ]#
-   [ ]I don't know
