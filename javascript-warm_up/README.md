# JavaScript - Warm-up

## Description
This project is part of the Higher Level Programming curriculum at Holberton School. It serves as an introductory "warm-up" to JavaScript, focusing on the basics of the language, asynchronous execution (Node.js), and the transition from C to a high-level, prototype-based language.

## Learning Objectives
* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables using `let` and `const`
* How to use `if`, `if ... else` statements
* How to use `switch` statements
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* How to use functions
* How to use arguments passed to a script
* How to work with Objects and Arrays
* How to use `map`, `filter`, and `reduce` (Bonus tasks)

## Requirements
* **Operating System:** Ubuntu 20.04 LTS
* **Node.js Version:** 14.x
* **Style Guide:** [semistandard](https://github.com/standard/semistandard) (Version 16.x)
* **Execution:** All files must be executable and start with `#!/usr/bin/node`

## Environment Setup
To install Node.js 14 and the `semistandard` linter:

```bash
curl -sL [https://deb.nodesource.com/setup_14.x](https://deb.nodesource.com/setup_14.x) | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard --global
```

## Project Structure
| File | Task | Description | 
| :... | :... | :... |
| 0-javascript_is_amazing.js | 0. First constant | Prints "JavaScript is amazing" |
| 1-multi_languages.js | 1. Three languages | Prints 3 specific lines about C, Python, and JS |
| 2-arguments.js | 2. Arguments | Prints a message based on the number of arguments |
| 3-value_argument.js | 3. Value of my argument |Prints the first argument passed to the script |
| 4-concat.js | 4. Create a sentence | Concatenates two arguments in a specific format |
| 5-to_integer.js | 5. An Integer | Attempts to convert an argument to an integer |
| 6-multi_languages_loop.js | 6. Loop to languages | Prints 3 lines using an array and a loop |
| 7-multi_c.js | 7. I love C | Prints "C is fun" X times |
| 8-square.js | 8. Square | Prints a square of characters 'X' of size N |
| 9-add.js | 9. Add | Defines a function add(a, b) |
| 10-factorial.js | 10. Factorial | Computes a factorial recursively |
| 11-second_biggest.js | 11. Second biggest!Finds the second largest integer in a list |
| 12-object.js | 12. Object | Updates a property value in a constant object |
| 13-add.js | 13. Add file | Exports a function for external use |

## Usage
Ensure the script is executable:
```Bash
chmod +x <filename>.js
./<filename>.js [arguments]
```
Example:
```Bash
./7-multi_c.js 3
# Output:
# C is fun
# C is fun
# C is fun
```
## Author
-   Julian Gonzalez - GitHub Profile
