1. Why JavaScript programming is amazing
JavaScript es increíble porque es el único lenguaje nativo que entienden los navegadores. Permite crear interfaces altamente interactivas, pero gracias a Node.js, también se puede usar en el servidor (back-end). Es versátil, tiene una comunidad gigantesca y permite manejar operaciones asíncronas de forma muy eficiente.

2. How to run a JavaScript script
En el entorno de Holberton (Ubuntu), se ejecuta usando Node.js desde la terminal:

Bash
node nombre_del_archivo.js
Para que sea ejecutable como un script directo (usando ./archivo.js), la primera línea debe ser el shebang: #!/usr/bin/node.

3. How to create variables and constants
Se crean utilizando las palabras clave let, const o var seguidas del nombre:

JavaScript
let myVariable = 10;
const myConstant = 3.14;
4. What are differences between var, const and let
var: Forma antigua. Tiene scope de función y permite re-declaración. (Evitar su uso en JS moderno).

let: Scope de bloque {}. Se puede re-asignar pero no re-declarar en el mismo scope.

const: Scope de bloque. No se puede re-asignar ni re-declarar. Es ideal para valores que no deben cambiar.

5. What are all the data types available in JavaScript
JavaScript tiene tipos Primitivos y Objetos:

Primitivos: Number, String, Boolean, Undefined, Null, Symbol y BigInt.

Objetos: Object (incluye arrays, funciones y diccionarios/objetos literales).

6. How to use the if, if ... else statements
Controlan el flujo según una condición booleana:

JavaScript
if (a > b) {
  console.log("A es mayor");
} else {
  console.log("B es mayor o igual");
}
7. How to use comments
Línea única: // esto es un comentario

Multi-línea: /* esto es un comentario largo */

8. How to affect values to variables
Se utiliza el operador de asignación =. También existen operadores compuestos como +=, -=, *=.

9. How to use while and for loops
for: Ideal cuando sabes cuántas veces iterar.

JavaScript
for (let i = 0; i < 5; i++) { /* código */ }
while: Itera mientras una condición sea verdadera.

JavaScript
while (condicion) { /* código */ }
10. How to use break and continue statements
break: Sale completamente del bucle actual.

continue: Salta la iteración actual y pasa a la siguiente.

11. What is a function and how do you use functions
Una función es un bloque de código diseñado para realizar una tarea específica. Se define con function y se invoca con ().

JavaScript
function sayHello (name) {
  return "Hello " + name;
}
console.log(sayHello("Julian"));
12. What does a function that does not use any return statement return
Si una función no tiene un return explícito, devuelve undefined por defecto.

13. Scope of variables
Es el contexto donde una variable es accesible:

Global: Accesible en todo el script.

Local (Función): Accesible solo dentro de la función donde se creó.

Bloque: (Solo con let y const) Accesible solo dentro de { } (como en un if o un for).

14. What are the arithmetic operators and how to use them
+ (Suma), - (Resta), * (Multiplicación), / (División).

% (Módulo/Resto), ** (Exponenciación), ++ (Incremento), -- (Decremento).

15. How to manipulate dictionary (Objects)
En JS los diccionarios son Objetos. Se manipulan mediante clave-valor:

JavaScript
const user = { name: "Julian", age: 31 };
console.log(user.name); // Notación de punto
user['age'] = 32;       // Notación de corchetes
16. How to import a file
En Node.js (versión 14, como requiere Holberton), se usa comúnmente require:

JavaScript
const myModule = require('./otro_archivo.js');
💡 Tips extra para tu proyecto de Holberton:
Shebang: No olvides que todos tus archivos deben empezar con #!/usr/bin/node.

Semistandard: Recuerda usar punto y coma ; al final de cada sentencia. Es una regla estricta de este proyecto.

Permisos: Usa chmod +x filename.js para hacerlos ejecutables antes de subirlos.

---
---

#   Quiz
##  Question #0
Does Javascript have `String` as a native datatype?

[x] Yes

[ ] No

### **Explicación**: 
En JavaScript, `String` es uno de los tipos de datos primitivos (junto con `Number`, `Boolean`, `Null`, `Undefined`, `Symbol` y `BigInt`).  
Aunque JS permite usar métodos sobre strings como si fueran objetos, el motor los trata internamente como valores primitivos por eficiencia.

---

##  Question #1
Does Javascript have `Array` as a native datatype?

[x] Yes

[ ] No

### **Explicación**:
Aunque técnicamente un `Array` es un objeto `(typeof [] devuelve "object")`, se considera un tipo de dato incorporado (**built-in**) en JavaScript.  
No requiere librerías externas y tiene su propio constructor y sintaxis literal [], por lo que el lenguaje lo reconoce como una estructura de datos nativa principal.

---

##  Question #2
Does Javascript have `Set` as a native datatype?

[ ] Yes

[x] No

### **Explicación**:
Al igual que los `Arrays`, `Set` es un objeto global introducido en ES6 para almacenar valores únicos.  
No es un tipo de dato primitivo/nativo; es una estructura de datos basada en objetos.

---

##  Question #3
Does Javascript have `Dictionary` as a native datatype?

[ ] Yes

[x] No

### **Explicación**:
JavaScript no tiene una palabra clave o tipo nativo llamado `Dictionary`.  
Lo que otros lenguajes (como Python) llaman diccionarios, en JS se maneja mediante `Objetos literales ({})` o mediante el objeto global `Map`.

---

##  Question #4
What does `let` mean? (please check all true answers)

[x] It’s the keyword to define a variable

[ ] It’s the keyword to define a variable with a global scope

[x] It’s the keyword to define a variable with optionally initializing it to a value

[ ] It’s the keyword to define a constant variable

[x] It’s the keyword to define a variable that can be re-assign during the execution

### **Explicación**:
`let` tiene scope de bloque (no global por defecto), permite declarar una variable sin darle valor de inmediato (será undefined) y, a diferencia de `const`, permite que cambies su valor más adelante en el código.

---

##  Question #5
What does `const` mean? (please check all true answers)

[x] It’s the keyword to define a variable

[ ] It’s the keyword to define a variable with a global scope

[ ] It’s the keyword to define a variable with optionally initializing it to a value

[x] It’s the keyword to define a constant variable

[ ] It’s the keyword to define a variable that can be re-assign during the execution

### **Explicación**:
const requiere inicialización obligatoria (no puedes dejarla vacía al declararla) y bloquea la re-asignación. Es importante notar que si la constante es un objeto o array, puedes cambiar su contenido, pero no puedes re-asignar la variable a un objeto totalmente distinto.

💡 Tip de Julian para Julian:
Para que nunca se te olvide en el examen: los únicos tipos nativos (primitivos) en JS son:

Number

String

Boolean

Undefined

Null

Symbol

BigInt

Todo lo demás (Array, Set, Map, Date, etc.) son Objetos.

---
---

#   Exercises
##  0. First constant, first print
Write a script that prints "JavaScript is amazing":
-   You must create a constant variable called `myVar` with the value "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
`0-javascript_is_amazing.js`
```js
#!/usr/bin/node
const myVar = 'JavaScript is amazing';
console.log(myVar);

```
### **Logic**
1.   **El Shebang (`#!/usr/bin/node`):** 
-   Es lo que le dice a Ubuntu: "Oye, no intentes correr esto como un script de Bash, usa Node.js". 
-   Sin esto, el comando `./0-javascript_is_amazing.js` fallará.

2.   **const vs var**: 
-   El ejercicio prohíbe explícitamente `var`. 
-   Usar `const` es la mejor práctica para valores que no van a cambiar, ya que reserva un espacio en memoria de manera más eficiente y segura.

3.   **Comillas**: 
-   En JS (y especialmente con `semistandard`), se suelen preferir las comillas simples (`) a menos que el string contenga una.

### **Output**
`semistandard 0-javascript_is_amazing.js`
```bash
guillaume@ubuntu:~/$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/$ 
```

---

##  1. 3 languages
Write a script that prints 3 lines:
-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use console.log(...) to print all output
-   You are not allowed to use var
`1-multi_languages.js`
```js
#!/usr/bin/node
console.log('C is fun');
console.log('Python is cool');
console.log('JavaScript is amazing');

```
### **Logic**
1. Orden de ejecución: JavaScript ejecuta las instrucciones de arriba hacia abajo. Cada console.log añade automáticamente un salto de línea al final, por eso verás las tres frases en líneas separadas.

2. Comillas: semistandard prefiere las comillas simples ' '. Si usas comillas dobles " ", el linter podría marcarte un error a menos que el texto interno contenga una comilla simple.

3. Sin variables: En este ejercicio específico, no necesitas declarar constantes ni variables, solo imprimir directamente los strings.

### **Output**
`semistandard 1-multi_languages.js`
```bash
guillaume@ubuntu:~/$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$ 
```

---

##  2. Arguments
Write a script that prints a message depending of the number of arguments passed:
-   If no arguments are passed to the script, print "No argument"
-   If only one argument is passed to the script, print "Argument found"
-   Otherwise, print "Arguments found"
-   You must use console.log(...) to print all output
-   You are not allowed to use var
`2-arguments.js`
```js
#!/usr/bin/node
const count = process.argv.length;

if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

```
### **Logic**
1.   **`count === 2`**: 
-   Significa que solo están los dos argumentos base (Node y el nombre del archivo). 
-   El usuario no escribió nada extra.

2.   **`count === 3`**: 
-   El usuario escribió exactamente una palabra después del nombre del archivo.

3.   **`else`**: 
-   Cualquier número mayor a 3 significa que hay múltiples palabras/argumentos.

#### `process.argv`
Imagina que ejecutas el script así: ./2-arguments.js Hola

El array `process.argv` se vería así internamente:

1.  **`process.argv[0]`** (El ejecutable de Node):
Es la ruta absoluta en tu sistema de dónde está instalado el programa Node.js. En Ubuntu suele ser algo como /usr/bin/node. Este es el "motor" que lee tu código.

2.  **`process.argv[1]`** (El archivo del script):
Es la ruta absoluta de tu archivo que se está ejecutando en ese momento. Por ejemplo: /home/juliangf94/holberton_projects/javascript-warm_up/2-arguments.js.

####  ¿Qué es `process.argv`?
-   Es un **Array** (una lista) que Node.js crea automáticamente cada vez que ejecutas un script.   
-   Este array contiene todos los "argumentos" o palabras que se escribieron en la línea de comandos para iniciar el proceso.

####     ¿Qué hace `.length`?
-   Como `process.argv` es un objeto de tipo **Array**, tiene una propiedad incorporada llamada `.length`: 
    +   Esta propiedad simplemente cuenta cuántos elementos hay dentro de la lista.

### **Output**
```bash
guillaume@ubuntu:~/$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/$ 
```

---

##  3. Value of my argument
Write a script that prints the first argument passed to it:
-   If no arguments are passed to the script, print "No argument"
-   You must use console.log(...) to print all output
-   You are not allowed to use var
-   You are not allowed to use length
`3-value_argument.js`
```js
#!/usr/bin/node
const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}

```
### **Logic**
#### por que usamos undefined y no 0?
Porque `0` es un valor (un número), mientras que `undefined` es la ausencia de un valor.
### **Output**
```bash
guillaume@ubuntu:~/$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/$ ./3-value_argument.js School
School
guillaume@ubuntu:~/$ 
```

---

##  4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: " is "
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
`4-concat.js`
```js
#!/usr/bin/node
console.log(process.argv[2] + ' is ' + process.argv[3]);

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/$ 
```

---

##  5. An Integer
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
-   If the argument can't be converted to an integer, print "Not a number"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use `try/catch`
`5-to_integer.js`
```js
#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}

```
### **Logic**
1.   **`parseInt(process.argv[2])`**:
-   Tomamos el primer argumento del usuario e intentamos "limpiarlo" para que sea un entero.

2.   **`Number.isInteger(num)`**:
-   Si el usuario no pasó nada, o pasó letras, `num` será `NaN`.
-   `Number.isInteger(NaN)` devuelve `false`, por lo que el script imprimirá "Not a number".

3.   **Decimales**:
-   Si pasas 89.89, `parseInt` lo corta en 89.
-   Como 89 es un entero, el if es verdadero y verás "My number: 89".
### **Output**
```bash
guillaume@ubuntu:~/$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/$ 
```

---

##  6. Loop to languages
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use console.log(...) to print all output
-   You are not allowed to use var
-   You are not allowed to use any if/else statement
-   You can use only one console.log
-   You must use a loop (while, for, etc.)
`6-multi_languages_loop.js`
```js
#!/usr/bin/node
const myLines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < myLines.length; i++) {
  console.log(myLines[i]);
}

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$ 
```

---

##  7. I love C
Write a script that prints x times "C is fun"
-   Where x is the first argument of the script
-   If the first argument can't be converted to an integer, print "Missing number of occurrences"
-   You must use console.log(...) to print all output
-   You are not allowed to use var
-   You can use only two console.log
-   You must use a loop (while, for, etc.)
`7-multi_c.js`
```js
#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/$ ./7-multi_c.js -3
guillaume@ubuntu:~/$ 
```

---

##  8. Square
Write a script that prints a square
-   The first argument is the size of the square
-   If the first argument can't be converted to an integer, print "Missing size"
-   You must use the character X to print the square
-   You must use console.log(...) to print all output
-   You are not allowed to use var
-   You must use a loop (while, for, etc.)
`8-square.js`
```js
#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$ 
```

---

##  9. Add
Write a script that prints the addition of 2 integers
-   The first argument is the first integer
-   The second argument is the second integer
-   You have to define a function with this prototype: function add(a, b)
-   You must use console.log(...) to print all output
-   You are not allowed to use var
`9-add.js`
```js
#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

add(firstInt, secondInt);

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ ./9-add.js 
NaN
guillaume@ubuntu:~/$ ./9-add.js 1
NaN
guillaume@ubuntu:~/$ ./9-add.js 1 7
8
guillaume@ubuntu:~/$ ./9-add.js 13 89
102
guillaume@ubuntu:~/$ 
```

---

##  10. Factorial
Write a script that computes and prints a factorial
-   The first argument is integer (argument can be cast as integer) used for computing the factorial
-   Factorial of NaN is 1
-   You must do it recursively
-   You must use a function
-   You must use console.log(...) to print all output
-   You are not allowed to use var
`10-factorial.js`
```js
#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));

```
### **Logic**
Factorial de 89: Da un número gigante con notación científica (1.65...e+136). Esto es normal en JavaScript para números muy grandes.

Factorial de 333: Devuelve Infinity porque el resultado supera el límite de capacidad de almacenamiento de números de JavaScript (IEEE 754). No te preocupes, el Checker espera exactamente eso.
### **Output**
```bash
guillaume@ubuntu:~/$ ./10-factorial.js 
1
guillaume@ubuntu:~/$ ./10-factorial.js 3
6
guillaume@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/$ 
```

---

##  11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.
-   You can assume all arguments can be converted to integer
-   If no argument passed, print 0
-   If the number of arguments is 1, print 0
-   You must use console.log(...) to print all output
-   You are not allowed to use var
`11-second_biggest.js`
```js
#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}

```
### **Logic**
Para encontrar el segundo más grande de forma limpia en JavaScript, seguiremos estos pasos:
1. **Filtrar**: Ignorar los dos primeros argumentos (node y el nombre del archivo).
2. **Validar**: Si no hay argumentos o solo hay uno, imprimir 0.
3. **Convertir y Ordenar**: Convertir los strings a números y ordenarlos de mayor a menor.
4. **Extraer**: El segundo elemento del array ordenado será nuestro objetivo.


1.  `process.argv.slice(2)`: 
- Crea una copia del array empezando desde el índice 2, eliminando las rutas de node y el script.

2.  `.map(Number)`: Es una forma rápida de convertir todos los strings del array en números reales.

3.  `.sort((a, b) => b - a)`: 
- Por defecto, .sort() en JS ordena como si fueran palabras ("10" vendría antes que "2"). Usando (a, b) => b - a, le decimos a JS que reste los valores para ordenarlos de mayor a menor.

args[1]: Una vez ordenados (ej. [5, 4, 3, 2, 0]), el índice 0 es el más grande y el índice 1 es el segundo más grande.


### **Output**
```bash
guillaume@ubuntu:~/$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/$ 
```

---

##  12. Object
Update this script to replace the value 12 with 89:
- You are not allowed to use var
`12-object.js`
```js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/$ 
```

---

##  13. Add file
Write a function that returns the addition of 2 integers.

The function must be visible from outside
The name of the function must be add
You are not allowed to use var
`13-add.js`
```js
#!/usr/bin/node
exports.add = function (a, b) {
  return (a + b);
};

```
### **Logic**

### **Output**
```bash
guillaume@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/$ ./13-main.js
8
guillaume@ubuntu:~/$ 
```

---
