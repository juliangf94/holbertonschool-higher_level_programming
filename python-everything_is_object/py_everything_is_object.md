#   Python - Everything is object

---

# 🧠 Conceptos Fundamentales
##  What is an object?
Un objeto es una unidad de datos (valores) junto con funcionalidad (métodos) que reside en la memoria.  
En Python, cada objeto tiene tres características:
-   **Identity**: Su dirección de memoria (nunca cambia una vez creado).
-   **Type**: Define qué operaciones puede hacer (ej: int, str, list).
-   **Value**: El dato que contiene.

##  What is the difference between a class and an object (instance)?

-   **Class**: 
    +   Es el plano o molde (ej: el concepto de "Perro").

-   **Object/Instance**: 
    +   Es la realización concreta de ese molde (ej: tu perro "Firulais").  
    +   La clase define la estructura, el objeto es el ejemplar que vive en la memoria.


##  What is a reference?
Una referencia es un nombre (variable) que apunta a un objeto en la memoria.  
Cuando haces `a = 1`, la variable `a` no "contiene" el `1`, sino que **apunta** a la ubicación de memoria donde está el objeto 1.

##  What is an assignment?
Es la acción de unir un nombre (variable) con un objeto. Se usa el operador =. Si el nombre ya existía, simplemente se cambia el "cable" para que apunte al nuevo objeto.

##  What is an alias?
Un alias ocurre cuando dos o más variables apuntan al mismo objeto en memoria.
```Python
l = [1, 2]
m = l  # 'm' es un alias de 'l'
```
Como ambos apuntan al mismo lugar, si cambias `l`, `m` también cambia.

---

# 🛠️ Mutabilidad vs Inmutabilidad
##  What is the difference between immutable object and mutable object
-   **Mutable**: 
    +   Objetos que pueden cambiar su contenido sin cambiar su identidad (dirección de memoria).
-   **Immutable**: 
    +   Objetos que no pueden cambiarse una vez creados.  
    +   Si intentas modificarlo, Python crea un objeto nuevo con el nuevo valor.

##  What are the built-in mutable types
##  What are the built-in immutable types
| Mutable types (Cambiables) | Immutable Types (Fijos) |
| :... | :... |
| list | int, float, complex |
| dict | str |
| set | tuple |
| bytearray | bool, frozenset, bytes |

##  How to know if two variables are linked to the same object / How to know if two variables are identical
-   Se utiliza el operador `is`. 
    +   Este operador compara las direcciones de memoria (IDs), no los valores.
-   `a is b` devuelve `True` si ambos apuntan al mismo objeto.

##  How to display the variable identifier (which is the memory address in the CPython implementation)
Se usa la función integrada `id()`.  
En **CPython** (la versión estándar de Python), este número es la dirección de memoria del objeto.

```Python
a = "Holberton"
print(id(a))  # Salida: 139963852150448 (ejemplo)
```

---

# 🚀 Paso de Variables a Funciones

##  How does Python pass variables to functions
Python utiliza un mecanismo llamado **"Pass by object reference"** (o Pass by assignment).
-   Si pasas un objeto **mutable** (como una lista) y lo modificas dentro de la función, el cambio **afecta** a la variable original fuera de la función.
-   Si pasas un objeto **inmutable** (como un entero) e intentas modificarlo, la función creará una copia local y **no afectará** al original.


```python
# CASO 1: Inmutable (int)
a = 1
b = a  # b apunta al mismo 1
a = 2  # a ahora apunta a un nuevo objeto 2. b sigue apuntando al 1.

# CASO 2: Mutable (list)
l = [1, 2, 3]
m = l  # m apunta a la MISMA lista que l
l[0] = 'x'  # Modificas el contenido del objeto. Como m apunta al mismo objeto, m refleja el cambio.
```

---
---
#   Exercise

##  0. Who am I?
What function would you use to print the type of an object?
Write the name of the function in the file, without `()`.

`0-answer.txt`
```
type
```

```bash
echo "type" > 0-answer.txt 
``` 
### **Logica**
-   **Function**: `type(object)`
-   **Purpose**: Returns the type object of the passed argument.
-   **Example:**
```Python
a = 7
type(a)
Output: <class 'int'>
s = "Holberton"
type(s)
Output: <class 'str'>
```

---

##  1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

`1-answer.txt`
```
id
```

```bash
echo "id" > 1-answer.txt
```

### **Logica**
-   **Function**: `id(obj)`

-   **Behavior**: It returns an integer which is guaranteed to be unique and constant for this object during its lifetime.

-   **Memory Link**: In the standard Python implementation (CPython), `id(x)` is the actual memory address where `x` is stored.


---

##  2. Right count
In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```

`2-answer.txt`
```
No
```

```bash
echo "No" > 2-answer.txt
```

### **Logica**
In Python, integers are immutable.  
When you assign `89` to `a`, it points to an integer object with the value 89.  
When you assign `100` to `b`, it points to a completely different integer object.  
If you were to run `a is b` in the interpreter, it would return `False`.

---

##  3. Right count =
In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
a = 89
b = 89
```

`3-answer.txt`
```
Yes
```

```bash
echo "Yes" > 3-answer.txt
```

### **Logica**
Python (specifically **CPython**) uses a memory optimization technique called **Integer Interning**.

Python pre-allocates an array of integer objects for all integers between -5 and 256. When you assign a value within this range to a variable, Python doesn't create a new object; it simply points the variable to the existing object in that pre-allocated range.

Since 89 falls within this range, both a and b point to the exact same memory address.

---

##  4. Right count =
In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
a = 89
b = a
```

`4-answer.txt`
```
Yes
```

```bash
echo "Yes" > 4-answer.txt
```

### **Logica**
When you perform the operation `b = a`, you are not creating a copy of the object `89`.  
Instead, you are telling the variable b to point to the exact **same memory address** that `a` is currently pointing to.
In Python terminology, `b` becomes an alias for `a`.  
Since they both refer to the same object in memory, `a is b` will return `True`.

---

##  5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.

```python
a = 89
b = a + 1
```

`5-answer.txt`
```
No
```
```bash
echo "No" > 5-answer.txt
```

### **Logica**
When you execute `b = a + 1`, Python first evaluates the expression on the right side.
1. It takes the value of `a` **(89)**.
2. It adds 1, resulting in 90.
3. It creates (or references) an integer object for **90** and points `b` to it.

Since **89** and **90** are two different mathematical values, they are represented by two different objects in memory.  
Therefore, `a` and `b` point to different objects.  
If you ran `a is b`, it would return `False`.

---

##  6. Is equal
What do these 3 lines print?

```python
s1 = "Best School"
s2 = s1
print(s1 == s2)
```

`6-answer.txt`
```
True
```
```bash
echo "True" > 6-answer.txt
```
### **Logica**
In Python, the `==` operator checks for **value equality**.  
It asks: "Is the content of `s1` the same as the content of `s2`?"
Since you assigned `s2 = s1`, both variables refer to the exact same string content.  
Therefore, the statement `s1 == s2` is true.  
Even if they were different objects in memory (which they aren't in this case due to the assignment), as long as the text inside is identical, `==` will always return `True`.

---

##  7. Is the same
What do these 3 lines print?
```python
s1 = "Best"
s2 = s1
print(s1 is s2)
```

`7-answer.txt`
```
True
```
```bash
echo "True" > 7-answer.txt
```
### **Logica**
When you execute `s2 = s1`, you are creating an **alias**.  
You are telling Python that the name `s2` should point to the **exact same object** in memory that `s1` is already pointing to.
Unlike `==` (which checks if the text is the same), the `is` operator checks if both variables share the same `id()`.  
Since they point to the same memory address, the result is `True`.

---

##  8. Is really equal
What do these 3 lines print?
```python
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
```

`8-answer.txt`
```
True
```
```bash
echo "True" > 8-answer.txt
```
### **Logica**
In Python, the `==` operator is used for **value comparison**.  
It looks at the data stored inside the objects.  
Since the string `"Best School"` in `s1` is identical character-for-character to the string `"Best School"` in `s2`, the expression evaluates to `True`.
It doesn't matter if they are the same object in memory or two different objects; as long as their contents match, `==` returns `True`.

---

##  9. Is really the same
What do these 3 lines print?
```python
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
```

`9-answer.txt`
```
True
```
```bash
echo "True" > 9-answer.txt
```
### **Logica**
Python uses a memory optimization called `String Interning`.
When Python sees two identical literal strings (especially those containing only letters, numbers, or underscores), it often stores only **one copy** in memory and points both variables to it to save space.
-   Note: 
    +   In modern versions of Python (like 3.8+), this interning of literals happens during the compilation of the script or the interactive session. 
    +   If you ran `id(s1)` and `id(s2)`, you would see they are identical.

---

##  10. And with a list, is it equal
What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)
```

`10-answer.txt`
```
True
```
```bash
echo "True" > 10-answer.txt
```
### **Logica**
The `==` operator in Python performs a **value comparison**.  
For lists, Python iterates through both objects and checks if:
1.   They have the same number of elements.
2.   Each corresponding element is equal (`l1[0] == l2[0]`, etc.).

Since both lists contain `[1, 2, 3]`, they are considered equal in value.

---

##  11. And with a list, is it the same
What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)
```

`11-answer.txt`
```
False
```
```bash
echo "False" > 11-answer.txt
```
### **Logica**
Unlike small integers or short strings (which Python sometimes "interns" or caches to save memory), **lists are mutable objects**.
Every time you use the square bracket notation `[]` to create a list, Python allocates a new block of memory for that specific list.  
Even if the contents are identical to another list, they are two distinct objects living at different addresses.  
Therefore, `l1 is l2` is false.

---

##  12. And with a list, is it really equal
What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```
`12-answer.txt`
```
True
```
```bash
echo "True" > 12-answer.txt
```
### **Logica**
When you run `l2 = l1`, you are making `l2` point to the exact same list object as `l1`.  
Since they are the same object, they naturally have the same values (`[1, 2, 3]`).
Because the `==` operator checks if the contents of the two lists are the same, and they are, the result is `True`.

---

##  13. And with a list, is it really the same
What do these 3 lines print?
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
```
`13-answer.txt`
```
True
```
```bash
echo "True" > 13-answer.txt
```
### **Logica**
When you execute `l2 = l1`, you are not creating a new list.  
You are creating an **alias**.  
This means `l1` and `l2` are now two different names for the **exact same object** in memory.
The `is` operator checks if the memory addresses (`id`) are identical.  
Since both variables point to the same block of memory, the result is `True`.

---

##  14. List append
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

`14-answer.txt`
```
[1, 2, 3, 4]
```
```bash
echo "[1, 2, 3, 4]" > 14-answer.txt
```
### **Logica**
When you execute `l2 = l1`, you aren't creating a copy; you are creating an **alias**.  
Both `l1` and `l2` point to the **exact same memory address**.
Since lists are mutable, the method `.append(4)` modifies the existing object in memory.  
Because `l2` is just another name for that same object, when you print `l2`, you see the updated list including the `4`.

---

##  15. List add
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
`15-answer.txt`
```
[1, 2, 3]
```
```bash
echo "[1, 2, 3]" > 15-answer.txt
```
### **Logica**
Here is the step-by-step breakdown of what happened in memory:
1.  `l1 = [1, 2, 3]`: 
    -   An object is created in memory. `l1` points to it.
2.  `l2 = l1`: 
    -   `l2` now points to the same object.
3.  `l1 = l1 + [4]`: 
    -   This is the key. The `+` operator for lists **creates a brand new list** by concatenating the two.
        +   Python calculates `[1, 2, 3] + [4]`, resulting in a new object `[1, 2, 3, 4]`.
        +   `l1` is then **reassigned** to point to this new object.
        +   Crucially, `l2` is still pointing to the **original** object `[1, 2, 3]`.

If the code had used `l1 += [4]` or `l1.append(4)`, the result would have been different because those operations modify the object in place (in most cases).  
But with `l1 = l1 + [4]`, you broke the link between `l1` and `l2`.

---

##  16. Integer incrementation
What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

`16-answer.txt`
```
1
```
```bash
echo "1" > 16-answer.txt
```
### **Logica**
Here is exactly what happens in memory:
1.  **Integers are immutable**: 
    -   You cannot change the value of an integer object once it is created.
2.  **Pass by Object Reference**: 
    -   When you call `increment(a)`, the local variable `n` inside the function starts pointing to the same object as `a` (the integer `1`).
3.  **Reassignment**: 
    -   Inside the function, `n += 1` is equivalent to `n = n + 1`.
    -   This creates a new integer object (+ ) and points the local variable `n` to it.
4.  **No effect on the caller**: 
    -   The variable `a` outside the function is still pointing to the original object `1`.
    -   Since `n` was just a local name, its reassignment doesn't affect `a`.

---

##  17. List incrementation
What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
`17-answer.txt`
```
[1, 2, 3, 4]
```
```bash
echo "[1, 2, 3, 4]" > 17-answer.txt
```
### **Logica**
Here is the step-by-step breakdown of the memory logic:
1.   **Lists are Mutable**: 
    -   Unlike integers, you can change the content of a list object without creating a new one.
2.   **Aliasing in Functions**: 
    -   When you call `increment(l)`, the local variable `n` inside the function becomes a reference to the **exact same list object** in memory that `l` points to.
3.   **In-place Modification**: 
    -   The `.append(4)` method modifies the object itself.
    -   It doesn't create a new list; it just adds an element to the existing memory block.
4.   **Global Impact**: 
    -   Since `l` and `n` both point to that same memory block, when the function finishes and you print `l`, you see the modification made by the function.

---

##  18. List assignation
What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
`18-answer.txt`
```
[1, 2, 3]
```
```bash
echo "[1, 2, 3]" > 18-answer.txt
```
### **Logica**
Here is the logic of what happened in memory during the function call:
1.  **Initial State**: 
    -   `l1` points to Object A `[1, 2, 3]`.
    -   `l2` points to Object B `[4, 5, 6]`.
2.  **Function Call**: 
    -   When `assign_value(l1, l2)` is called, the local variable `n` points to Object A, and the local variable `v` points to Object B.
3.  **The Reassignment**: 
    -   Inside the function, `n = v` tells the **local name** `n` to stop pointing at Object A and start pointing at Object B.
        +   This **does not change** Object A itself.
        +   This **does not change** what the global variable `l1` is pointing to.
4.  **Function Exit**: 
    -   Once the function finishes, the local variable `n` is destroyed.
    -   The global variable `l1` still points to its original Object A `[1, 2, 3]`.
    -   **Note**: 
        +   If the function had been `n[0] = v[0]`, then `l1` would have changed because that is a mutation of the object.
        +   But `n = v` is just moving a local pointer.

---

##  19. Copy a list object
Write a function `def copy_list(a_list):` that returns a **copy** of a list.
-   The input list can contain any type of objects
-   Your file should be maximum 3-line long (no documentation needed)
-   You are not allowed to import any module
guillaume@ubuntu:~/$ cat 19-main.py
```python
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

```
`19-copy_list.py`
```python
#!/usr/bin/python3
def copy_list(a_list):
    return a_list[:]
```

### **Output**
```bash
guillaume@ubuntu:~/$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/$ 
No test cases needed
```
### **Logica**
-   **Slicing (`[:]`)**: 
    +   When you use `a_list[:]`, Python creates a "shallow copy" of the entire list.
    +   It starts from the beginning and goes to the end, putting all elements into a **brand new list object**.
-   **Identity Check**: 
    +   Because a new object is created, `new_list is a_list` will be `False`, even though `new_list == a_list` is `True`.

**Alternative**
```python
#!/usr/bin/python3
def copy_list(a_list):
    return list(a_list)
```

---

##  20. Tuple or not?
```python
a = ()
```
Is a a tuple? Answer with Yes or No.

`20-answer.txt`
```
Yes
```
```bash
echo "Yes" > 20-answer.txt
```
### **Logica**
In Python, parentheses `()` are the standard syntax used to define a **tuple**.
-   `a = ()` creates an empty tuple.
-   Tuples are **immutable**, meaning once created, you cannot add, remove, or change their elements.
-   You can verify this in your terminal by running `type(())`, which will return `<class 'tuple'>`.

---

##  21. Tuple or not?
```python
a = (1, 2)
```
Is a a tuple? Answer with Yes or No.

`21-answer.txt`
```
Yes
```
```bash
echo "Yes" > 21-answer.txt
```
### **Logica**
In Python, multiple values separated by commas and enclosed in parentheses `()` create a **tuple**.  
In fact, it is actually the **comma** that defines the tuple in most cases, but the parentheses are the standard way to represent them visually and syntactically.
Since `(1, 2)` contains two elements separated by a comma, it is a valid tuple object.
---

##  22. Tuple or not?
```python
a = (1)
```
Is a a tuple? Answer with Yes or No.

`22-answer.txt`
```
No
```
```bash
echo "No" > 22-answer.txt
```
### **Logica**
-   In Python, parentheses `()` are used both for **tuples** and for grouping **mathematical expressions** (operator precedence).
    +   When you write `a = (1)`, Python interprets the parentheses as a **grouping operator**. 
        *   It simply evaluates the expression inside (`1`) and assigns that integer to `a`.
    +   To define a tuple with a **single element**, you must include a trailing comma: `a = (1,)`.
```python
>>> a = (1)
>>> type(a)
<class 'int'>

>>> b = (1,)
>>> type(b)
<class 'tuple'>
```

---

##  23. Tuple or not?
```python
a = (1, )
```
Is a a tuple? Answer with Yes or No.

`23-answer.txt`
```
Yes
```
```bash
echo "Yes" > 23-answer.txt
```
### **Logica**
-   In Python, the **comma** is the actual constructor for a tuple, not necessarily the parentheses.
    +   By adding the trailing comma inside the parentheses, you are explicitly telling Python: "This is not just a grouped integer; this is a collection containing one element."
    +   You could even write `a = 1,` without any parentheses at all, and Python would still recognize it as a tuple.
```python
>>> a = (1, )
>>> type(a)
<class 'tuple'>
>>> len(a)
1
```

---

##  24. Who I am?
What does this script print?
```python
a = (1)
b = (1)
a is b
```

`24-answer.txt`
```
True
```
```bash
echo "True" > 24-answer.txt
```
### **Logica**
Here is the step-by-step logic:
1.  **Not a Tuple**: 
-   `(1)` is just an integer `1` wrapped in parentheses for grouping.
    +   It is **not** a tuple because it lacks a trailing comma.
2.  **Integer Interning**: 
-   Because `a` and `b` are both the integer `1`, Python uses its internal optimization (interning) for small integers (range -5 to 256).
3.  **Identity**: 
-   Since both variables refer to the same pre-allocated integer object `1` in memory, the `is` operator returns `True`.
If the code had been `a = (1,)` and `b = (1,)`, the answer would have been `False` because those would be two distinct tuple objects.

---

##  25. Tuple or not
What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```

`25-answer.txt`
```
False
```
```bash
echo "False" > 25-answer.txt
```
### **Logica**
While tuples are immutable (their content cannot change), Python handles them differently than small integers or short string literals:
1.  **New Objects**: 
-   Every time you define a tuple literal like `(1, 2)`, Python usually allocates a **new** tuple object in memory.
2.  **No Automatic Interning**: 
-   Unlike integers between -5 and 256, Python does not automatically "intern" or cache most tuples to save space.
3.  **Identity vs. Equality**: 
-   If you ran `a == b`, the result would be `True` because their values match. 
    +   However, because they are stored at two different memory addresses, `a is b` returns `False`.

---

##  26. Empty is not empty
What does this script print?
```python
a = ()
b = ()
a is b
```

`26-answer.txt`
```
True
```
```bash
echo "True" > 26-answer.txt
```
### **Logica**
Empty tuples are a special case in CPython:
1.  **Immutability**: 
    +   Since a tuple is immutable, an empty tuple `()` can never change its state.
2.  **Memory Optimization**: 
    +   To save memory, Python creates a **single, global instance** of an empty tuple.
3.  **The Singleton Pattern**: 
    +   Every time you "create" an empty tuple `()`, Python simply points your variable to that one pre-existing object in memory.

Since `a` and `b` both point to this same internal singleton, `a is b` evaluates to `True`.  
Note that this **does not** apply to empty lists `[]`, because lists are mutable and each must be a unique object.

---

##  27. Still the same?
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

`27-answer.txt`
```
No
```
```bash
echo "No" > 27-answer.txt
```
### **Logica**
When you use the expression `a = a + [5]`, Python performs the following steps:
1.   **Evaluation**: 
    +   It takes the current list `a` ([1, 2, 3, 4]) and the new list ([5]).
2.   **Creation**: 
    +   The `+` operator creates a **brand new list object** in memory containing `[1, 2, 3, 4, 5]`.
3.  **Reassignment**: 
    +   The variable `a` is then updated to point to the memory address of this **new** object.

Since a new object was created, its memory address (returned by `id(a)`) will be different from the original one.
    +   **Note**: 
        *   If the code had used `a.append(5)` or `a += [5]`, the id would have remained the same because those operations modify the existing list in place.

---

##  28. Same or not?
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

`28-answer.txt`
```
Yes
```
```bash
echo "Yes" > 28-answer.txt
```
### **Logica**
For **lists**, the `+=` operator is implemented using the `__iadd__` method, which is functionally equivalent to `a.extend([4])`.
1.  **In-place Operation**: 
    +   Unlike `a = a + [4]` (which creates a brand new object), `a += [4]` modifies the original list object in memory.
2.  **Memory Address**: 
    +   Because the object is modified in place rather than replaced, its memory address (the `id`) remains exactly the same.
-   **Note**: 
    +   This behavior is specific to mutable objects. 
    +   If a were an immutable tuple, `a += (4,)` would create a new object and the id would change!

---

##  

```python

```
``
```

```
```bash

```
### **Logica**
