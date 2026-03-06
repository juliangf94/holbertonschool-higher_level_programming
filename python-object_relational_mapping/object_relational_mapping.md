# Python & MySQL — Learning Objectives
## How to connect to a MySQL database from a Python script

To connect Python to MySQL, you need the `MySQLdb` module (or `mysql-connector-python`).

### Install:
```bash
pip install mysqlclient
# or
pip install mysql-connector-python
```

### Connect:
```python
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    db="your_database"
)

cursor = db.cursor()
```

- `host` — where the MySQL server is running
- `user` — MySQL username
- `passwd` — MySQL password
- `db` — the database you want to connect to

Always close the connection when done:
```python
db.close()
```

---

## How to SELECT rows in a MySQL table from a Python script

```python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="my_db")
cursor = db.cursor()

cursor.execute("SELECT * FROM users")

# Fetch all results
rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()
```

### Fetch methods:
| Method | Description |
|--------|-------------|
| `fetchall()` | Returns **all** rows as a list of tuples |
| `fetchone()` | Returns the **next** single row |
| `fetchmany(n)` | Returns the **next n** rows |

### With a WHERE condition:
```python
cursor.execute("SELECT * FROM users WHERE age > %s", (21,))
rows = cursor.fetchall()
```

> ⚠️ Always use `%s` placeholders instead of f-strings or string concatenation to avoid **SQL injection**.

---

## How to INSERT rows in a MySQL table from a Python script

```python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="my_db")
cursor = db.cursor()

sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("John", 25)

cursor.execute(sql, values)

# IMPORTANT: commit the transaction to save changes
db.commit()

print(cursor.rowcount, "record inserted.")

db.close()
```

> ⚠️ `db.commit()` is **required** after `INSERT`, `UPDATE`, and `DELETE`. Without it, changes are not saved to the database.

### Insert multiple rows at once:
```python
records = [("Alice", 22), ("Bob", 30), ("Charlie", 28)]
cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", records)
db.commit()
```

---

## What ORM means

**ORM** stands for **Object-Relational Mapping**.

It is a programming technique that lets you **interact with a database using Python objects instead of writing raw SQL**. The ORM automatically translates your Python code into SQL queries behind the scenes.

### Without ORM (raw SQL):
```python
cursor.execute("SELECT * FROM users WHERE id = 1")
row = cursor.fetchone()
print(row[1])  # access by index
```

### With ORM (SQLAlchemy):
```python
user = session.query(User).filter_by(id=1).first()
print(user.name)  # access by attribute name
```

### Benefits of ORM:
| Benefit | Description |
|---------|-------------|
| **Abstraction** | No need to write raw SQL |
| **Readability** | Code is more Pythonic and easier to understand |
| **Portability** | Switch databases (MySQL, PostgreSQL, SQLite) with minimal code changes |
| **Security** | Helps prevent SQL injection by default |
| **Maintainability** | Easier to manage and refactor |

The most popular Python ORM is **SQLAlchemy**.

---

## How to map a Python Class to a MySQL table

With **SQLAlchemy**, each Python class represents a table. Each class attribute represents a column.

### Install:
```bash
pip install sqlalchemy
```

### Define a mapped class:
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'        # name of the MySQL table

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age})>"
```

### Connect and use the class:
```python
# Create engine (connection to MySQL)
engine = create_engine("mysql+mysqldb://root:password@localhost/my_db")

# Create all tables defined in Base
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# INSERT using Python object
new_user = User(name="Alice", age=22)
session.add(new_user)
session.commit()

# SELECT using Python class
users = session.query(User).all()
for user in users:
    print(user)

# SELECT with filter
user = session.query(User).filter_by(name="Alice").first()
print(user.age)
```

### Mapping summary:
| MySQL concept | SQLAlchemy equivalent |
|--------------|----------------------|
| Table | Python `class` |
| Column | Class `attribute` (`Column(...)`) |
| Row | Instance of the class |
| `INSERT` | `session.add(obj)` + `session.commit()` |
| `SELECT` | `session.query(Class).all()` |
| `WHERE` | `.filter_by()` or `.filter()` |
| `DELETE` | `session.delete(obj)` + `session.commit()` |

---
---
#   Exercises
##  0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`:

-   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
-   You must use the module MySQLdb (`import MySQLdb`)
-   Your script should connect to a `MySQL` server running on localhost at port `3306`
-   Results must be sorted in ascending order by states.id
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported  

`0-select_states.sql`
```sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

```

`0-select_states.py`
```python
#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_states():
    """
    Connects to the database and fetches all states sorted by id.
    """
    # Get database credentials from command line arguments
    # sys.argv[1]: user, sys.argv[2]: password, sys.argv[3]: database name
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to the MySQL server
    # Running on localhost at port 3306 as required
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the last executed statement
    query_rows = cursor.fetchall()

    # Iterate through the result set and print each row
    for row in query_rows:
        print(row)

    # Clean up: close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure the code is not executed when the module is imported
    list_states()

```


**Logic**
### 💡 Puntos clave del script:

1. **`sys.argv`**: Es la forma en que Python recibe datos desde la terminal. 
   - `argv[1]` será tu usuario (ej. 'root').
   - `argv[2]` será tu contraseña.
   - `argv[3]` será 'hbtn_0e_0_usa'.
2. **`MySQLdb.connect`**: Abre la sesión. Es el equivalente a cuando te logueas en la app de Wise o AXA; sin esto no hay acceso.
3. **`cursor`**: Es el objeto que realmente "habla" SQL. Sin el cursor, no puedes ejecutar `SELECT`.
4. **`fetchall()`**: Devuelve una **lista de tuplas**. Cada tupla representa una fila de la tabla `states`.
5. **`if __name__ == "__main__":`**: Esto asegura que si alguien importa tu archivo como un módulo, el código no empiece a borrar o leer cosas automáticamente.
**Try**
1. Asegúrate de tener la base de datos lista:
```bash
echo 'CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");' | mysql -uroot -p
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$ 
```

---

##  1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

-   Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
-   You must use the module MySQLdb (import MySQLdb)
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by states.id
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported
`1-filter_states.py`
```python
#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def filter_states():
    """
    Connects to the database and fetches states starting with N.
    """
    # Capture arguments from the command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor to interact with the database
    cursor = db.cursor()
    
    # Execute SQL query to filter names starting with 'N'
    # 'LIKE BINARY' is used to ensure case sensitivity (Upper N)
    # '%' is a wildcard that matches any characters following 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all records that match the query
    query_rows = cursor.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Prevent execution if the script is imported
    filter_states()

```


**Logic**
# Explicación: Task 1 - Filter states

## 🎯 Objetivo del Script
El archivo `1-filter_states.py` conecta a la base de datos MySQL `hbtn_0e_0_usa` y lista únicamente los estados cuyo nombre comienza con la letra **'N'** mayúscula, ordenados por `id` de forma ascendente.

## 🛠️ Desglose del Código y Conceptos Clave

### 1. Argumentos Dinámicos (`sys.argv`)
Para que el script sea reutilizable y seguro, no guardamos las credenciales dentro del código. Usamos la librería `sys` para capturar los datos que el usuario ingresa en la terminal:
* `sys.argv[1]`: Usuario de MySQL.
* `sys.argv[2]`: Contraseña.
* `sys.argv[3]`: Nombre de la base de datos.

### 2. La Consulta SQL y el filtro `LIKE BINARY`
La parte fundamental de este ejercicio es la sentencia SQL:
`SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC`

* **`LIKE`**: Es el operador de SQL que nos permite buscar patrones en cadenas de texto.
* **`BINARY`**: Es un requerimiento clave. En muchas configuraciones, MySQL no distingue entre mayúsculas y minúsculas (*case-insensitive*). Al agregar `BINARY`, forzamos a MySQL a comparar los valores byte por byte. Esto garantiza que atrape "New York" pero ignore "nevada" (si estuviera en minúscula).
* **`'N%'`**: El símbolo `%` actúa como un comodín (wildcard) que representa "cualquier cantidad de caracteres". Por ende, `'N%'` significa "cualquier texto que empiece con N mayúscula".

### 3. El Cursor (`db.cursor()`)
El cursor es el objeto de Python que interactúa directamente con la base de datos. Actúa como el mensajero:
1. Toma nuestra consulta SQL (`cursor.execute()`).
2. La entrega al servidor MySQL.
3. Recoge la respuesta completa usando `cursor.fetchall()`, que nos devuelve una lista de tuplas.

### 4. Buenas Prácticas (Estándar Holberton)
* **`if __name__ == "__main__":`**: Este bloque evita que el código se ejecute automáticamente si este archivo llega a ser importado por otro script de Python.
* **Cierre de conexiones**: Al final del script, siempre ejecutamos `cursor.close()` y `db.close()` para liberar los recursos del servidor y evitar fugas de memoria.

## 🚀 Cómo ejecutarlo
```bash
./1-filter_states.py root root hbtn_0e_0_usa
**Try**
```bash

```
**Output**
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$ 
```

---

##  2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument.
-   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
-   You must use the module MySQLdb (import MySQLdb)
-   Your script should connect to a MySQL server running on localhost at port 3306
-   You must use `format` to create the SQL query with the user input
-   Results must be sorted in ascending order by states.id
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported

`2-my_filter_states.py`
```sql
#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed.
"""
import sys
import MySQLdb


def filter_by_input():
    """
    Connects to the database and fetches states matching the user input.
    """
    # Capture the 4 arguments from the command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish connection to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Construct the SQL query using format() as requested
    # BINARY ensures the match is case-sensitive (e.g., 'Arizona' != 'arizona')
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    
    # Execute the formatted query
    cursor.execute(query)

    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Close resources
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_by_input()

```


**Logic**
# Explicación: Task 2 - Filter states by user input

## 🎯 Objetivo del Script
El archivo `2-my_filter_states.py` toma un **cuarto argumento** desde la línea de comandos (el nombre de un estado) y muestra todos los registros en la tabla `states` que coincidan exactamente con ese nombre.

## 🛠️ Conceptos Clave y Desglose del Código

### 1. El Cuarto Argumento (`sys.argv[4]`)
A diferencia de los scripts anteriores, ahora capturamos un parámetro adicional de búsqueda ingresado por el usuario:
* `state_name = sys.argv[4]`

### 2. Construcción de la Consulta con `.format()`
El requerimiento principal de esta tarea es inyectar la variable del usuario directamente en el *string* de la consulta SQL utilizando el método `format()` de Python:

`query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)`

* **`LIKE BINARY`**: Al igual que en la Task 1, fuerza a MySQL a realizar una comparación estricta de mayúsculas y minúsculas (*case-sensitive*). De esta forma, si el usuario busca 'arizona' (minúscula), no coincidirá con 'Arizona' (mayúscula).
* **`{}`**: Es el *placeholder* que será reemplazado por el valor de la variable `state_name`.



### 3. La Trampa Educativa (SQL Injection)
Construir consultas usando `.format()` o concatenación de *strings* (`+`) es extremadamente peligroso. Si un usuario malintencionado pasa un argumento diseñado específicamente (como `' OR '1'='1`), podría alterar la lógica de la consulta y acceder a datos no autorizados. Holberton exige este método en la Task 2 para ilustrar el problema, el cual será corregido en la Task 3.

## 🚀 Cómo ejecutarlo
Recuerda pasar el nombre del estado entre comillas simples si ejecutas desde la terminal:
```bash
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
**Try**
```bash

```
**Output**
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$ 
```

---

##  3. SQL Injection...
Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?
```bash
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$ 
```
What? Empty?

Yes, it's an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

-   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
-   You must use the module MySQLdb (import MySQLdb)
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by states.id
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported
`3-my_safe_filter_states.py`
```sql
#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed, safely from SQL injections.
Usage: ./3-my_safe_filter_states.py <user> <password> <database> <state_name>
"""
import sys
import MySQLdb


def safe_filter_states():
    """
    Connects to the database and fetches states matching the user input
    using parameterized queries to prevent SQL injection.
    """
    # Capture arguments from command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Use parameterized query (%s) to prevent SQL injection.
    # We pass the query string and a tuple containing the user input separately.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the query passing the state_name as a tuple element
    cursor.execute(query, (state_name,))

    # Fetch and print results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Close resources
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()

```


**Logic**
# Explicación: Task 3 - SQL Injection (Safe filter states)

## 🎯 Objetivo del Script
El archivo `3-my_safe_filter_states.py` realiza la misma búsqueda que la Task 2 (filtrar estados por nombre), pero implementa **consultas parametrizadas** para ser inmune a ataques de Inyección SQL.

## 🛠️ ¿Qué es la Inyección SQL?
Es una vulnerabilidad que ocurre cuando se concatena texto (usando `+` o `.format()`) directamente en una consulta SQL. Si un usuario ingresa código SQL malicioso como argumento, la base de datos lo interpretará como una instrucción válida. 
En el ejemplo de Holberton, la entrada `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` engañó al script anterior para que borrara todos los registros de la tabla.

## 🛡️ La Solución: Consultas Parametrizadas
Para solucionar este fallo de seguridad, delegamos la inserción de variables al propio controlador de la base de datos (`MySQLdb`), el cual se encarga de escapar y limpiar los caracteres peligrosos.

### Desglose del Código:
1. **El Placeholder (`%s`)**:
   En lugar de inyectar la variable directamente en el string, usamos `%s` como marcador de posición:
   `query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"`
   *(Nota: en MySQLdb siempre se usa `%s`, incluso si el dato es un número entero).*

2. **Ejecución Segura (`cursor.execute`)**:
   Pasamos la variable como un **segundo argumento** en forma de tupla al método `execute()`:
   `cursor.execute(query, (state_name,))`
   La coma extra `(state_name,)` es crucial porque Python necesita saber que es una tupla de un solo elemento, no solo una expresión entre paréntesis.
   -    La palabra `query` (que en español significa "consulta" o "petición") es simplemente una variable de texto (string) en Python.

### Conclusión de Seguridad
Con este método, si el usuario intenta ingresar código malicioso, la base de datos lo tratará literalmente como un string de texto y buscará un estado que se llame exactamente *"Arizona'; TRUNCATE TABLE states..."*, lo cual no arrojará resultados, manteniendo la base de datos a salvo.

## 🚀 Cómo ejecutarlo
```bash
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
**Try**
```bash

```
**Output**
```bash
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$ 
```

---

##  4. Cities by states
Write a script that lists all cities from the database hbtn_0e_4_usa

-   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
-   You must use the module MySQLdb (import MySQLdb)
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by cities.id
-   You can use only execute() once
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported  

`4-cities_by_state.sql`
```sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
```
`4-cities_by_state.py`
```sql
#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_cities():
    """
    Connects to the database and fetches all cities with their respective
    state names, using an INNER JOIN.
    """
    # Capture the 3 arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query using JOIN to combine cities and states
    # We select city id, city name, and state name.
    # We match them where the state_id in cities matches the id in states.
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    
    # Execute the query (Only once, as required)
    cursor.execute(query)

    # Fetch all the rows
    query_rows = cursor.fetchall()

    # Print the results in the exact format required
    for row in query_rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
```


**Logic**
# Explicación: Task 4 - Cities by states

## 🎯 Objetivo del Script
El archivo `4-cities_by_state.py` lista todas las ciudades de la base de datos `hbtn_0e_4_usa`, mostrando el ID de la ciudad, el nombre de la ciudad y el nombre del estado al que pertenece.

## 🛠️ Desglose del Código y Conceptos Clave

### 1. El desafío del `execute() only once`
Holberton añade la restricción de usar `execute()` solo una vez. Esto obliga a resolver el problema usando puramente SQL (una sola consulta eficiente) en lugar de usar Python para hacer una consulta a `cities`, un bucle `for`, y múltiples consultas a `states` (lo cual sería terrible para el rendimiento).

### 2. Relación de Tablas (`JOIN`)
Como la tabla `cities` solo guarda el `state_id` (un número) pero el checker nos pide mostrar el nombre del estado en texto, necesitamos unir ambas tablas.



La consulta SQL utilizada es:
```sql
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC
**Try**
```bash
./4-cities_by_state.py root root hbtn_0e_4_usa
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$ 
```

---

##  5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

-   Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
-   You must use the module MySQLdb (import MySQLdb)
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by cities.id
-   You can use only execute() once
-   The results must be displayed as they are in the example below
-   Your code should not be executed when imported
`5-filter_cities.py`
```sql

```


**Logic**
# Explicación: Task 5 - All cities by state

## 🎯 Objetivo del Script
El archivo `5-filter_cities.py` recibe el nombre de un estado por argumento y devuelve una lista de todas las ciudades que pertenecen a ese estado, separadas por comas. El código está protegido contra inyecciones SQL y solo utiliza el método `execute()` una vez.

## 🛠️ Desglose del Código y Conceptos Clave

### 1. La Súper Consulta SQL (`JOIN` + `WHERE` + `%s`)
Esta consulta combina lo aprendido en los ejercicios anteriores:
```sql
SELECT cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = %s
ORDER BY cities.id ASC
**Try**
```bash
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```
**Output**
```bash
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/$ 
```

---

##  6. First state model
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
-   State class:
-   inherits from Base Tips
-   links to the MySQL table states
-   class attribute id that represents a column of an auto-generated, unique integer, can't be null and is a primary key
-   class attribute name that represents a column of a string with maximum 128 characters and can't be null
-   You must use the module SQLAlchemy
-   Your script should connect to a MySQL server running on localhost at port 3306
-   WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)  

`6-model_state.sql`
```sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
-- SHOW CREATE TABLE states;: Este comando intenta mostrar cómo se creó la tabla states.
SHOW CREATE TABLE states;

```
`model_state.py`
```py
#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Mantiene un registro de todas las tablas que creas. 
# # Cuando en el otro archivo llamas a Base.metadata.create_all, SQLAlchemy revisa este registro y dice: 
# #"Ah, aquí tengo anotada la tabla states, ¡vamos a crearla!".
# Create the declarative base instance
Base = declarative_base()

# Al heredar de Base, le dices a Python: "Esta no es una clase cualquiera, es una tabla de base de datos".
class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table 'states'.
    """
    # Aquí le das el nombre real que tendrá la tabla en MySQL.
    __tablename__ = 'states'

    id = Column(
        Integer,            # Tipo de dato: Número entero
        primary_key=True,   # Es la Llave Primaria (única e identificativa)
        nullable=False,     # No puede estar vacío (NOT NULL)
        autoincrement=True, # MySQL le asigna el número solo (1, 2, 3...)
        unique=True         # No se puede repetir
    )
    
    name = Column(
        String(128),        # Tipo de dato: Texto (VARCHAR) de hasta 128 caracteres
        nullable=False      # Es obligatorio poner un nombre
    )

```
###  Resumen de la Traducción (Python ➔ SQL)
Lo que hace SQLAlchemy es "traducir" tu código de Python a este código SQL que MySQL entiende:
| Código en model_state.py | Traducción a SQL |
| :... | :... |
|class State(Base) | CREATE TABLE ... |
| __tablename__ = 'states' | states |
| Integer, primary_key=True | INT PRIMARY KEY |
| String(128), nullable=False | VARCHAR(128) NOT NULL |

`6-model_state.py`
```python
#!/usr/bin/python3
"""
Start link class to table in database 
This script connects to a MySQL server and creates the table 
defined in model_state.py in the specified database.
"""
# Se usa para leer los argumentos que pasas por la terminal (usuario, contraseña y base de datos).
import sys
# Importa la "lógica" que escribiste en el otro archivo. SQLAlchemy necesita saber qué definiste para poder crearlo.
from model_state import Base, State
# Es la herramienta de SQLAlchemy que gestiona la conexión física con MySQL.
from sqlalchemy import create_engine


if __name__ == "__main__":
    # The engine is the source of connectivity to the database
    # Format: mysql+mysqldb://user:password@host/database_name
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        # Es una medida de seguridad. Antes de hacer nada, el programa le envía un "ping" a MySQL para confirmar que la conexión no se ha caído.
        pool_pre_ping=True
    )
    # 1. Scans all classes that inherit from Base (like State)
    # 2. Generates the SQL "CREATE TABLE" commands
    # 3. Executes them on the MySQL server
    Base.metadata.create_all(engine)

```


**Logic**
#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    
    name = Column(
        String(128),
        nullable=False
    )

# 🚀 Resumen: Task 6 - El Salto al ORM (SQLAlchemy)

En los ejercicios anteriores (0 al 5), usábamos **MySQLdb**, donde escribíamos strings de SQL puro (`"SELECT * FROM..."`). En este ejercicio, implementamos un **ORM** (Object-Relational Mapping).

### 1. Definición del "Plano" (`model_state.py`)
En lugar de crear la tabla manualmente en MySQL, creamos una **Clase de Python** llamada `State`. 
* Le dijimos que hereda de `Base` (la base declarativa).
* Definimos sus atributos (`id`, `name`) usando tipos de datos de SQLAlchemy (`Integer`, `String`).
* **Resultado:** Python ahora entiende que la clase `State` es el equivalente a una tabla en la base de datos.

### 2. El Motor de Conexión (`engine`)
En el archivo `6-model_state.py`, configuramos el `create_engine`. 
* El **Engine** es el puente. Sabe cómo hablar con MySQL usando tus credenciales (`root`, `password`, `db`).
* Es el encargado de traducir tus objetos de Python a comandos que MySQL entienda.

### 3. La Creación Automática (`create_all`)
Usamos la línea mágica: `Base.metadata.create_all(engine)`.
* Esto le pide a SQLAlchemy que busque todas las clases que heredan de `Base`.
* Al encontrar a `State`, SQLAlchemy generó automáticamente el comando `CREATE TABLE states (...)` y lo ejecutó por ti.

### 🛠️ Problemas Técnicos Superados
* **Entornos Virtuales (.venv):** Identificamos que tu terminal estaba "atrapada" en un entorno de otro proyecto (AirBnB) que estaba incompleto.
* **Gestión de Paquetes:** Reparamos la instalación de `pip` y nos aseguramos de que `SQLAlchemy` estuviera disponible globalmente en tu sistema.
* **Permisos de Ejecución:** Usamos `chmod u+x` para que Linux te permitiera correr el script de Python.

---

### 💡 Conclusión
Ahora ya no necesitas escribir SQL para crear tablas. Simplemente defines clases en Python y SQLAlchemy se encarga del trabajo sucio en la base de datos.

**Try**
```bash

```
**Output**
```bash
guillaume@ubuntu:~/$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table    Create Table
states    CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$ 
```

---

##  7. All states via SQLAlchemy
Write a script that lists all State objects from the database hbtn_0e_6_usa

-   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
-   You must use the module `SQLAlchemy`
-   You must import `State` and Base from model_state - from model_state import Base, `State`
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by states.id
-   The results must be displayed as they are in the example below
-   Your code should not be executed when imported
`7-model_state_fetch_all.sql`
```sql
-- Insert states into hbtn_0e_6_usa
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

`7-model_state_fetch_all.py`
```python
#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
```


### **Logic**
#### Imports
```python
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
```

| Import | Para qué sirve |
|--------|---------------|
| `sys` | Para leer los argumentos de la línea de comandos (`sys.argv`) |
| `create_engine` | Para crear la conexión con la base de datos MySQL |
| `Session` | Para abrir una sesión y hacer queries con objetos Python |
| `Base, State` | La clase `State` (representa la tabla `states`) y `Base` importados desde `model_state.py` |

---

#### El Engine — conexión a MySQL
```python
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ),
    pool_pre_ping=True
)
```

El engine es el **puente entre Python y MySQL**. La cadena de conexión se arma así:

```python
mysql+mysqldb://usuario:password@localhost/nombre_base_de_datos
```

- `mysql+mysqldb://` — le dice a SQLAlchemy que use el driver MySQLdb
- `sys.argv[1]` — usuario MySQL (ej: `root`)
- `sys.argv[2]` — contraseña MySQL (ej: `root`)
- `sys.argv[3]` — nombre de la base de datos (ej: `hbtn_0e_6_usa`)
- `pool_pre_ping=True` — verifica que la conexión esté viva antes de usarla

---

#### Base.metadata.create_all(engine)
```python
Base.metadata.create_all(engine)
```

Le dice a SQLAlchemy que cree todas las tablas definidas en las clases que heredan de `Base` si es que no existen todavía. En este caso se asegura que la tabla `states` exista antes de hacer cualquier query.

---

#### La Session — abrir la sesión
```python
session = Session(engine)
```

La sesión es el equivalente al `cursor` en MySQLdb. Es el objeto que usás para interactuar con la base de datos usando objetos Python en lugar de SQL puro.

```python
# MySQLdb (viejo)                  vs      SQLAlchemy (nuevo)
cursor = db.cursor()                        session = Session(engine)
cursor.execute("SELECT ...")                session.query(State)...
```

---

#### El Query — traer todos los estados
```python
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
```

Desglosado parte por parte:

| Parte | Equivalente SQL | Descripción |
|-------|----------------|-------------|
| `session.query(State)` | `SELECT * FROM states` | Trae todos los registros de la tabla `states` |
| `.order_by(State.id)` | `ORDER BY id ASC` | Ordena por `id` de menor a mayor |
| `.all()` | — | Ejecuta el query y devuelve una lista de objetos `State` |

Cada `state` del loop es un **objeto Python** con atributos:
- `state.id` → el id del registro
- `state.name` → el nombre del estado

```python
# En vez de acceder por índice como en MySQLdb:
print(row[0], row[1])

# Con SQLAlchemy accedés por nombre de atributo:
print(state.id, state.name)
```

---

#### Cerrar la sesión
```python
session.close()
```

Siempre hay que cerrar la sesión al terminar para liberar los recursos de la conexión. Es el equivalente a `cursor.close()` y `db.close()` en MySQLdb.

---

### Comparación MySQLdb vs SQLAlchemy

```python
# MySQLdb — con SQL puro
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print("{}: {}".format(row[0], row[1]))

# SQLAlchemy — con objetos Python
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
```

| | MySQLdb | SQLAlchemy |
|---|---------|-----------|
| Query | String SQL manual | Métodos Python |
| Acceso a datos | `row[0]`, `row[1]` (por índice) | `state.id`, `state.name` (por nombre) |
| Legibilidad | Menos legible | Más legible y Pythónico |

---

### Output esperado

```bash
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```
**Try**
```bash

```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$ 
```

---

##  8. First state
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

-   Your script should take 3 arguments: mysql username, `mysql password` and `database name`
-   You must use the module `SQLAlchemy`
-   You must import `State` and Base from `model_state - from model_state import Base, State`
-   Your script should connect to a MySQL server running on `localhost` at port `3306`
-   The state you display must be the first in `states.id`
-   You are not allowed to fetch all states from the database before displaying the result
-   The results must be displayed as they are in the example below
-   If the table `states` is empty, print `Nothing` followed by a new line
-   Your code should not be executed when imported
`8-model_state_fetch_first.py`
```sql
#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()

```

### **Logic**
#### Imports y conexión
```python
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
```
Igual que el task 7 — `sys` para los argumentos, `create_engine` y `Session` para conectarse a MySQL, y `Base, State` desde `model_state.py`.

---

#### Engine y Session
```python
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ),
    pool_pre_ping=True
)
Base.metadata.create_all(engine)
session = Session(engine)
```
Igual que el task 7 — crea la conexión con los 3 argumentos de la línea de comandos y abre la sesión.

---

#### El Query — traer solo el primer estado
```python
state = session.query(State).order_by(State.id).first()
```

Esta es la línea más importante y la diferencia clave con el task 7:

| Parte | Equivalente SQL | Descripción |
|-------|----------------|-------------|
| `session.query(State)` | `SELECT * FROM states` | Prepara el query sobre la tabla `states` |
| `.order_by(State.id)` | `ORDER BY id ASC` | Ordena por `id` de menor a mayor |
| `.first()` | `LIMIT 1` | Trae **solo el primer resultado** |

El SQL que genera internamente es:
```sql
SELECT * FROM states ORDER BY id ASC LIMIT 1;
```

> ⚠️ El enunciado prohíbe fetchear todos los estados antes de mostrar el resultado. Por eso se usa `.first()` y NO `.all()[0]` — `.first()` hace `LIMIT 1` directamente en la base de datos, mientras que `.all()[0]` traería todos los registros primero.

---

#### Verificar si la tabla está vacía
```python
if state is None:
    print("Nothing")
else:
    print("{}: {}".format(state.id, state.name))
```

`.first()` retorna `None` si no encuentra ningún resultado (tabla vacía). Por eso hay que verificar antes de acceder a `state.id` y `state.name` — si no, tiraría un `AttributeError`.

```
Tabla con datos  →  state = <State object>  →  "1: California"
Tabla vacía      →  state = None            →  "Nothing"
```

---

#### Cerrar la sesión
```python
session.close()
```
Siempre cerrar la sesión al terminar para liberar recursos.

---

#### Diferencia clave con Task 7

```python
# Task 7 — trae TODOS los estados
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

# Task 8 — trae SOLO el primero
state = session.query(State).order_by(State.id).first()
print("{}: {}".format(state.id, state.name))
```

| | Task 7 | Task 8 |
|---|--------|--------|
| Método | `.all()` | `.first()` |
| Retorna | Lista de todos los objetos | Un solo objeto o `None` |
| SQL equivalente | `SELECT * FROM states ORDER BY id` | `SELECT * FROM states ORDER BY id LIMIT 1` |
| Si está vacío | No imprime nada | Imprime `Nothing` |

---

#### Output esperado

```bash
# Con datos en la tabla
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California

# Con la tabla vacía
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
Nothing
```
### **Try**
```bash

```
### **Output**
```bash
guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/$ 
```

---

##  9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

-   Your script should take 3 arguments: mysql username, mysql password and database name
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by states.id
-   The results must be displayed as they are in the example below
-   Your code should not be executed when imported

### **`9-model_state_filter_a.py`**
```python
#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
```


### **Logic**
#### El Query — la parte nueva
```python
states = session.query(State).filter(
    State.name.like('%a%')
).order_by(State.id).all()
```

Esta es la única diferencia real con los tasks anteriores — el uso de `.filter()`:

| Parte | Equivalente SQL | Descripción |
|-------|----------------|-------------|
| `session.query(State)` | `SELECT * FROM states` | Prepara el query |
| `.filter(State.name.like('%a%'))` | `WHERE name LIKE '%a%'` | Filtra los que contienen 'a' |
| `.order_by(State.id)` | `ORDER BY id ASC` | Ordena por id |
| `.all()` | — | Trae todos los resultados |

El SQL que genera internamente es:
```sql
SELECT * FROM states WHERE name LIKE '%a%' ORDER BY id ASC;
```

---

#### ¿Qué significa `'%a%'`?

El `%` es un **wildcard** (comodín) que representa cualquier cantidad de caracteres.

```
'%a%'  →  cualquier cosa + 'a' + cualquier cosa
```

```
"California"  →  contiene 'a' ✅  →  Cali-a-liforni-a
"Arizona"     →  contiene 'a' ✅  →  Arizon-a
"Texas"       →  contiene 'a' ✅  →  tex-a-s
"New York"    →  no contiene 'a' ❌
"Nevada"      →  contiene 'a' ✅  →  Nev-a-d-a
```

---

#### `.filter()` vs `.filter_by()`

SQLAlchemy tiene dos formas de filtrar:

```python
# filter() — más flexible, usa operadores de comparación
session.query(State).filter(State.name.like('%a%'))
session.query(State).filter(State.id == 3)

# filter_by() — más simple, solo para igualdad exacta
session.query(State).filter_by(name="California")
session.query(State).filter_by(id=3)
```

| | `.filter()` | `.filter_by()` |
|---|-------------|----------------|
| Uso | Cualquier condición (`LIKE`, `>`, `<`, etc.) | Solo igualdad exacta (`=`) |
| Sintaxis | `State.name.like(...)` | `name="California"` |
| Flexibilidad | Alta | Baja |

Para este task necesitamos `.filter()` porque usamos `LIKE`, no una igualdad exacta.

---

#### Comparación con tasks anteriores

```python
# Task 7 — todos los estados
session.query(State).order_by(State.id).all()

# Task 8 — solo el primero
session.query(State).order_by(State.id).first()

# Task 9 — solo los que contienen 'a'
session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
```

---

#### Output esperado

```bash
./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
```

> New York (id=4) no aparece porque no contiene la letra `a`.

### **Try**
```bash
./9-model_state_filter_a.py root root hbtn_0e_6_usa
```
### **Output**
```bash
guillaume@ubuntu:~/$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/$ 
```

---

##  10. Get a state
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

-   Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   You can assume you have one record with the state name to search
-   Results must display the states.id
-   If no state has the name you searched for, display Not found
-   Your code should not be executed when imported
### **`10-model_state_my_get.py`**
```python
#!/usr/bin/python3
"""Prints the State object with the name passed as argument from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
```


### **Logic**
#### El Query — buscar por nombre exacto
```python
state = session.query(State).filter(
    State.name == sys.argv[4]
).first()
```

| Parte | Equivalente SQL | Descripción |
|-------|----------------|-------------|
| `session.query(State)` | `SELECT * FROM states` | Prepara el query |
| `.filter(State.name == sys.argv[4])` | `WHERE name = 'Texas'` | Busca por nombre exacto |
| `.first()` | `LIMIT 1` | Trae solo el primer resultado |

El SQL que genera internamente es:
```sql
SELECT * FROM states WHERE name = 'Texas' LIMIT 1;
```

---

#### ¿Por qué es SQL injection free?

SQLAlchemy con `.filter()` y el operador `==` **escapa automáticamente** el input del usuario, igual que los `%s` en MySQLdb.

```python
# ❌ VULNERABLE — string concatenation
cursor.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))

# ✅ SEGURO — MySQLdb con %s
cursor.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))

# ✅ SEGURO — SQLAlchemy con ==
session.query(State).filter(State.name == sys.argv[4])
```

SQLAlchemy internamente usa parámetros preparados, por eso cualquier input malicioso como `"Texas'; DROP TABLE states; --"` se trata como un string literal y no como código SQL.

---

#### Mostrar resultado o "Not found"
```python
if state is None:
    print("Not found")
else:
    print("{}".format(state.id))
```

- Si `.first()` no encuentra ningún resultado → retorna `None` → imprime `"Not found"`
- Si encuentra el estado → imprime **solo el `id`** (no el nombre, a diferencia de los tasks anteriores)

---

#### Comparación con tasks anteriores

```python
# Task 9 — filtra con LIKE (contiene 'a')
session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

# Task 10 — filtra con == (nombre exacto)
session.query(State).filter(State.name == sys.argv[4]).first()
```

| | Task 9 | Task 10 |
|---|--------|---------|
| Tipo de filtro | `LIKE '%a%'` | `== nombre_exacto` |
| Método final | `.all()` | `.first()` |
| Retorna | Lista de objetos | Un objeto o `None` |
| Imprime | `id: name` | Solo `id` |
| Si no hay resultados | No imprime nada | `Not found` |

---

### **Output esperado**

```bash
# Estado encontrado
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3

# Estado no encontrado
./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
```
### **Try**
```bash
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
```
### **Output**
```bash
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/$ 
```

---

##  11. Add a new state
Write a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa

-   Your script should take 3 arguments: mysql username, mysql password and database name
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Print the new states.id after creation
-   Your code should not be executed when imported
### **`11-model_state_insert.py`**
```python
#!/usr/bin/python3
"""Adds the State object Louisiana to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()

```

---

### **Logic**
#### Crear el nuevo objeto
```python
new_state = State(name="Louisiana")
```
Creás una instancia de la clase `State` como cualquier objeto Python. No escribís SQL — SQLAlchemy lo traduce automáticamente a un `INSERT`.

El `id` **no se pasa** porque está definido como `autoincrement=True` en `model_state.py` — MySQL lo genera solo.

---

#### Agregar a la sesión
```python
session.add(new_state)
```
Le decís a SQLAlchemy *"quiero guardar este objeto"*. En este momento el objeto **todavía no está en la base de datos** — está en la sesión esperando ser confirmado.

---

#### Confirmar los cambios
```python
session.commit()
```
Ejecuta el `INSERT` real en la base de datos. Sin `commit()` los cambios **no se guardan**.

```
session.add()   →  "quiero guardar esto"   (pendiente)
session.commit() →  INSERT ejecutado        (guardado en DB)
```

Después del `commit()`, SQLAlchemy actualiza el objeto `new_state` con el `id` generado por MySQL automáticamente.

---

#### Imprimir el nuevo id
```python
print("{}".format(new_state.id))
```
Después del `commit()`, `new_state.id` ya tiene el valor asignado por MySQL. Por eso se imprime **después** del commit y no antes.

```
ANTES del commit  →  new_state.id = None
DESPUÉS del commit →  new_state.id = 6
```

---

#### Comparación: MySQLdb vs SQLAlchemy

```python
# MySQLdb — INSERT manual
cursor.execute("INSERT INTO states (name) VALUES (%s)", ("Louisiana",))
db.commit()
print(cursor.lastrowid)  # id generado

# SQLAlchemy — con objetos
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()
print(new_state.id)      # id generado
```

| | MySQLdb | SQLAlchemy |
|---|---------|-----------|
| Insertar | `cursor.execute("INSERT ...")` | `session.add(objeto)` |
| Confirmar | `db.commit()` | `session.commit()` |
| Obtener id | `cursor.lastrowid` | `objeto.id` |

---

### Output esperado

```bash
./11-model_state_insert.py root root hbtn_0e_6_usa
6

./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
```

### **Try**
```bash
./11-model_state_insert.py root root hbtn_0e_6_usa
```
### **Output**
```bash
guillaume@ubuntu:~/$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$ 
```

---

##  12. Update a state
Write a script that changes the name of a State object from the database hbtn_0e_6_usa

-   Your script should take 3 arguments: mysql username, mysql password and database name
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Change the name of the State where id = 2 to New Mexico
-   Your code should not be executed when imported
`12-model_state_update_id_2.py`
```python
#!/usr/bin/python3
"""Changes the name of the State where id=2 to New Mexico in hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()

```

### **Logic**
#### Buscar el estado a modificar
```python
state = session.query(State).filter(State.id == 2).first()
```
Busca el estado con `id = 2`. Es exactamente igual al task 10 pero filtrando por `id` en vez de por `name`.

El SQL equivalente es:
```sql
SELECT * FROM states WHERE id = 2 LIMIT 1;
```

---

#### Modificar el atributo
```python
state.name = "New Mexico"
```
Simplemente cambiás el atributo del objeto Python como harías con cualquier objeto. SQLAlchemy detecta automáticamente que el objeto fue modificado y prepara un `UPDATE`.

---

#### Confirmar los cambios
```python
session.commit()
```
Ejecuta el `UPDATE` real en la base de datos.

```
state.name = "New Mexico"  →  objeto modificado (pendiente)
session.commit()            →  UPDATE ejecutado  (guardado en DB)
```

El SQL que genera internamente es:
```sql
UPDATE states SET name = 'New Mexico' WHERE id = 2;
```

---

#### Los 3 pasos para UPDATE con SQLAlchemy

```python
# 1. Buscar el objeto
state = session.query(State).filter(State.id == 2).first()

# 2. Modificar el atributo
state.name = "New Mexico"

# 3. Confirmar
session.commit()
```

---

#### Comparación: MySQLdb vs SQLAlchemy

```python
# MySQLdb — UPDATE manual
cursor.execute(
    "UPDATE states SET name = %s WHERE id = 2",
    ("New Mexico",)
)
db.commit()

# SQLAlchemy — con objetos
state = session.query(State).filter(State.id == 2).first()
state.name = "New Mexico"
session.commit()
```

| | MySQLdb | SQLAlchemy |
|---|---------|-----------|
| Buscar | `cursor.execute("SELECT ...")` | `session.query(State).filter(...)` |
| Modificar | String SQL con `SET` | `objeto.atributo = nuevo_valor` |
| Confirmar | `db.commit()` | `session.commit()` |

---

#### Resumen de operaciones CRUD con SQLAlchemy

| Operación | Código |
|-----------|--------|
| **CREATE** | `session.add(State(name="..."))` + `session.commit()` |
| **READ** | `session.query(State).filter(...).all()` |
| **UPDATE** | `state.name = "..."` + `session.commit()` |
| **DELETE** | `session.delete(state)` + `session.commit()` |

---

### **Try**
```bash
./12-model_state_update_id_2.py root root hbtn_0e_6_usa
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```

### **Output**
```bash
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
```

---

##  13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

-   Your script should take 3 arguments: mysql username, mysql password and database name
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Your code should not be executed when imported
`13-model_state_delete_a.py`
```python
#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    # SELECT * FROM states WHERE name LIKE '%a%';
    states = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()

```
---

### **Logic**
#### Buscar todos los estados con 'a'
```python
states = session.query(State).filter(
    State.name.like('%a%')
).all()
```
Igual que el task 9 — busca todos los estados que contienen la letra `a` en cualquier posición. El SQL equivalente es:
```sql
SELECT * FROM states WHERE name LIKE '%a%';
```

Con los datos actuales retorna:
```
California, Texas, Nevada, Louisiana
```
> New Mexico y New York no contienen 'a' → no se borran.

---

#### Borrar cada estado
```python
for state in states:
    session.delete(state)
```
Iterás sobre cada objeto encontrado y llamás `session.delete(state)`. Igual que con `session.add()`, los objetos quedan **pendientes de borrado** hasta el `commit()`.

---

#### Confirmar los borrados
```python
session.commit()
```
Ejecuta todos los `DELETE` pendientes en la base de datos de una sola vez.

```
session.delete(state1)  →  pendiente
session.delete(state2)  →  pendiente
session.delete(state3)  →  pendiente
session.commit()         →  DELETE ejecutado para todos
```

El SQL que genera internamente es:
```sql
DELETE FROM states WHERE id = 1;  -- California
DELETE FROM states WHERE id = 3;  -- Texas
DELETE FROM states WHERE id = 5;  -- Nevada
DELETE FROM states WHERE id = 6;  -- Louisiana
```

---

#### CRUD completo con SQLAlchemy

| Operación | Código | SQL equivalente |
|-----------|--------|-----------------|
| **CREATE** | `session.add(obj)` + `session.commit()` | `INSERT INTO ...` |
| **READ** | `session.query(State).filter(...).all()` | `SELECT * FROM ...` |
| **UPDATE** | `obj.attr = valor` + `session.commit()` | `UPDATE ... SET ...` |
| **DELETE** | `session.delete(obj)` + `session.commit()` | `DELETE FROM ...` |

---

### **Try**
```bash
./13-model_state_delete_a.py root root hbtn_0e_6_usa
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```
---
### **Output**
```bash
2: New Mexico
4: New York
```

---

##  14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

-   City class:
    +   inherits from Base (imported from model_state)
    +   links to the MySQL table cities
    +   class attribute id that represents a column of an auto-generated, unique integer, can't be null and is a primary key
    +   class attribute name that represents a column of a string of 128 characters and can't be null
    +   class attribute state_id that represents a column of an integer, can't be null and is a foreign key to states.id
    +   You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

-   Your script should take 3 arguments: mysql username, mysql password and database name
-   You must use the module SQLAlchemy
-   You must import State and Base from model_state - from model_state import Base, State
-   Your script should connect to a MySQL server running on localhost at port 3306
-   Results must be sorted in ascending order by cities.id
-   Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
-   Your code should not be executed when imported  

### **`model_city.py`**
```python
#!/usr/bin/python3
"""Contains the City class linked to the cities MySQL table"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class linked to the cities MySQL table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
```
### **model_city.py Logic**
-   `ForeignKey('states.id')` — vincula `state_id` con la tabla `states`, igual que `REFERENCES states(id)` en SQL
-   `Base` se importa desde `model_state.py` en vez de crear uno nuevo — ambas clases deben compartir el mismo Base


**`from model_state import Base`**
`City` importa `Base` desde `model_state.py` — no crea uno nuevo. Así ambas clases (`State` y `City`) comparten el mismo `Base` y SQLAlchemy las trata como parte del mismo esquema.

**`state_id = Column(Integer, ForeignKey('states.id'), nullable=False)`**
Esta es la columna nueva — `ForeignKey('states.id')` le dice a SQLAlchemy que `state_id` es una clave foránea que referencia la columna `id` de la tabla `states`. Es el equivalente a:
```sql
state_id INT NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id)
```


### **`14-model_city_fetch_by_state.py`**
```sql
#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    # SELECT states.*, cities.* FROM states, cities
    # WHERE states.id = cities.state_id
    # ORDER BY cities.id ASC;
    results = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

```

### **14-model_city_fetch_by_state.py Logic**
#### Explicación del Query
```python
results = session.query(State, City).filter(
    State.id == City.state_id
).order_by(City.id).all()
```

| Parte | Equivalente SQL | Descripción |
|-------|----------------|-------------|
| `session.query(State, City)` | `SELECT states.*, cities.*` | Trae datos de ambas tablas |
| `.filter(State.id == City.state_id)` | `WHERE states.id = cities.state_id` | Une las dos tablas por la FK |
| `.order_by(City.id)` | `ORDER BY cities.id ASC` | Ordena por id de ciudad |
| `.all()` | — | Trae todos los resultados |

El SQL equivalente completo es:
```sql
SELECT states.*, cities.*
FROM states, cities
WHERE states.id = cities.state_id
ORDER BY cities.id ASC;
```

#### Desempaquetar los resultados
```python
for state, city in results:
    print("{}: ({}) {}".format(state.name, city.id, city.name))
```

Como el query trae **dos objetos por fila** (`State` y `City`), se desempaquetan directamente en el loop con `state, city`. Luego se accede a los atributos de cada objeto por separado.

---

#### Relación entre State y City

```
states                    cities
+----+------------+       +----+----------+----------+
| id | name       |       | id | state_id | name     |
+----+------------+       +----+----------+----------+
|  1 | California |◄──────|  1 |    1     | San Fran |
|  2 | Arizona    |◄──────|  6 |    2     | Page     |
+----+------------+       +----+----------+----------+
         ▲                      FK references states.id
```

---

**Try**
```bash
cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```
---
**Output**
```bash
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/$ 
```

---

```bash
cat 0-select_states.sql | mysql
./0-select_states.py root root hbtn_0e_0_usa
./1-filter_states.py root root hbtn_0e_0_usa
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
./3-my_safe_filter_states.py root root hbtn_0e_0_usa
./4-cities_by_state.py root root hbtn_0e_4_usa
./5-filter_cities.py root root hbtn_0e_4_usa Texas
python3 6-model_state.py root root hbtn_0e_6_usa
cat 6-model_state.sql | mysql -uroot -p
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
./9-model_state_filter_a.py root root hbtn_0e_6_usa
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
./11-model_state_insert.py root root hbtn_0e_6_usa
./12-model_state_update_id_2.py root root hbtn_0e_6_usa
./13-model_state_delete_a.py root root hbtn_0e_6_usa
cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

Crear la base de datos
```bash
cat 4-cities_by_state.sql | mysql -u root -p
```

Borrar y recrear la base de datos vacía
```bash
mysql -u root -p -e "DROP DATABASE IF EXISTS hbtn_0e_0_usa; CREATE DATABASE hbtn_0e_0_usa;"
```
Borrar solo la tabla
```bash
mysql -uroot -p -e "DROP TABLE IF EXISTS hbtn_0e_6_usa.states;"
```
