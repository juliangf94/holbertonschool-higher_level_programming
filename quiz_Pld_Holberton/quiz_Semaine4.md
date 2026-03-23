#   Quiz  semaine 4
##   0. Which of the following is used to define a block of code?
Score: 0.0

[ ]parentheses
[ ]key
[ ]brackets
[X]indentation
[ ]I don't know

##   1. What is indexing?
Score: 1.0

[x]It means referring to an element of an iterable by its position within the iterable.
[ ]It means getting a subset of elements from an iterable based on their indices.
[ ]It means assigning a specific position to a value in an iterable.
[ ]It means getting a set of values from a list.
[ ]I don't know

##   2. What will be the output of the following code snippet?
Score: 1.0
```python
a = [1, 2, 3] 
a = tuple(a) 
a[0] = 2 
print(a) 
```
[ ][2, 2, 3]
[ ](2, 2, 3)
[ ](1, 2, 3)
[x]Throws exception
[ ]I don't know

##   3. Python supports the creation of anonymous functions at runtime, using a construct called
Score: 1.0

[ ]kwargs
[ ]anonymous
[x]lambda
[ ]variadic
[ ]def
[ ]I don't know

##   4. What do these lines print?
Score: 1.0

```python
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "James" } ] } 
>>> a.get('friends')[-1].get("name")
```
[ ]89
[ ][{'id':82, 'name':"Bob"}, {'id':83, 'name': "James"}]
[x]'James'
[ ]'Bob'
[ ]Nothing
[ ]I don't know

##   5. What will be the output of the following code?
Score: 1.0
```python
x = 'abcd'
for i in range(len(x)):
    print(i)
```
[ ]Throws exception
[ ]1 2 3 4
[ ]a b c d
[x]0 1 2 3
[ ]I don't know

##   6. What do these lines print?
Score: 1.0
```python
>>> def my_function(counter=89): 
>>>     print(f"Counter: {counter}")
>>>       
>>> my_function(12)
```
[x]Counter: 12
[ ]Counter: 89
[ ]Counter: 101
[ ]Throws exception
[ ]I don't know

##   7. What will be the output of the following Python program?
Score: 0.0
```python
def foo(x): 
    x[0] = ['def']
    x[1] = ['abc'] 
    return id(x) 

q = ['abc', 'def'] 
print(id(q) == foo(q)) 
```
[ ]None
[ ]False
[x]True
[ ]Throws exception
[ ]I don't know

*   

##   8. Which of the following are immutable?
Score: 1.0

Please select all valid answers

[ ]lists
[x]integers
[ ]dictionaries
[ ]sets
[x]strings
[x]tuples
[x]booleans
[x]floats
[ ]I don't know

*   Cuando decimos que un objeto es inmutable, significa que una vez que se crea en la memoria, su contenido no puede ser cambiado jamás.
Si "modificas" una variable inmutable, lo que Python hace en realidad es crear un objeto completamente nuevo en otra dirección de memoria y apuntar la variable hacia allá. El valor viejo se queda solo y luego el "Garbage Collector" lo borra.
*   

##   9. What is an Exception?
Score: 1.0

[x]Is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions
[ ]Is an event, which occurs when a condition was not met.
[ ]Is an event, which occurs when the user makes a mistake using the program.
[ ]Is an event, which occurs when a function did not receive the parameters needed to execute properly.
[ ]Is an edge case.
[ ]I don't know

##  10. What is slicing?
Score: 1.0

[ ]It means referring to an element of an iterable by its position within the iterable.
[x]It means getting a subset of elements from an iterable based on their indices.
[ ]It means assigning a specific position to a value in an iterable.
[ ]It means getting a set of values from a dictionary.
[ ]I don't know

##   11. What will be the output of the following code snippet?
Score: 1.0
```python
example = ["Sunday", "Monday", "Tuesday", "Wednesday"] 
print(example[-3:-1])
```
[x]["Monday", "Tuesday"]
[ ]["Sunday", "Monday"]
[ ]["Monday", "Tuesday", "Wednesday"]
[ ]["Wednesday", "Monday"]
[ ]Throws exception
[ ]I don't know

##   12. What module can be used to handle command line arguments?
Score: 1.0

[x]sys
[ ]calc
[ ]argv
[ ]argc
[ ]lambda
[ ]filter
[ ]shell
[ ]terminal
[ ]None
[ ]I don't know

*   El módulo sys (específicamente sys.argv) es el estándar para leer lo que el usuario escribe al ejecutar el script en la terminal.  

##   13. Which of the following statements are used in Exception Handling?
Score: 1.0

Please select all valid answers

[x]try
[x]except
[x]finally
[ ]catch
[x]else
[ ]I don't know

*   `else`: Mantén el bloque try lo más pequeño posible. Solo mete ahí la línea que realmente puede fallar. Todo el código que dependa de que esa línea haya tenido éxito, debe ir en el else.

##   14. What is the return value of a function that has no return statement in it?
Score: 1.0

[ ]An integer
[ ]Always 0
[ ]Always 1
[ ]Void
[ ]True
[ ]False
[ ]A boolean
[x]None
[ ]I don't know
