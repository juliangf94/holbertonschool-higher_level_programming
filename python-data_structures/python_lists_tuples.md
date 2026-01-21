# Python - Data Structures: Lists and Tuples
## General Concepts
### 1. What are Lists and How to Use Them
A **list** is a mutable, ordered collection of items. In Python, lists can contain different data types (heterogeneous) and are defined using square brackets `[]`.
* **Creation**: `my_list = [1, "Python", 3.14]`
* **Access**: 
    -   Elements are accessed via zero-based indexing. 
        -   `my_list[0]` returns `1`.
    -   Like strings, lists can be indexed and sliced:    
        -   `my_list[-1]` returns `3.14`.
        -   `my_list[-2:]` returns `Python, 3.14`. 
    -   Lists also support concatenation:    
        -   ```python
            >>> my_list + [36, 49, 64, 81, 100]
            [1, "Python", 3.14, 36, 49, 64, 81, 100]
            ```
* **Mutability**: 
    -    Unlike strings, you can modify elements: 
        -   `my_list[1] = "C is fun"`.
    -   You can use list.append() method to add new items:
        -   ```python
            >>> my_list.append(216)
            [1, "Python", 3.14, 216]
            ```
    -   Simple assignment never copies data. Any changes you make to a variable that was assigned a list will make the changes to that list:
        -   ```python
            >>> rgb = ["Red", "Green", "Blue"]
            >>> rgba = rgb
            >>> rgba.append("Alph")
            >>> rgb 
            ["Red", "Green", "Blue", "Alph"]
            ```
    -   It is possible to nest lists:
        -   ```Python
            >>> a = ['a', 'b', 'c']
            >>> n = [1, 2, 3]
            >>> x = [a, n]
            >>> x
            [['a', 'b', 'c'], [1, 2, 3]]
            >>> x[0]
            ['a', 'b', 'c']
            >>> x[0][1]
            'b'
            ```

### 2. What are the differences and similarities between strings and lists
Both are **Sequences**, but they handle memory and modifications differently.

| Feature | Strings | Lists |
| :--- | :--- | :--- |
| **Type** | Sequence of characters | Sequence of any object |
| **Mutability** | **Immutable** (cannot be changed) | **Mutable** (can be changed) |
| **Indexing/Slicing** | Yes | Yes |
| **Memory** | Fixed once created | Dynamic (can grow or shrink) |


###  3. What are the most common methods of lists and how to use them
* `append(x)`: Adds an item to the end of the list.
* `extend(iterable)`: Appends all items from another iterable to the list.
* `insert(i, x)`: Inserts an item at a given position `i`.
* `remove(x)`: Removes the first item from the list whose value is `x`.
* `pop([i])`: Removes and returns the item at the given position (default is the last item).
* `clear()` : Remove all items from the list. Similiar to del a[:].
* `index(x[, start[, end]])` : Return zero-based index of the first occurence of x in the list.
* `count(x)` : Return the number of times x appears in the list.
* `sort(*, key=None, reverse=False)`: Sorts the items of the list in place.
* `reverse()`: Reverses the elements of the list in place.
* `copy()` : Return a shallow copy of the list. Similiar to a[:].
Examples:
```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

###  4.  How to use lists as stacks and queues
* **Stacks (LIFO - Last In, First Out)**: 
    -   Use `append()` to push and `pop()` (with no index) to fetch the last element.
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
* **Queues (FIFO - First In, First Out)**: 
    -   While you can use `insert(0, x)` and `pop()`, it is inefficient for lists. For fast queues, use `collections.deque`.
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

###  5. What are list comprehensions and how to use them
List comprehensions provide a concise way to create lists without using multiple lines of `for` loops.
* **Syntax**: `[expression for item in iterable if condition]`

```python
>>> squares = []
>>> for x in range(10):             # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>>     squares.append(x**2)

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
This overwrites a variable named `x`, we can calculate the list of squares withouth any sides effects using:
```python
>>> squares = list(map(lambda x: x**2, range(10)))

>>> squares = [x**2 for x in range(10)]
```
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. 
For example, this listcomp combines the elements of two lists if they are not equal:
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
### Nested List Comprehensions
The initial  expression ina list comprehension can be another list comprehension:
Example 1:
```python
>>> matrix = [
>>>     [1, 2, 3, 4],
>>>     [5, 6, 7, 8],
>>>     [9, 10, 11, 12],
>>> ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Example 2:
```python
>>> transposed = []
>>> for i in range(4):
>>>     transposed.append([row[i] for row in matrix])

>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
You can use the `zip()` function for complex flow statements:
```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
###  6. What are tuples and how to use them
A **tuple** is an immutable sequence of items, typically used to store collections of heterogeneous data (data of different types).  
Unlike lists, they are defined using parentheses `()` instead of square brackets.
* **Immutability**: Once a tuple is created, its values cannot be modified, added, or removed.
* **Tuple Packing**: You can create a tuple by simply separating values with commas: `t = 12345, 54321, 'hello!'`.
* **Sequence Unpacking**: You can extract the values of a tuple back into individual variables: `x, y, z = t`.
* **Nestin**: Tuples may be nested:  
```python
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

###  7. When to use tuples versus lists
Choosing between a tuple and a list depends on whether the data needs to be changed and what kind of data it represents.

| Feature | Lists | Tuples |
| :--- | :--- | :--- |
| **Mutability** | **Mutable**: You can change, add, or delete items after creation. | **Immutable**: You cannot change the items once the tuple is defined. |
| **Data Type** | Usually **homogeneous** (items of the same type, like a list of names). | Usually **heterogeneous** (items of different types, like a coordinate `(x, y)`). |
| **Performance** | Slightly slower due to dynamic memory allocation. | Faster and more memory-efficient because they are fixed. |

**Rule of thumb**: Use **tuples** for fixed data that should not change (like database records or coordinates) and **lists** for collections that will grow or be reordered during the program's execution.

###  8. What is a sequence

In Python, a **sequence** is a generic term for an ordered collection of items where each item is identified by an index.
* **Types of Sequences**: The most common sequence types are **strings**, **lists**, and **tuples**.
* **Shared Features**: All sequences support basic operations like indexing (e.g., `seq[0]`), slicing (e.g., `seq[1:4]`), and checking for membership with the `in` operator.

### 9.  What is tuple packing
A **tuple** is an immutable sequence of items. They are defined using parentheses `()`.
* **Immutability**: Once a tuple is created, you cannot change its values.
* **When to use Tuples vs. Lists**: 
    * Use **Tuples** for fixed data (coordinates, RGB values, database records).
    * Use **Lists** for data that needs to be modified or reordered.

###  10.  What is sequence unpacking
* **Sequence**: A generic term for ordered collections (Strings, Lists, Tuples).
* **Tuple Packing**: Assigning multiple values into one tuple: `t = 1, 2, "three"`.
* **Sequence Unpacking**: Distributing tuple/list values into variables: `x, y, z = t`.

###  11.  What is the del statement and how to use it
The `del` statement is used to remove an item from a list by its index (unlike `remove()`, which uses the value).
* **Remove index**: `del a[0]`
* **Remove slice**: `del a[2:4]`
* **Delete variable**: `del a` (removes the entire variable from memory).

---

## Technical Summary Table

| Structure | Syntax | Mutable | Common Use Case |
| :--- | :--- | :--- | :--- |
| **List** | `[a, b]` | Yes | Dynamic collections, stacks. |
| **Tuple** | `(a, b)` | No | Fixed records, returning multiple values. |
| **String** | `"abc"` | No | Text processing. |

------------------------------------------------------------------------------------------------------
#   Quiz
##  Question #0
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[0]

1
2
[1]
[1, 2]
[1, 2, 3, 4]

##  Question #1
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[-1]

-1
2
4
[4, 3, 2, 1]

##  Question #2
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[-3]

-3
[4, 3]
2

##  Question #3
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> len(a)

2
4
6
8

##  Question #4
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)

2
5
6

##  Question #5
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[1:3]

[1, 2, 3]
[1, 2]
[2, 3]

##  Question #6
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a

[1, 2, 3, 4]
[1, 10, 3, 4]
[1, 2, 10, 4]
[1, 2, 10, 10]

##  Question #7
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> b

[1, 2, 3, 4]
[1]
1
a

##  Question #8
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a

[1]
[1, 2, 10, 4]
[1, 2, 3, 4]
a
b

##  Question #9
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b

[1]
[1, 2, 10, 4]
[1, 2, 3, 4]
a
b


------------------------------------------------------------------------------------------------------
#   Exercises
##  0-print_list_integer.py 
`0-main.py`
```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

```
`0-print_list_integer.py`
```python
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

```
Output:
```bash
1
2
3
4
5
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  1-element_at.py 
`1-main.py`
```python
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

```
`1-element_at.py`
```python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

```
Output:
```bash
Element at index 3 is 4
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  2-replace_in_list.py 
`2-main.py`
```python
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
```
`2-replace_in_list.py`
```python
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

```
Output:
```bash
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  3-print_reversed_list_integer.py 
`3-main.py`
```python
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
```
`3-print_reversed_list_integer.py`
```python
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        print("{:d}".format(i))

```
-   `my_list[::-1]` : We print from the back
    -   The first : indicates we start from the beginning
    -   The second : indicate we go to the end
    -   The -1 indicates we step backwards
Output:
```bash
5
4
3
2
1
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  4-new_in_list.py 
`4-main.py`
```python
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
```
`4-new_in_list.py`
```python
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list

```
Output:
```bash
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  5-no_c.py 
`5-main.py`
Write a function that removes all characters c and C from a string.
```python
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
```
`5-no_c.py `
```python
#!/usr/bin/python3
def no_c(my_string):
    new_list = [char for char in my_string if char != 'c' and char != 'C']
    return "".join(new_list)

```
-   [char for char in my_string if char != 'c' and char != 'C']
    -   `for char in my_string`: Python takes the string and breaks it: 'C', 'h', 'i', 'c', 'a', 'g', 'o'.
    -   `if char != 'c' and char != 'C'`: It only allows the characters that are noy 'c' and 'C'.
    -   `[char ...]`: The characters allowed are being saved inside the new list.
Output:
```bash
Best Shool
hiago
 is fun!
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  6-print_matrix_integer.py
Write a function that prints a matrix of integers
`6-main.py`
```python
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

```
`6-print_matrix_integer.py `
```python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()

```
Opcional:
`6-print_matrix_integer.py `
```python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))

```
Output:
```bash
1 2 3$
4 5 6$
7 8 9$
--$
$
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  7-add_tuple.py
Write a function that adds 2 tuples.
`7-main.py`
```python
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

```
`7-add_tuple.py `
```python
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    result = (a[0] + b[0], a[1] + b[1])
    return result

```
Output:
```bash
(89, 100)
(2, 89)
(1, 89)
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  8-multiple_returns.py
Write a function that returns a tuple with the length of a string and its first character.
`8-main.py`
```python
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
```
`8-multiple_returns.py`
```python
#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)

```
Output:
```bash
Length: 22 - First character: A
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  9-max_integer.py
Write a function that finds the biggest integer of a list.
`9-main.py`
```python
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
```
`9-max_integer.py`
```python
#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list :
        return None
    biggest = my_list[0]
    for x in my_list:
        if x > biggest:
            biggest = x
    return biggest

```
Output:
```bash
Max: 90
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  10-divisible_by_2.py 
Write a function that finds all multiples of 2 in a list.
`10-main.py`
```python
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
```
`10-divisible_by_2.py`
```python

```
Output:
```bash
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  11-delete_at.py
Write a function that deletes the item at a specific position in a list.
`11-main.py`
```python
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
```
`11-delete_at.py`
```python
def delete_at(my_list=[], idx=0):
    copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy

```
*   Cuando escribes copy[idx], le estás diciendo a Python: "Busca en la lista llamada copy el casillero que tiene el número de etiqueta idx".

Recuerda que en programación empezamos a contar desde 0.

Si idx es 3, Python va directo al cuarto casillero.
*   thon toma el valor de la variable element y lo mete en el casillero seleccionado.
Output:
```bash
[1, 2, 3, 5]
[1, 2, 3, 5]
```

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  12-switch.py
`12-switch.py`
```python

```
Output:
```bash
a=10 - b=89
```



pycodestyle 
