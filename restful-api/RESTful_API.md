#   RESTful API
##  Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The `Representational State Transfer (REST)` architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

##  Learning Objectives:
1)  **HTTP/HTTPS Basics**: Grasp the foundational principles of the web's primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.

**HTTP (HyperText Transfer Protocol)** is the foundation of data exchange on the web, operating on a Request-Response model between a Client and a Server.
HTTP is a protocol for fetching resources such as HTML documents.  
It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser.  
A complete document is typically constructed from resources such as text content, layout instructions, images, videos, scripts, and more.  
It is an application layer protocol that is sent over TCP, or over a TLS-encrypted TCP connection, though any reliable transport protocol could theoretically be used. Due to its extensibility, it is used to not only fetch hypertext documents, but also images and videos or to post content to servers, like with HTML form results. HTTP can also be used to fetch parts of documents to update Web pages on demand.
HTTPS es HTTP con encriptación y verificación.  
La única diferencia entre ambos protocolos es que el HTTPS utiliza TLS (SSL) para encriptar las peticiones y respuestas HTTP normales, y para firmar digitalmente esas peticiones y respuestas.  
Como resultado, HTTPS es mucho más seguro que HTTP.  
Un sitio web que utiliza HTTP tiene http:// en su URL, mientras que un sitio web que utiliza HTTPS tiene https://.
HTTP significa Protocolo de transferencia de hipertexto, y es un protocolo, o un orden y sintaxis estipulados para presentar la información, que se usa para transferir datos a través de una red.  
La mayor parte de la información que se envía por Internet, incluidos los contenidos de los sitios web y las llamadas a las API, utiliza el protocolo HTTP.  
Hay dos tipos principales de mensajes HTTP: solicitudes y respuestas.
### Components of HTTP-based systems
HTTP is a client-server protocol: `requests` are sent by one entity, the user-agent (or a proxy on behalf of it).  
Most of the time the user-agent is a Web browser, but it can be anything, for example, a robot that crawls the Web to populate and maintain a search engine index.  
Each individual request is sent to a server, which handles it and provides an answer called the response.  
Between the client and the server there are numerous entities, collectively called proxies, which perform different operations and act as gateways or caches, for example.
+----------+        +----------+        +----------+        +----------+
|  Client  |        |   Proxy  |        |   Proxy  |        |  Server  |
+----------+        +----------+        +----------+        +----------+
     |------------------>|                    |                   |
     |                   |------------------->|                   |
     |                   |                    |------------------>|
     |                   |                    |<------------------|
     |                   |<-------------------|                   |
     |<------------------|                    |                   |
+----------+        +----------+        +----------+        +----------+
|  Client  |        |   Proxy  |        |   Proxy  |        |  Server  |
+----------+        +----------+        +----------+        +----------+


In reality, there are more computers between a browser and the server handling the request: there are routers, modems, and more.  
Thanks to the layered design of the Web, these are hidden in the network and transport layers.  
HTTP is on top, at the application layer.   
Although important for diagnosing network problems, the underlying layers are mostly irrelevant to the description of HTTP.

### Solicitudes y Respuestas HTTP
Las `solicitudes` HTTP las genera el navegador de un usuario cuando este interactúa con las propiedades de la web.  
Por ejemplo, si un usuario hace clic en un hipervínculo, el navegador enviará una serie de peticiones **HTTP GET** para el contenido que aparece en esa página.  
Si alguien busca en Google "¿Qué es el HTTP?" y este artículo aparece en los resultados de la búsqueda, cuando haga clic en el enlace, su navegador creará y enviará una serie de solicitudes HTTP para obtener la información necesaria para representar la página.

Todas estas solicitudes HTTP se dirigen a un servidor de origen o a un servidor proxy de caché, y ese servidor generará una `respuesta` HTTP.  
Las respuestas HTTP son respuestas a las solicitudes HTTP.
`Solicitud HTTP típica`
```text
GET /hello.txt HTTP/1.1
User-Agent: curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11
Host: www.example.com
Accept-Language: en
```
Cuando un usuario envía un formulario, el navegador lo traduce en una solicitud HTTP POST en lugar de una solicitud HTTP GET  
`Respuesta HTTP del servidor de origen`
```text
HTTP/1.1 200 OK
Date: Wed, 30 Jan 2019 12:14:39 GMT
Server: Apache
Last-Modified: Mon, 28 Jan 2019 11:17:01 GMT
Accept-Ranges: bytes
Content-Length: 12
Vary: Accept-Encoding
Content-Type: text/plain

Hello World!
```
### Solicitudes y Respuestas HTTPS
La S de HTTPS significa "seguro."  
HTTPS utiliza TLS (o SSL) para encriptar las solicitudes y respuestas HTTP.
En lugar de ver el texto HTTP, el atacante ve algo asi:
```text
t8Fw6T8UV81pQfyhDkhebbz7+oiwldr1j2gHBB3L3RFTRsQCpaSnSBZ78Vme+DpDVJPvZdZUZHpzbbcqmSW1+3xXGsERHg9YDmpYk0VVDiRvw1H5miNieJeJ/FNUjgH0BmVRWII6+T4MnDwmCMZUI/orxP3HGwYCSIvyzS3MpmmSe4iaWKCOHQ==
```
### TLS/SSL
TLS utiliza una tecnología denominada `criptografía de clave pública`, hay dos `claves`:
-   Pública
    +   Se comparte con los dispositivos clientes mediante el certificado SSL del servidor. 
-   Privada 

Cuando un cliente abre una conexión con un servidor, los dos dispositivos utilizan la clave pública y la privada para acordar nuevas claves, conocidas como `claves de sesión`, para encriptar las comunicaciones posteriores entre ellos.
Todas las solicitudes y respuestas HTTP se encriptan entonces con estas claves de sesión, para que el que intercepte las comunicaciones solo pueda ver una cadena de caracteres aleatoria, y no el texto plano.
### HTTPS ayuda a autenticar los servidores web
Cuando un cliente abre un canal con un servidor de origen (por ejemplo, cuando un usuario navega por un sitio web), la posesión de la clave privada que coincide con la clave pública del certificado SSL de un sitio web demuestra que el servidor es realmente el anfitrión legítimo del sitio web.  
Esto evita o ayuda a bloquear una serie de ataques que son posibles cuando no hay autenticación
### List of HTTP status codes
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
-   **1xx informational response**
    +   An informational response indicates that the request was received and understood and is being processed.
    +   It alerts the client to wait for a final response.
    +   The message does not contain a body.
    +   As the HTTP/1.0 standard did not define any 1xx status codes, servers must not send a 1xx response to an HTTP/1.0 compliant client except under experimental conditions
-   **2xx success**
    +   A success status indicates that the action requested by the client was received, understood, and accepted
-   **3xx redirection**
    +   A 3xx status indicates that the client must take additional action, generally URL redirection, to complete the request.
    +   A user agent may carry out the additional action with no user interaction if the method used in the additional request is GET or HEAD.
    +   A user agent should prevent cyclical redirects.
-   **4xx client error**
    +   A 4xx status code is for situations in which an error seems to have been caused by the client.
    +   Except when responding to a HEAD request, the server should include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.
    +   These status codes are applicable to any request method.
    +   User agents should display any included entity to the user.
-   **5xx server error**
    +   5xx status indicates that the server is aware that it has encountered an error or is otherwise incapable of performing the request.
    +   Except when responding to a HEAD request, the server should include an entity containing an explanation of the error situation, and indicate whether it is a temporary or permanent condition.
    +   Likewise, user agents should display any included entity to the user.
    +   These response codes are applicable to any request method.

### Cliente: el agente del usuario
Para poder mostrar una página Web:
-   El navegador envía una petición de documento HTML al servidor.  
-   El servidor procesa este documento,
-   Envía más peticiones para solicitar scripts, hojas de estilo (CSS), y otros datos que necesite (normalmente vídeos y/o imágenes) 
-   El navegador, une todos estos documentos y datos, y compone el resultado final: la página Web.
-   Los scripts, los ejecuta también el navegador, y también pueden generar más peticiones de datos en el tiempo, y el navegador, gestionará y actualizará la página Web en consecuencia.
##  Resumen
-   **Data Transfer**: 
    +   Communication consists of headers (metadata, status codes) 
    +   Optional body (the actual data, usually in JSON format).
-   **HTTP Methods**:
    +   `GET`: Retrieve data from a server.
    +   `POST`: Send new data to a server to create a resource.
    +   `PUT`/`PATCH`: Update existing resources.
    +   `DELETE`: Remove resources.
-   **HTTP vs. HTTPS**: 
    +   HTTPS is the secure version of HTTP. 
    +   It uses `TLS/SSL` encryption to protect data integrity and privacy, preventing "man-in-the-middle" attacks.

2)  **API Consumption with Command Line**: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.

Interacting with APIs via the terminal is essential for debugging and quick testing.

-   **Tool**: 
    +   `curl` (Client URL) is the industry standard.
    +   curl es "agnóstico al lenguaje". No importa si usas Python, JS o PHP, curl siempre te dirá la verdad sobre lo que responde el servidor.
-   **Example**: 
    +   `curl -X GET https://api.example.com/data`
-   **Headers**: 
    +   Use `curl -i` to see the response headers and status codes (e.g., 200 OK, 404 Not Found).

3)  **API Consumption with Python**: Elevate your data fetching skills by leveraging Python's capabilities, allowing for more advanced processing and data manipulation.

Python simplifies API interaction through the requests library, allowing for automated data processing.
-   **Key Feature**: 
    +   The `.json()` method automatically parses the response into a Python dictionary.
-   **Logic**: 
    +   Developers can handle status codes and automate complex workflows based on the data received.

4)  **API Development with http.server**: Understand the basics of crafting an API from scratch using Python's built-in modules, setting a solid foundation.

Python’s built-in `http.server` module provides a low-level way to understand how web servers handle requests at the socket level.
-   **Learning Value**: 
    +   It requires manually parsing request paths and headers, which helps understand what high-level frameworks (like Flask) do behind the scenes.

5)  **API Development with Flask**: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.
Flask is a "micro-framework" used to build robust and scalable APIs quickly.
-   **Routing**: Uses decorators (e.g., @app.route('/api/resource')) to map URLs to Python functions.
-   **Flexibility**: It is unopinionated, meaning developers have full control over the database and tools they choose to integrate.
    Flask no te obliga a usar una base de datos específica (como SQL o NoSQL), dándote total libertad arquitectónica.

6)  **API Security & Authentication**: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.

Protecting data and ensuring that only authorized users can access resources is critical.
-   **Methods**:
    +   `Basic Auth`: Sending credentials (username/password) in the header.
    +   `API Keys`: A unique identifier passed in the request.
    +   `JWT (JSON Web Tokens)`: A secure way to transmit information as a JSON object, commonly used for modern "Bearer Token" authentication.

7)  **API Standards & Documentation with OpenAPI**: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

Standardization ensures that an API is "discoverable" and easy to use for other developers.
-   **OpenAPI (Swagger)**: 
    +   A specification for machine-readable interface files.
    +   It provides a visual dashboard where users can test endpoints without writing code, ensuring the API is well-documented and maintainable.
    +   OpenAPI permite la generación automática de código. Un equipo de Frontend puede generar sus modelos de datos basándose únicamente en tu archivo de documentación.

##  Importance
In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems.  
They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures.  
From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It's a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

##  REST API Conceptual Diagram

+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database

### Components:
-   `Client`: The requester of the service, often a web browser or application.
-   `Web Server`: Handles the incoming request, acts as a middleman before passing it to the API server.
-   `API Server`: The actual logic layer that processes the request, determining what data or action is required.
-   `Database`: Stores the data which the API might fetch or modify.

### Flow:
-   The client sends an HTTP/HTTPS request to the Web Server.
-   The Web Server, after potential routing and load balancing, forwards the request to the API Server.
-   The API Server processes the request, interacts with the database if needed.
-   The API Server returns the processed response to the Web Server.
-   The Web Server sends back the final HTTP/HTTPS response to the client.
This diagram provides a high-level view of how RESTful API communication typically works.  
In simpler setups, the Web Server and API Server might be combined into one.  
The separation here illustrates potential layers in a more complex or scaled environment.

---
---

#   Exercises
##  0. Basics of HTTP/HTTPS
### Background:
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.
### Objective:
At the end of this exercise, students should be able to:
1.   Differentiate between HTTP and HTTPS.
2.   Understand the basic working and structure of HTTP requests and responses.
3.   Recognize and explain the common HTTP methods and status codes.

##  Answer
1. **Summary: HTTP vs. HTTPS**
The main difference between these two protocols is `security`.
-   **HTTP (Hypertext Transfer Protocol)**: 
    +   Data is sent in `plain text`. 
    +   If someone is trying to get information on the network (using tools like Wireshark) can read the content of the communication, including passwords or sensitive data.
-   **HTTPS (HTTP Secure)**: 
    +   It is the secure version of HTTP. 
    +   It uses `SSL/TLS` encryption to wrap the data.
        *   **Encryption**: Even if data is intercepted, it is unintelligible.
        *   **Authentication**: The browser verifies the server's SSL certificate to ensure it is the legitimate owner of the website.
        *   **Integrity**: It prevents attackers from tampering with the data during transit.

2. **Structure of HTTP Messages**
An HTTP communication consists of a `Request` and a `Response`.

-   **HTTP Request Outline**:
    +   **Request Line**: Includes the Method (e.g., `GET`), the Path (e.g., `/index.html`), and the Version (e.g., `HTTP/1.1`).
    +   **Headers**: Metadata like `Host`, `User-Agent`, and `Accept-Language`.
    +   **Empty Line**: Separates headers from the body.
    +   **Body**: (Optional) Data sent to the server (common in POST/PUT requests).
-   **HTTP Response Outline**:
    +   **Status Line**: Includes the Version, a Status Code (e.g., 200), and a Reason Phrase (e.g., OK).
    +   **Headers**: Server info, `Content-Type`, `Content-Length`, `Set-Cookie`.
    +   **Empty Line**: Separates headers from the body.
    +   **Body**: The actual content requested (HTML, JSON, Image).Shutterstock


3. **Common HTTP Methods**

| Method | Description | Use Case |
| :... | :... | :...|
| GET | Retrieves data from a specific resource. | Fetching a profile page or a list of blog posts. |
| POST | Submits data to be processed to a specified resource. | Submitting a "Contact Us" form or creating a new user. |
| PUT | Replaces all current representations of the target resource. | Updating an entire user profile with new information. |
| DELETE | Deletes the specified resource. | Removing a photo or a post from a database. |

4. **Common HTTP Status Codes**
| Status Code | Description | Scenario |
| :... | :... | :...|
|200 OK | The request has succeeded. | Successfully loading the homepage of a website. |
| 301 Moved Permanently | The resource has been assigned a new permanent URI. | When a website changes its domain and redirects old links. |
| 400 Bad Request | The server cannot process the request due to client error. | Sending a malformed JSON body in an API request. |
| 404 Not Found | The server cannot find the requested resource. | Trying to access a page that does not exist (e.g., /wrong-url). |
| 500 Internal Server Error | The server encountered an unexpected condition. | A crash in the backend code (like a Python traceback). |

##  1. Consume data from an API using command line tools (curl)
### Background:
`curl (Client URL)` is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more).  
It's widely used for debugging, testing, and interacting with RESTful web services and APIs.  
By mastering curl, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.
---
1. Installation and Version Verification
In a WSL/Linux environment, curl is typically pre-installed.
-   Command: `curl --version`
-   Result: You will see the version number, the release date, and a list of supported protocols (HTTP, HTTPS, FTP, etc.).
---
2. Basic Interaction
To fetch the raw HTML content of a website:
-   Command: `curl http://example.com`
-   Observation: The terminal will display the HTML source code of the page. This confirms that the client-server connection is active.
---
3. Fetching Data from an API (GET Request)
Using a public API like **JSONPlaceholder** allows us to see how data is transferred in JSON format.
-   Command: `curl https://jsonplaceholder.typicode.com/posts`
-   Output: A JSON array of 100 posts. Each object contains:
    +   userId: ID of the author.
    +   id: Unique identifier of the post.
    +   title: The title of the post.
    +   body: The content of the post.
---
4. Inspecting Headers
Sometimes we only need the metadata (status codes, server type, content type) without the actual body content.
-   Command: `curl -I https://jsonplaceholder.typicode.com/posts`
-   Output Analysis: * HTTP/2 200: Confirming a successful request.
    +   content-type: application/json; charset=utf-8: Confirming the data format.
    +   x-powered-by: Often showing the server technology (e.g., Express).
---
5. Sending Data (POST Request)
To simulate creating a new resource on the server, we use the `-X` flag to specify the method and `-d` to send data.
-   Command: 
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
-   Result: The server responds with the object you sent plus an `id: 101`.
-   Explanation: Even though JSONPlaceholder is a mock API and doesn't permanently save the data, it returns a **201 Created** status or a success body to acknowledge the request was processed.
-   By default `curl` uses `GET`
**Logic**

### Useful Shortcuts:
| Flag | Name | Function | Example | Output |
| :... | :... | :... | :... | :... |
| `-X` | Method | Specifies the HTTP method (POST, PUT, DELETE). | `curl -X DELETE https://jsonplaceholder.typicode.com/posts/1` | El servidor responderá con un cuerpo vacío {} y un código 200 OK, indicando que la "eliminación" (simulada) fue exitosa. |
| `-I` | Head | Fetches only the headers of the response. | `curl -I https://jsonplaceholder.typicode.com/photos` | HTTP/2 200, content-type: application/json, y la fecha |
| `-d` | Data | Sends data in a POST/PUT request (data-ascii). | `curl -X POST -d "title=NuevoPost&body=HolaMundo&userId=1" https://jsonplaceholder.typicode.com/posts` | El servidor te devolverá el objeto que enviaste junto con un id: 101. |
| `-H` | Header | Adds a custom header (e.g., `-H "Content-Type: application/json`"). | `curl -X POST -H "Content-Type: application/json" -d '{"title": "foo", "body": "bar", "userId": 1}' https://jsonplaceholder.typicode.com/posts` | Al definir el `Content-Type`, el servidor procesa el texto `-d` como un objeto JSON real en lugar de un formulario simple |
| `-v` | VerboseShows the entire "handshake" (Request + Response). | `curl -v https://www.google.com` | Las líneas que empiezan con * son detalles de la conexión. Las líneas con > son lo que tú enviaste (Request). Las líneas con < son lo que el servidor respondió (Response). |


| Comando |	Acción Realizada |
| :... | :... |
| curl -X DELETE ... | Ordena al servidor borrar un recurso. |
| curl -I ... | Solo pide el "recibo" de la petición, no la mercancía. |
| curl -d "key=val" ... | Empaqueta datos para enviar al servidor. |
| curl -H "Auth: Key" ... | Envía credenciales o formatos específicos. |
| curl -v ... | Abre la "caja negra" para ver cómo viajan los datos. |


If you want to make the JSON output look pretty in your WSL terminal, try piping the command to jq (you might need to install it with sudo apt install jq):
    curl https://jsonplaceholder.typicode.com/posts/1 | jq


---

##  2. Consuming and processing data from an API using Python
### Background:
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs.  
The requests library simplifies HTTP communication and allows users to send HTTP requests using Python.  
Once the data is fetched, Python's built-in libraries and tools enable effortless data manipulation and processing.

###  Objective:
At the end of this exercise, students should be able to:
1.  Utilize the requests library to send HTTP requests and process responses.
2.  Parse and manipulate JSON data using Python.
3.  Convert structured data into other formats, e.g., CSV.
`main_02_requests.py`
```python
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()

```
`task_02_requests.py`
```python
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Print the status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        #   Parse data into a JSON object (list of dictionaries)
        posts = response.json()

        for post in posts:
            #   We use get because it´s safer than post["title"]
            print(post.get('title'))

def fetch_and_save_posts():
    """
     Fetches all posts and saves id, title, and body into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Structure the data: pick only the required fields
        # Using a list comprehension for efficiency
        structured_data = [
            {'id': post['id'],'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        # Define CSV column headers
        headers = ['id', 'title', 'body']
        #  Write to posts.csv
        try:
            # newline is used to avoid jumps in line
            with open('posts.csv', 'w', newline="", encoding='utf-8') as csvfile:
                # We give the headers to DictWrite and it orders the data
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                # It writes the first line with headers's names
                writer.writeheader()
                # It takes the list and writes it in the file
                writer.writerows(structured_data)
        # Handle error for in/out operation
        except IOError as e:
            print(f"Error saving CSV: {e}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

```
**Logic**



**Hints**:
1)   The `requests.get()` function returns a Response object, from which you can access various properties like `status_code`, `headers`, and methods like `json()`.
2)   When converting the parsed JSON data into a list of dictionaries, you might find list comprehensions useful for concise code.
3)   The `csv.DictWriter` class can be a convenient way to write dictionaries to a CSV file, as it automatically handles headers based on dictionary keys.

**Output**
```test
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
dolorem eum magni eos aperiam quia
...
```
1)   After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
2)   When parsing JSON data, you should see printed titles of the posts, e.g., "sunt aut facere repellat provident occaecati excepturi optio reprehenderit."
3)   After the data manipulation and conversion task, you should have a CSV file with columns id, title, and body. Each row in the CSV should correspond to a post from the fetched data.
---
##  3. Develop a simple API using Python with the `http.server` module
### Background:
The `http.server` module in Python's standard library provides basic classes for implementing web servers. While it's not typically used for production applications, it's a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.

### Objective:
At the end of this exercise, students should be able to:
1.   Set up a basic web server using the `http.server` module.
2.   Handle different types of HTTP requests (GET, POST, etc.).
3.   Serve JSON data in response to specific endpoints.

``
```python

```
`task_03_http_server.py`
```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# BaseHTTPRequestHandler tiene como limitacion principal que no tiene un 
# sistema de ruteo integrado, Flask ofrece dercoradores
class SimpleAPIRequestHandler(BaseHTTPRequestHandler):
    """
    Custom handler for a simple HTTP API.
    """
    def do_GET(self):
        """
        Handles GET requests by routing to specific endpoints.
        """
        # Endpoint: Root /
        # path is a string with everything that comes after /
        if self.path == '/':
            self.send_response(200)
            # Define simple text format
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send the message in bytes ("b")
            self.wfile.write(b"Hello, this is a simple API!")
        # Endpoint: /data
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            # application/json tells the browser that are structed data
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Convert dictionary to JSON string and then to bytes
            # json.dumps(data) converts the dict in a JSON string
            # encode transforms the str into bytes
            self.wfile.write(json.dumps(data).encode("utf-8"))
        # Endpoint: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        # Endpoint: /info (Requirement for Expected Output)
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))
        # Error Handling: 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIRequestHandler, port=8000):
    """
    Initializes and starts the HTTP server.
    """
    # '': Tells the server to hear every interface in the machine (localhost, private IP, etc)
    # port: Specific channel, 8000
    server_address = ('', port)
    # server_class: It's the constructor blueprint (HTTPServer)
    # hanlder_class: The manual (SimpleAPIRequestHandler)
    # httpd: The object with the server built and ready
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        # Start an infinite bucle that blocks the terminal
        # The program waits for a do_GET, then answers and waits
        httpd.serve_forever()
    # Detects when the users press "Ctrl + C"
    except KeyboardInterrupt:
        # We close the program, otherwise the port 8000 might be blocked
        httpd.server_close()
        print("\nServer stopped.")
# We tell Python
if __name__ == "__main__":
    run()

```

**Logic**

**Hints**
When sending headers using `http.server`, the `send_response` method is handy. You can also use `send_header` to specify specific headers, and don't forget to end headers with `end_headers`.  
For serving JSON data, you'll want to convert a Python dictionary to a JSON string.  
The `json` module in Python's standard library will be beneficial.
When checking the `path` of the request, the path attribute of the request handler (`self.path`) can be used to route requests to different endpoints.
**Output**
1.  On visiting `http://localhost:8000`, you should see the text: "Hello, this is a simple API!".
2.  On accessing the endpoint `/data`, a JSON response with the sample dataset should be returned: `{"name": "John", "age": 30, "city": "New York"}`.
3.  When visiting /info, you might see something like: `{"version": "1.0", "description": "A simple API built with http.server"}`.
4.  Accessing any other undefined endpoint should return a `404 Not Found` status with a message like "Endpoint not found".

---

##  4. Develop a Simple API using Python with Flask
### Background:
Flask is a lightweight web framework for Python, which is especially popular for creating small to medium web applications and RESTful APIs. Its minimalist and modular approach makes it a great choice for beginners to delve into web development without the overhead of more complex frameworks.
``
```shell
$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
`task_04_flask.py`
```python
from flask import Flask, jsonify, request


# Create the instance of the app
app = Flask(__name__)
# In-memory dictionary to store users
users = {}

# Returns a simple string
@app.route("/")
def home():
    """Root route that returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames."""
    # Takes the users's names and put them on a list
    # Convert the dictionary keys (usernames) into a list
    # jsonify converts the list to a JSON string and sets the Content-Type header to application/json
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Health check endpoint."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object based on the dynamic username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    # Return a 404 status code if the username does not exist in the dictionary
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via a POST request."""
    # Attempt to parse the request body as JSON
    # silent=True prevents Flask from crashing on invalid JSON, returning None instead
    # Si de request.get_json recibes un None la causa probable es que el cliente 
    # no envio el header 'Content-Type: application/json', Flask utiliza esta cabecera 
    # para saber que debe intentar procesar el cuerpo de la petición como objeto JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # Extract the 'username' field from the parsed dictionary
    username = data.get("username")
    # Validation logic: Ensure the username is provided and unique
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    # Store the user object in the memory dictionary
    users[username] = data
    # Return success confirmation with the 201 Created status code
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()

```
**Logic**

**Hints**
1.  Flask routes are defined using the @app.route() decorator, followed by a function that returns the desired response for that route.
2.  For serving dynamic content in routes, Flask allows you to add variables to the route (e.g., <variable_name>). These can be captured in your function parameters.
3.  The jsonify() function in Flask turns a Python dictionary or list into a response with application/json content-type.
4.  Flask's development server reloads automatically on code changes. However, for certain types of changes (like adding new files), you might need to restart the server.

**Output**
```python
Accessing http://localhost:5000 should show the message: "Welcome to the Flask API!".
Visiting http://localhost:5000/data should return a JSON response with a list of all usernames stored in the API. For example, if the users dictionary contains
{"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

the response should be:

    ["jane", "john"]

The /status endpoint should return the string: 
    "OK"
Accessing /users/jane should return the full object corresponding to the username "jane". For example:
{
        "username": "jane", 
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
}
Similarly, accessing /users/john should return:
{
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
}
"But if it doesn't exist, return a 404 with:"

{"error": "User not found"}
Posting a new user to /add_user should add the user to the users dictionary and return a 201 status code with a confirmation message with the user's data. For example, posting:
{
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}
should return:

{
        "message": "User added",
        "user": {
                "username": "alice",
                "name": "Alice",
                "age": 25,
                "city": "San Francisco"
        }
}
Posting a new user to /add_user without a username should return a 400 code error with the message:
{
        "error": "Username is required"
}
Posting a new user to /add_user with a duplicate username (i.e., the username already exists) should return a 409 code error with the message:
{
        "error": "Username already exists"
}
Posting a new user to /add_user with an invalid JSON body should return a 400 code error with the message:
{
        "error": "Invalid JSON"
}
```
---

##  5. API Security and Authentication Techniques
### Background:
API security is of paramount importance, especially when the API is exposed to the wider internet. 
There are many risks, including unauthorized data access, data tampering, and denial-of-service attacks.  
One fundamental method of securing APIs is to use authentication and authorization mechanisms, ensuring only authorized users can access certain resources.

### Objective:
At the end of this exercise, students should be able to:
1.   Understand the importance of API security.
2.   Implement basic authentication using Flask.
3.   Set up token-based authentication with JSON Web Tokens (JWT).
4.   Differentiate between authentication and authorization.

`task_05_basic_security.py`
```python
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
# get_jwt_identity es un atajo para el identificador principal, 
# mientras que get_jwt permite acceder a claims adicionales como roles o timestamps
app = Flask(__name__)

# Security Configuration
# Protects the sessions in Flask
app.config['SECRET_KEY'] = 'holberton_super_secret_key'
# A secret key used by JWT to sign the tokens
app.config['JWT_SECRET_KEY'] = 'jwt_super_secret_key'
# Initialize the security
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        # Transform the password into a hash
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- BASIC AUTHENTICATION ---
@auth.verify_password
# Callback: Flask-HTTPAuth calls this automatically to validate credentials
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    # Search the dictionary for an existing user
    user = users.get(username)
    # Compare the provided password with the stored hash
    if user and check_password_hash(user['password'], password):
        return user
    # Flask blocks the access
    return None


@app.route('/basic-protected')
# Forces the client to go to verify_password
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


# --- JWT AUTHENTICATION ---
@app.route('/login', methods=['POST'])
def login():
    """Authenticates the user and returns a JWT token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Additional claims store the role inside the token for fast authorization
        # create_access_token: Generates the token the client will use
        access_token = create_access_token(
            # Saves the user's name inside the token
            identity=username,
            # Saves if the user is a user or admin
            # Como precaucion de seguridad no se deben guardar objetos grandes
            # porque el token se envia en cada peticion y aumenta el overhead de red
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
# If someone tries to enter withouth a token, Flask-JWT-Extended stops the execution
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


# --- Admin ---
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-Based Access Control (Admin only)."""
    # Retrieve the claims from the current JWT token (the role)
    claims = get_jwt()
    if claims.get("role") != "admin":
        # 403 Forbidden is used when the user is authenticated but lacks permissions
        # El error 403 implica saber quien es el usuario pero no dejarlo pasar
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- CUSTOM JWT ERROR HANDLERS ---
# These handlers ensure that all authentication errors return a 401 status code


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# El error 401 indica falta de autenticidad válida, es un token expirado
@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()

```
**Logic**
-   `@jwt.token_in_blocklist_loader`: 
    +   Este callback permite consultar una base de datos, (como Redis) para invalidar tokens especificos aunquete tecnicamnete sean validos
-   `Salt`:
    +   Asegura que dos contraseñas identicas tengan hashes diferentes, evitando ataques de Rainbow Tables.      
    +   Aáde aleatoriedad para que la misma entrada no genere siempre la misma salida predecible
-   `/data`:
    +   Se prefiere devolver una lista de objetos en lugar de una lista de strings:
        *   Para permitir la extensibilidad futura sin romper la compatibilidad con clientes antiguos.
        +   Si devuelves objetos, puedes añadir nuevos campos (como ID o fecha) sin cambiar la estructura basica de la lista.
-   `create_access_token`:
    +   Si intentas ejecutarlo sin configurar `JWT_SECRET_KEY`:
        *   Flask lanzará una exepcion (RuntimeError) porque no tiene una semilla para firmar el token
        *   La firma criptográfica requiere obligatoriamente una llave secreta; sin ella el token no seria seguro ni verificable
**Cifrado vs Hashing**
-   Cifrado (Encryption):
    +   Bidireccional (puedes volver al origen).
    +   Enviar mensajes secretos.
    +   Necesitas una llave para descifrar.
-   Hashing:
    +   Unidireccional (no hay vuelta atrás).
    +   Verificar integridad y contraseñas.
    +   No hay llave para "des-hashear".
**Autenticacion vs Autorizacion**


**Output**
```bash
```

---
---
#   Conceptos Clave de RESTful API y Seguridad
-   HTTP Verbs (GET, POST, PUT, DELETE) & Status Codes (200, 201, 400, 401, 403, 404, 409)
-   Flask Routing: 
    +   `@app.route()` with dynamic parameters <username>
-   Request Handling: 
    +   `request.get_json(silent=True)`
    +   `request.headers`
-   Response Management: 
    +   `jsonify()` for JSON serialization and status codes
-   Security: 
    +   Password Hashing 
        *   `generate_password_hash`
        *   `check_password_hash`
-   Authentication: 
    +   HTTP Basic Auth 
        *   `@auth.login_required` 
        *   `verify_password`
-   JWT (JSON Web Tokens): 
    +   Access tokens
    +   payloads
    +   additional claims
    +   secret keys
-   Authorization: 
    +   Role-Based Access Control (RBAC)
        *   `get_jwt()`
-   Error Handling: 
    +   `@jwt.unauthorized_loader` 
    +   `@jwt.expired_token_loader` 
    +   Custom Error Handlers
-   Data Structures: 
    +   In-memory persistence using Python Dictionaries and Lists
