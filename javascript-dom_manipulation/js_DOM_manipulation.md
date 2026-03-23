# JavaScript DOM Manipulation — Learning Objectives

## How to select HTML elements in JavaScript

```javascript
// By ID
const title = document.getElementById('main-title');

// By class name
const cards = document.getElementsByClassName('card');

// By tag name
const paragraphs = document.getElementsByTagName('p');

// By CSS selector (returns first match)
const header = document.querySelector('header');
const firstCard = document.querySelector('.card');
const mainTitle = document.querySelector('#main-title');

// By CSS selector (returns all matches)
const allCards = document.querySelectorAll('.card');
const allLinks = document.querySelectorAll('nav a');
```

---

## Differences between ID, class and tag name selectors

| | ID | Class | Tag name |
|---|----|----|---------|
| HTML syntax | `id="main"` | `class="card"` | `<p>` |
| JS selector | `#main` | `.card` | `p` |
| JS method | `getElementById('main')` | `getElementsByClassName('card')` | `getElementsByTagName('p')` |
| Uniqueness | Unique — only one per page | Reusable — multiple elements | Targets all elements of that type |
| Returns | Single element | HTMLCollection | HTMLCollection |

```javascript
// ID — targets ONE specific element
document.getElementById('header');         // <div id="header">
document.querySelector('#header');

// Class — targets ALL elements with that class
document.getElementsByClassName('card');   // all <div class="card">
document.querySelectorAll('.card');

// Tag — targets ALL elements of that type
document.getElementsByTagName('p');        // all <p> elements
document.querySelectorAll('p');
```

---

## How to modify an HTML element style

```javascript
const title = document.querySelector('h1');

// Modify individual style properties
title.style.color = 'red';
title.style.fontSize = '32px';
title.style.backgroundColor = '#333';
title.style.display = 'none';       // hide element
title.style.display = 'block';      // show element

// Add/remove/toggle CSS classes (preferred approach)
title.classList.add('highlight');
title.classList.remove('highlight');
title.classList.toggle('active');
title.classList.contains('active'); // returns true/false
title.classList.replace('active', 'inactive'); //Changes from active to inactive
```

---

## How to get and update an HTML element content

```javascript
const paragraph = document.querySelector('p');

// Get content
console.log(paragraph.innerHTML);    // HTML content (tags included)
console.log(paragraph.textContent);  // Plain text only (no tags)

// Update content
paragraph.innerHTML = '<strong>New bold text</strong>';  // renders HTML
paragraph.textContent = 'New plain text';                // treats as text

// Get/set input values
const input = document.querySelector('input');
console.log(input.value);            // get current value
input.value = 'New value';           // set value

// Get/set attributes
const link = document.querySelector('a');
console.log(link.getAttribute('href'));
link.setAttribute('href', 'https://example.com');
```
Aunque ambos funcionan para cambiar el texto, hay una diferencia de seguridad y rendimiento:

- **textContent**: Solo inserta texto plano. Si intentas meter etiquetas como <b>Hola</b>, el navegador las mostrará literalmente como texto. Es el método más seguro contra ataques de inyección de código (XSS).

- **innerHTML**: El navegador tiene que "parsear" (analizar) el contenido para ver si hay etiquetas HTML. Es más lento y peligroso si el contenido viene de una fuente externa.

---

## How to modify the DOM

```javascript
// Create a new element
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello World';
newDiv.classList.add('card');

// Add to the DOM
document.body.appendChild(newDiv);                          // add at end of body
document.querySelector('#container').appendChild(newDiv);   // add inside container
document.querySelector('#container').prepend(newDiv);       // add at beginning

// Remove from the DOM
const element = document.querySelector('.card');
element.remove();                          // remove the element itself
element.parentNode.removeChild(element);   // remove via parent (older syntax)

// Replace an element
const newParagraph = document.createElement('p');
newParagraph.textContent = 'Replaced!';
const old = document.querySelector('h2');
old.parentNode.replaceChild(newParagraph, old);

// Clone an element
const clone = element.cloneNode(true);  // true = deep clone (with children)
document.body.appendChild(clone);
```

---

## How to make a request with XMLHttpRequest

```javascript
const xhr = new XMLHttpRequest();

// Configure the request
xhr.open('GET', 'https://api.example.com/data');

// Handle the response
xhr.onload = function () {
  if (xhr.status === 200) {
    const data = JSON.parse(xhr.responseText);
    console.log(data);
  } else {
    console.error('Error:', xhr.status);
  }
};

// Handle network errors
xhr.onerror = function () {
  console.error('Network error');
};

// Send the request
xhr.send();

// POST request with data
const xhrPost = new XMLHttpRequest();
xhrPost.open('POST', 'https://api.example.com/users');
xhrPost.setRequestHeader('Content-Type', 'application/json');
xhrPost.onload = function () {
  console.log(JSON.parse(xhrPost.responseText));
};
xhrPost.send(JSON.stringify({ name: 'Alice', age: 25 }));
```

---

## How to make a request with Fetch API

```javascript
// Basic GET request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Alice', age: 25 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// With async/await (cleaner syntax)
const getData = async () => {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
};

getData();
```

### XHR vs Fetch API

| | XMLHttpRequest | Fetch API |
|---|----------------|-----------|
| Syntax | Verbose | Clean and modern |
| Returns | Nothing (uses callbacks) | Promise |
| Error handling | `onerror` callback | `.catch()` or `try/catch` |
| Async/await | ❌ No | ✅ Yes |
| Browser support | All browsers | Modern browsers |

---

## How to listen/bind to DOM events

```javascript
const button = document.querySelector('button');

// Method 1 — addEventListener (recommended)
button.addEventListener('click', function () {
  console.log('Button clicked!');
});

// Method 2 — arrow function
button.addEventListener('click', () => {
  console.log('Button clicked!');
});

// Method 3 — named function (easier to remove)
const handleClick = () => console.log('Clicked!');
button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick); // remove listener

// Listen on the document
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM fully loaded');
});
```
1. **Función Anónima Tradicional (`function () { ... }`)**
- Se crea una función "sin nombre" directamente dentro del listener.
  + **Comportamiento de `this`**: Dentro de la función, la palabra clave `this` se refiere al elemento que recibió el evento (en este caso, el `button`).
  + **Desventaja**: 
    * Al ser anónima, **no puedes eliminarla** después con removeEventListener.
    * Si intentas quitarla, el navegador no sabrá a cuál te refieres porque la función no tiene una "dirección" guardada en memoria.

2. **Arrow Function** (`() => { ... }`)
- Es la sintaxis moderna (ES6) y la que más verás en React o proyectos modernos de JS.
  + **Comportamiento de `this`**: 
    * Las Arrow Functions no tienen su propio `this`. 
    * Heredan el `this` del contexto donde fueron creadas (usualmente el objeto global o una clase). 
    * Si necesitas usar `this` para referirte al botón, este método te dará problemas.

3. **Función Nombrada** (Referencia en memoria)
- Primero guardas la lógica en una constante (`handleClick`) y luego la pasas como referencia.
- **Por qué es mejor**: 
    + Como la función tiene un nombre, JavaScript sabe exactamente dónde está guardada en la memoria. Esto te permite:
    * **Reutilizarla**: Puedes asignar el mismo `handleClick` a 10 botones distintos sin repetir código.
    * **Eliminarla**: Es el único método que te permite usar `removeEventListener`. Esto es vital para el rendimiento; por ejemplo, si quieres que un botón solo funcione una vez y luego deje de "escuchar".

---

## How to listen/bind to user events

```javascript
// Click
element.addEventListener('click', (event) => {
  console.log('Clicked at:', event.clientX, event.clientY);
});

// Keyboard events
document.addEventListener('keydown', (event) => {
  console.log('Key pressed:', event.key);
  if (event.key === 'Enter') {
    console.log('Enter pressed!');
  }
});

document.addEventListener('keyup', (event) => {
  console.log('Key released:', event.key);
});

// Input change
const input = document.querySelector('input');
input.addEventListener('input', (event) => {
  console.log('Current value:', event.target.value);
});

// Form submit
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();  // prevent page reload
  console.log('Form submitted!');
});

// Mouse events
element.addEventListener('mouseover', () => console.log('Mouse over'));
element.addEventListener('mouseout', () => console.log('Mouse out'));

// The event object
button.addEventListener('click', (event) => {
  event.preventDefault();    // prevent default behavior
  event.stopPropagation();   // stop event from bubbling up
  console.log(event.target); // the element that triggered the event
});
```


---
---

#   Exercises:
##  0. Color Me
Write a JavaScript script that updates the text color of the header element to red (#FF0000):
-   You must use document.querySelector to select the HTML tag
Please test with this HTML file in your browser:
`0-main.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```
`0-script.js`
```js
const header = document.querySelector('header');
header.style.color = '#FF0000';

```

**Logic**

**Output**
```bash
Change color in:
"First HTML page"
```

---

##  1. Click and turn red
Write a JavaScript script that updates the text color of the `header` element to red (#`FF0000`) when the user clicks on the tag with id `red_header`:
Please test with this HTML file in your browser:
`1-main.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>

```
`1-script.js`
```js
const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', () => {
  header.style.color = '#FF0000';
});

```

**Logic**
1.  `addEventListener('click', ...)`: 
- Este es el método estándar para manejar interactividad. 
- Le dice al navegador: "Quédate atento a este elemento, y si alguien le hace clic, ejecuta esta función".

2.  **Arrow Function** `() => { ... }`: 
- Es la forma moderna y limpia de escribir funciones en JavaScript (ES6), cumpliendo con el requisito de no usar var y ser compatible con semistandard.

3.  Selección por **ID vs Etiqueta**:
- Usamos `#red_header` (con el numeral) porque estamos buscando un ID específico.
- Usamos `header` (sin nada) porque estamos buscando la etiqueta HTML.
**Output**
```bash

```

---

##  2. Add `.red` class
Write a JavaScript script that adds the class `red` to the `header` element when the user clicks on the tag with id `red_header`
Please test with this HTML file in your browser:
``2-main.html``
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```
`2-script.js`
```js
const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', () => {
  header.classList.add('red');
});

```

**Logic**

**Output**
```bash

```

---

##  3. Toggle classes
Write a JavaScript script that toggles the class of the `header` element when the user clicks on the tag id `toggle_header`:
- The `header` element must always have one class: `red` or `green`, never both in the same time and never empty. 
- If the current class is `red`, when the user click on id `toggle_header` element, the class must be updated to `green` ; and the reverse.

Please test with this HTML file in your browser:
``3-main.html``
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```
`3-script.js`
```js
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', () => {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});

```

**Logic**

**Output**
```bash

```

---

##  4. List of elements
Write a JavaScript script that adds a `li` element to a list when the user clicks on the element with id `add_item`:
- The new element must be: `<li>Item</li>` The new element must be added to the ul element with class `my_list`
Please test with this HTML file in your browser:
``4-main.html``
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```
`4-script.js`
```js
const addItem = document.getElementById('add_item');
const myList = document.querySelector('.my_list');
addItem.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  myList.appendChild(newLi);
});

```

**Logic**

**Output**
```bash

```

---

##  5. Change the text
Write a JavaScript script that updates the text of the `header` element to `New Header!!!` when the user clicks on the element with id `update_header`
Please test with this HTML file in your browser:
`5-main.html`
```html

```
`5-script.js`
```javascript
const updateHeader = document.getElementById('update_header');
const header = document.querySelector('header');
updateHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});

```

**Logic**

**Output**
```bash

```

---

##  6. Star wars character
Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`
- The name must be displayed in the HTML tag with id `character`.
- You must use the `Fetch API`.
- You probably should read something about `usign Promises` later.
Please test with this HTML file in your browser:
`6-main.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```
`6-script.js`
```js
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterName = document.getElementById('character');

fetch(url)
  .then(response => response.json())
  .then(data => {
    characterName.textContent = data.name;
  });

```

**Logic**
- `fetch(url)`:
  + El navegador lanza una petición asíncrona. Imagina que envías a un mensajero a la dirección de la URL. Tu código principal **no se detiene**; sigue ejecutándose mientras el mensajero viaja por internet.
- `.then(response => response.json())`:
  + `response`: Es lo que el mensajero trae de vuelta. Es un paquete cerrado que contiene el estado de la conexión (si fue exitosa o no) y los datos en un formato crudo.

  + `response.json()`: Es como decirle al mensajero: "Abre el paquete y traduce lo que hay dentro de JSON a un objeto de JavaScript que yo pueda entender". Este proceso de traducción también toma un poco de tiempo, por eso necesitamos otro `.then`.
- `.then(data => {characterName.textContent = data.name;});
  + `data`: 
    * Aquí ya tienes los datos "masticados" y listos. 
    * Es un objeto que se ve así: `{ "name": "Leia Organa", "height": "150", ... }`.
  + Las llaves `{ }`: 
    * Le dicen al linter que aquí termina la función de flecha y que simplemente estás ejecutando una orden (asignar el nombre), no intentando devolver (return) un valor.
  + `characterName.textContent`: 
    * El navegador busca la propiedad `.name` dentro de los datos recibidos y escribe ese texto dentro del elemento que seleccionamos al principio.

**Output**
```bash

```

---

##  7. Star Wars movies
Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`
- All movie titles must be list in the HTML `ul` element with id `list_movies`
- You must use the Fetch API.
Please test with this HTML file in your browser:
`7-main.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```
`7-script.js`
```js
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.getElementById('list_movies');

fetch(url)
  .then(response => response.json())
  .then((data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  });

```

**Logic**
1.  `data.results`: 
- Al inspeccionar la respuesta de esta API, verás que los datos de las películas están dentro de una propiedad llamada `results`. Es un array `[]`.

2.  `movies.forEach((movie) => { ... })`: 
- Este es el método más limpio en JavaScript para recorrer una lista. 
- Por cada "película" (`movie`) dentro del array, ejecutamos el código que está entre las llaves.

3.  **Creación dinámica**:
- `document.createElement('li')`: Fabricamos un nuevo punto de lista.
- `listItem.textContent = movie.title`: Le asignamos el título de la película actual (ej: "A New Hope").
- `listMovies.appendChild(listItem)`: Lo "pegamos" dentro del <ul> con id `list_movies`.

**Output**
```bash

```

---

##  8. Say Hello!
Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.com/?lang=fr` and displays the value of `hello` from that fetch in the HTML element with id `hello`.
- The translation of “hello” must be displayed in the HTML element with id `hello`
- Your script must work when it is imported from the <head> tag
Please test with this HTML file in your browser:
`8-main.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
```
`8-script.js`
```js
document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElement = document.getElementById('hello');
  fetch(url)
    .then(response => response.json())
    .then((data) => {
      helloElement.textContent = data.hello;
    });
});

```

**Logic**
1.  `document.addEventListener('DOMContentLoaded', ...)`:
- Sin esto, el `querySelector('#hello')` devolvería null porque el script corre antes de que el cuerpo de la página exista.

2.  **Fetch API**: 
- La URL nos devuelve un objeto JSON con una propiedad llamada `hello` (que en este caso será "Salut").

3.  **Selección del Elemento**: 
- Una vez que el DOM está listo, atrapamos el div y le inyectamos el saludo francés.
**Output**
```bash

```

---
