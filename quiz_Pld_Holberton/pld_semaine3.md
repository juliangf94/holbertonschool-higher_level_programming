#   PLD
##  1. Is there a do...while loop in Python?
No. Python does not have a built-in do...while structure. 
To mimic it, you usually use a while True loop with a break condition at the end.

##  2. What is a docstring and how do you write one?
A docstring (documentation string) is a string literal that appears as the first statement in a module, function, class, or method definition. 
It is used to explain what the code does. You write it using triple quotes (""" or ''').

```Python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```
##  3. Is there a switch...case in Python?
Historically, no. 
However, since Python 3.10, a feature called Structural Pattern Matching was introduced using match and case. 
Before 3.10, developers used if-elif-else or dictionaries to handle multiple cases.

##  4. How to write a function with multiple cases?
You use if, elif (short for else if), and else.

```Python
def check_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")
```        
##  5. import module vs from module import *
import module: 
    Imports the whole module. 
    You must access functions using the dot notation (module.function()). 
    This is safer and prevents naming conflicts.

from module import *: 
    Imports every public function/variable directly into your workspace. 
    This is generally discouraged because it can overwrite existing names in your script and makes code harder to read.

##  6. What is the correct file extension for Python files?
The extension is .py.

##  7. What does the keyword break do?
It terminates the current loop (for or while) and jumps to the next statement immediately after the loop.

##  8. What does the keyword continue do?
It skips the rest of the current iteration of the loop and moves back to the top of the loop for the next cycle.

##  9. What does the keyword pass do?
It is a null operation. 
It does nothing. 
It is used as a placeholder when a statement is syntactically required but you don’t want to execute any code (like in an empty function or class).

##  10. What is the range function and its parameters?
It generates a sequence of numbers. Parameters: range(start, stop, step)

    -   start (optional, default 0): The beginning of the sequence.
    -   stop (required): The number at which to stop (not included).
    -   step (optional, default 1): The increment between numbers.

##  11. What does a function return if there is no return statement?
It returns None.

##  12. What is an f-string in Python and how do you use it?
Introduced in Python 3.6, f-strings (formatted string literals) allow you to embed expressions inside string literals using curly braces {}. 
You prefix the string with an f. 
```Python
name = "Julian"; 
print(f"Hello, {name}")
```
##  13. Can we increment and decrement in python using ++ or -- respectively?
No. Python does not have increment/decrement operators like C. You must use 

```Python
i += 1 
i -= 1
```
##  14. in a very simple way what is a module in python?
In simple terms, a module is just a file containing Python code (functions, variables, etc.) that you can use in other Python files.

##  15. What is a Python traceback?
A traceback is the report Python gives you when an error occurs. 
It shows the "trail" of where the error happened, including the file name, the line number, and the sequence of function calls that led to the problem.

##  16. How to prevent code from executing when imported?
You wrap the executable code in an if __name__ == "__main__": block.

```Python
if __name__ == "__main__":
    # This only runs if you execute the script directly
    my_function()
```
