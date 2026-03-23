#   RESTful API
##  0. What does API stand for ?
Score: 1.0

Select the correct statement

-   [ ]Applicable programming interface
-   [x]Application programming interface
-   [ ]Application programmable interface
-   [ ]Applicable programs Interface
-   [ ]I don't know

**Logic**
It’s a set of rules that allows one piece of software to talk to another.


Es una interfaz que permite que dos aplicaciones se comuniquen. Piensa en ella como un "traductor" o un "puente" entre piezas de código.

---

##  1. What is the primary purpose of an API in software development?
Score: 1.0

Select the correct answer.

-   [ ]Assigning Pixel Coordinates in Images
-   [ ]Automating Physical Infrastructure
-   [x]Allowing Different Software Systems to Communicate and share data with each other.
-   [ ]I don't know

**Logic**
APIs act as a bridge. They allow different systems (like your Python backend and your React frontend) to exchange data and commands without needing to know how the other is built.
A REST API is a specific type of Web API that follows a particular architectural style. It is designed specifically for web-based communication using the HTTP protocol.

Su función principal es permitir que sistemas diferentes compartan datos y funcionalidades sin necesidad de saber cómo están construidos internamente.

---

##  2. What does the data format CSV stand for ?
Score: 1.0

Select the correct answer.

-   [ ]Computer System Visualization
-   [x]Comma-Separated Values
-   [ ]Centralized System View
-   [ ]Comma Segregated Variables
-   [ ]I don't know

**Logic**
A simple text format where each line is a data record and each field is separated by a comma. 
It's the most basic way to store table-like data.




Es un formato de archivo simple donde los datos se organizan en filas y las columnas se separan por comas. 
Es muy usado para intercambiar datos de tablas (como Excel).

---

##  3. In software engineering, what does REST stand for?
Score: 1.0

Select the correct answer.

-   [x]Representational State Transfer
-   [ ]Reliable Event Synchronization Technique
-   [ ]Remote Execution and Synchronization Toolkit
-   [ ]Robust Encryption and Security Techniques
-   [ ]I don't know

**Logic**
It’s an architectural style for distributed systems. 
It’s "Representational" because the server sends a representation of the data (like a JSON object) to the client.


Es un estilo de arquitectura para diseñar redes. 
Se basa en que el servidor entrega una "representación" del estado del recurso al cliente (normalmente en JSON).

---

##  4. Select the correct statements.
Score: 1.0

-   [ ]An API is Graphical User Interface.
-   [ ]An application API routes always exists in an abstraction layer already built-in in web frameworks and the developer doesn't need to create them.
-   [x]An API connects computers or pieces of software to each other. It is not intended to be used directly by a person (the end user) other than a computer programmer who is incorporating it into the software.
-   [x]An API is often made up of different parts which act as tools or services that are available to the programmer.
-   [ ]I don't know


**Logic**
Unlike a GUI (Graphic User Interface) meant for humans, an API is a Programmatic Interface meant for code. 
It provides tools and services that a developer can call upon.



Las APIs no son para el usuario final (como un botón en una web), sino para que un programador las integre en su software. 
Son herramientas y servicios para desarrolladores.

---

##  5. Select all the correct statements.
Score: 1.0

-   [ ]All APIs are REST APIs.
-   [x]All REST APIs are APIs, but not all APIs are REST APIs
-   [x]an API is a general term for a set of protocols, tools, and definitions allowing software components to interact. Whereas REST API is a specific type of API that follows the principles and constraints of the REST architectural style.
-   [x]REST means that a server will respond with the representation of a resource (generally an HTML, XML or JSON document) and that resource will contain hypermedia links that can be followed to make the state of the system change.
-   [ ]I don't know

**Logic**
"API" is the broad category. "REST API" is a specific sub-type that follows 6 constraints (like being stateless and using a uniform interface). 
In REST, we interact with resources (like /messages) through links and representations.



API es el término general. REST es un tipo específico de API que sigue reglas estrictas (como ser stateless y usar métodos HTTP). 
No toda API es REST (existen SOAP, GraphQL, etc.).

---

##  6. In Python, what does the CamelCase naming convention entail?
Score: 1.0

Select the correct answer.

-   [ ]Writing all letters in lowercase, with words separated by hyphens.
-   [x]Capitalizing the first letter of each word, except the first one, which remains lowercase.
-   [ ]Using only uppercase letters for variable and function names.
-   [ ]Randomly mixing uppercase and lowercase letters to create unique identifiers.
-   [ ]I don't know

**Logic**
In this convention, you capitalize the first letter of each word except the first one (e.g., myVariableName). 
Note: Python mostly uses snake_case, but this definition is technically correct for "lowerCamelCase".



Es escribir palabras juntas donde cada palabra inicia con Mayúscula. En Python se usa PascalCase (Capitalizing all) para clases. 
Nota: En Python puro, camelCase (primera minúscula) casi no se usa, se prefiere snake_case

---

##  7. Which of the following examples respect the Pythonic Class naming convention, as per PEP 8?
Score: 1.0

Select the correct answers.

-   [ ]ClassUPPERCASE
-   [x]MyClass
-   [ ]My_Class
-   [ ]snake_case_class
-   [x]Amenity
-   [x]HolbertonStudentClass
-   [ ]I don't know

**Logic**
PEP 8 dictates using PascalCase (or CapWords). 
Examples: MyClass, Amenity, User. No underscores allowed here!





Según PEP 8, las clases deben usar CapWords (o PascalCase). 
Ejemplo: MyClass, User, HolbertonStudent. Nunca deben llevar guiones bajos.

---

##  8. Which of the following examples respect the Pythonic Variable naming convention, as per PEP 8?
Score: 1.0

Select all the correct anwers.

-   [ ]MYVARIABLE
-   [x]number
-   [x]date_of_birth
-   [ ]My_var
-   [ ]my_Var
-   [ ]I don't know

**Logic**
Variables should be snake_case (lowercase with underscores). 
Example: date_of_birth. This is the "Pythonic" way.



Deben ser en minúsculas y, si tienen varias palabras, separadas por guion bajo (snake_case). 
Ejemplo: date_of_birth.

---

##  9. If the following statement correct ?
Score: 1.0

The Pythonic way (convention) to write function names is to use a lowercase word or words. Separate words by underscores to improve readability.

-   [x]Yes
-   [ ]No
-   [ ]I don't know

**Logic**
Just like variables, functions must be lowercase_with_underscores. 
This separates them visually from classes.



Al igual que las variables, las funciones deben usar snake_case para ser "Pythonic". 
Mejora mucho la legibilidad del código.

---

##  10. Which of the following examples respect the Pythonic function naming convention, as per PEP 8?
Score: 1.0

Select all the correct statements.

-   [ ]FUNCTION_NAME
-   [x]add
-   [ ]Function_Name
-   [x]calculate
-   [x]concat_strings
-   [ ]I don't know

**Logic**
add, calculate, and concat_strings are all perfect PEP 8 examples because they are descriptive, lowercase, and use underscores if needed.



add, calculate o concat_strings son correctos. Evita usar mayúsculas en nombres de funciones a menos que sean constantes (y las constantes van todas en mayúsculas).

---
#   🚀 HTTP Protocol & Security
##  11. Which HTTP method is commonly used to retrieve data from a REST API ?
Score: 1.0

Select the correct answer.

-   [ ]POST
-   [ ]DELETE
-   [x]GET
-   [ ]I don't know

**Logic**
Used specifically to retrieve or read data. It should never change the state of the server (it's "idempotent").



Es el método para leer o recuperar información. No debe modificar nada en el servidor; es como pedir una carta en un restaurante.

---

##  12. In a REST API, which of the following HTTP methods is used to create a new resource ?
Score: 1.0

Select the correct answer.

-   [ ]PUT
-   [ ]DELETE
-   [x]POST
-   [ ]CREATE
-   [ ]I don't know

**Logic**
Used to send data to a server to create a new resource. 
In your app, when you send a new message, you use POST.




Es el método para enviar datos al servidor con el fin de crear un nuevo recurso (como registrar un nuevo usuario o un mensaje).

---

##  13. What does HTTP stand for ?
Score: 1.0

Select the correct answer.

-   [x]HyperText Transfer Protocol
-   [ ]Hyperlink Text Processing
-   [ ]HyperTime Transmission Protocol
-   [ ]I don't know

**Logic**
The foundation of data exchange on the web. It defines how messages are formatted and transmitted.



Es el protocolo (lenguaje) que permite la transferencia de información en la World Wide Web.

---

##  14. Which HTTP status code indicates a successful request ?
Score: 1.0

Select the correct answer.

-   [ ]402
-   [x]200
-   [ ]404
-   [ ]500
-   [ ]I don't know

**Logic**
This is the standard response for a successful HTTP request. 
It simply means "OK, everything went as expected."


Es el código universal de "OK". 
Significa que la petición fue procesada con éxito.

---

##  15. What is the purpose of an HTTP request header ?
Score: 1.0

Select the correct answer.

-   [ ]To display HTML content
-   [ ]To store the body of the message
-   [x]To send metadata about the request to the server
-   [ ]I don't know

**Logic**
Headers are used to pass metadata. 
They tell the server things like "I am sending JSON" (Content-Type: application/json) or "I am using a specific browser."


Son metadatos (información extra) que el cliente envía al servidor. 
Aquí se indica, por ejemplo, qué tipo de datos acepta el cliente (Accept: application/json) o tokens de seguridad.

---

##  16. What is the primary function of an HTTP server ?
Score: 1.0

Select the correct answer.

-   [ ]To process user input and generate (create) data
-   [x]To serve web pages and handle HTTP requests from clients
-   [ ]I don't know

**Logic**
The server's job is to "wait" for requests from clients (like Chrome or a mobile app) and serve back the requested content (HTML, Images, or JSON).



---

##  17. What is the main difference between HTTP and HTTPS ?
Score: 1.0

Select the correct answer.

-   [ ]HTTPS is faster than HTTP
-   [x]HTTPS is more secure because it uses encryption
-   [ ]HTTP cannot be used to transfer data
-   [ ]I don't know

**Logic**
The 'S' stands for Secure. 
HTTPS uses TLS/SSL encryption to protect the data while it travels across the internet, preventing hackers from reading your messages.



---

##  18. What is authentication ?
Score: 1.0

Select the correct answer.

-   [x]The process of verifying a user’s identity
-   [ ]The process of encrypting data
-   [ ]The process of sending a request to the server
-   [ ]I don't know

**Logic**
This is the process of identity verification. 
It’s the server asking, "Are you really Julian?" before letting you access your Wise or BNP Paribas account data.

---
