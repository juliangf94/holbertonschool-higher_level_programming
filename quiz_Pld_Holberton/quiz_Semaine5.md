#   Quiz
Date: 2026-01-29
Status: Done
Duration: 11 minutes

Score: 93.33%

##  0. What does OOP stand for ?
Score: 1.0

-   [] Objectively Oriented Programs
-   [x] Object Oriented Programming
-   [] Object Orienting Programs
-   [] Objectively Orienting Programming
-   [] I don't know

##  1. What is the output of the following Python3 code ?
Score: 1.0
```python
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(new_list)
```
-   [ ][1, 2, 3]
-   [ ][1, 2, 3, 4]
-   [x][2, 3, 4]
-   [ ][2, 3]
-   [ ]I don't know

##  2. Which of the following code snippets correctly creates a list in Python3 ?
Score: 0.0

Select all the correct options.

-   [x]my_list = list((1, 2, 3, 4))
-   [ ]my_list = list(1, 2,3,4)
-   [x]my_list = [1, 2, 3, 4]
-   [ ]my_list = {1, 2, 3, 4}
-   [ ]my_list = (1, 2, 3, 4)
-   [ ]I don't know

##  3. How can you remove an item from a list in Python3 ?
Score: 1.0
```python
Let’s suppose that we want to remote the element 30 from the following list:
my_list = [10, 20, 30, 40, 50]
```
- [ ]my_list.pop(30)
- [x]my_list.remove(30)
- [ ]del list[30]
- [ ]I don't know

##  4. How can you check if a key exists in a dictionary in Python 3?
Score: 1.0
```python
Let’s suppose that we want to check that the key banana exists in my_dict
my_dict = {'apple': 5, 'banana': 3, 'orange': 2}
```
-   [ ]my_dict.keys('banana')
-   [ ]`my_dict.exist('banana')
-   [x]'banana' in my_dict
-   [ ]I don't know

##  5. How can you access the value associated with a specific key in a dictionary in Python3 ? Select all the correct answers.
Score: 1.0
```python
let’s suppose that we want to get the value of the key age in the following dictionary:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```
-   [ ]my_dict.get('age')
-   [ ]my_dict.pop('age')
-   [ ]my_dict.remove('age')
-   [x]my_dict['age']
-   [ ]my_dict[age]
-   [ ]I don't know

##  6. How can you add an element to a set in Python3 ?
Score: 1.0
```python
Let’s suppose that we want to add the element 4 to the following set:
my_set = {1, 2, 3}
```
-   [ ]my_set.append(4)
-   [ ]my_set.extend(4)
-   [ ]my_set.insert(4)
-   [x]my_set.add(4)
-   [ ]I don't know

##  7. How can I get the value of element at a specific position (index) in a set in Python3 ?
Score: 1.0
```python
Let’s suppose that we have the following set and we want to access the element at index 0 (first element):
my_set = {1, 2, 3}
```
-   [ ]my_set[0]
-   [ ]my_set.show(0)
-   [x]I cannot because elements are unordered in sets.
-   [ ]I don't know

##  8. What's the other way to write an intersection in python for the following example ? Select the right answer
Score: 1.0
```python
if I want to get all the common elements from 2 or more sets in Python3, I can use intersection like that:
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)
```
-   [x]s1 & s2 & s3
-   [ ]There is no other way to do it.
-   [ ]s1 | s2 | s3
-   [ ]s1 - s2 - s3
-   [ ]I don't know

##  9. Select all the correct statements about Tuples in Python3.
Score: 1.0

-   [ ]Tuples are mutable data.
-   [x]Tuples are immutable data.
-   [ ]After creating a tuple, we can add another element to it.
-   [x]We can access to element of a tuple via their index, like that: my_tuple[index].
-   [x]Tuples can have elements of different data types.
-   [ ]I don't know

##  10. In Python3, which keyword is used to define a class?
Score: 1.0

Select the correct answer.

-   [ ]cls
-   [ ]self
-   [ ]init
-   [x]class
-   [ ]I don't know

##  11. What is the purpose of the __init__ method in a class in Python 3?
Score: 1.0

-   [x]It is a special method in Python classes that is automatically called when an object is created from the class. It is used to initialize the newly created object and perform any necessary setup or initialization tasks.
-   [ ]It is used to initialize the class itself and set its attributes.
-   [ ]It is a method used for destroying objects and freeing up memory resources.
-   [ ]I don't know

##  12. What is an object?
Score: 1.0

-   [ ]It is a variable that stores a single value or data.
-   [ ]It is a function that performs a specific task.
-   [x]It is an instance of a class that has properties and methods.
-   [ ]It is a keyword used for defining loops and conditional statements.
-   [ ]I don't know

##  13. Is the following statement correct ?
Score: 1.0

In Python, when members of a class are declared as public, they can be accessed conveniently from any section of the program. By default, all data members and member functions of a class are public, allowing straightforward accessibility to them from the class or any instance of it, throughout the program.

-   [x]True
-   [ ]False
-   [ ]I don't know

##  14. By convention, in Python3 how private attributes in a class are defined ?
Score: 1.0

Select the correct answer.

-   [ ]By prefixing the attribute name with a single underscore, such as _private_attribute.
-   [x]By prefixing the attribute name with a double underscore, such as __private_attribute.
-   [ ]By enclosing the attribute name within parentheses, such as (private_attribute).
-   [ ]By suffixing the attribute name with a single underscore, such as private_attribute_.
-   [ ]I don't know
