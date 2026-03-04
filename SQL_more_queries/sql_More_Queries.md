#   SQL - More queries
## Resources
### Database Management & Permissions
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [How To Use MySQL GRANT Statement](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)

### SQL Fundamentals & Constraints
* [MySQL Constraints](https://zetcode.com/mysql/constraints/)
* [SQL Style Guide](https://www.sqlstyle.guide/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [MySQL Cheat Sheet](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

### Advanced Querying (Joins & Subqueries)
* [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
* [Basic query operation: the join](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join.md)
* [SQL technique: join types](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join_types.md)
* [SQL technique: multiple joins and the distinct keyword](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_multiple_joins.md)
* [SQL technique: subqueries](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_subqueries.md)
* [SQL technique: union and minus](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_union_minus.md)

### Tutorials
* [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)

### Database Design & Modeling
* [Relational Database Design](https://www.guru99.com/database-design.html)
* [Database Normalization Explained (1NF, 2NF, 3NF)](https://www.guru99.com/database-normalization.html)
* [Entity-Relationship (ER) Modeling](https://www.guru99.com/er-modeling.html)


---
---
# MySQL — Advanced Concepts

## How to create a new MySQL user

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

Example:
```sql
CREATE USER 'john'@'localhost' IDENTIFIED BY 'securepassword';
```

- `'username'@'host'` — defines the user and where they connect from. Use `'%'` as host to allow connections from anywhere.
- `IDENTIFIED BY` — sets the user's password.

---

## How to manage privileges for a user to a database or table

### Grant privileges:
```sql
-- All privileges on a database
GRANT ALL PRIVILEGES ON my_database.* TO 'john'@'localhost';

-- Specific privileges on a table
GRANT SELECT, INSERT ON my_database.users TO 'john'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
```

### Show privileges:
```sql
SHOW GRANTS FOR 'john'@'localhost';
```

### Revoke privileges:
```sql
REVOKE INSERT ON my_database.users FROM 'john'@'localhost';
```

### Common privilege types:
| Privilege | Description |
|-----------|-------------|
| `ALL PRIVILEGES` | Full access |
| `SELECT` | Read data |
| `INSERT` | Add data |
| `UPDATE` | Modify data |
| `DELETE` | Remove data |
| `CREATE` | Create tables/databases |
| `DROP` | Delete tables/databases |

---

## What's a PRIMARY KEY?

A **PRIMARY KEY** is a column (or set of columns) that **uniquely identifies each row** in a table. Rules:
- Must be **unique** — no two rows can have the same value.
- Cannot be **NULL**.
- A table can only have **one** primary key.

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

## What's a FOREIGN KEY?

A **FOREIGN KEY** is a column that creates a **link between two tables** by referencing the PRIMARY KEY of another table. It enforces **referential integrity** — you can't insert a value that doesn't exist in the referenced table.

```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

Here, `student_id` in `orders` must match an existing `id` in the `students` table.

---

## How to use NOT NULL and UNIQUE constraints

### NOT NULL
Ensures a column **cannot have an empty value**.
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,   -- name is required
    email VARCHAR(150)            -- email is optional
);
```

### UNIQUE
Ensures all values in a column are **different from each other**.
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(150) UNIQUE     -- no two users can share the same email
);
```

### Combined:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);
```

---

## How to retrieve data from multiple tables in one request

There are two main approaches: **JOIN** and **subqueries**.

```sql
-- Using JOIN (most common)
SELECT students.name, orders.course
FROM students
JOIN orders ON students.id = orders.student_id;

-- Using a subquery
SELECT name FROM students
WHERE id IN (SELECT student_id FROM orders);
```

---

## What are subqueries?

A **subquery** is a query nested inside another query. It runs first and its result is used by the outer query.

```sql
-- Subquery in WHERE
SELECT name FROM students
WHERE id IN (
    SELECT student_id FROM orders WHERE course = 'Math'
);

-- Subquery in SELECT
SELECT name,
    (SELECT COUNT(*) FROM orders WHERE orders.student_id = students.id) AS total_orders
FROM students;

-- Subquery in FROM
SELECT AVG(age) FROM (
    SELECT age FROM students WHERE age > 18
) AS adult_students;
```

> A subquery is always wrapped in parentheses `()`.

---

## What are JOIN and UNION?

### JOIN
**JOIN** combines rows from two or more tables based on a related column.

```sql
-- INNER JOIN: only matching rows in both tables
SELECT students.name, orders.course
FROM students
INNER JOIN orders ON students.id = orders.student_id;

-- LEFT JOIN: all rows from left table + matching from right
SELECT students.name, orders.course
FROM students
LEFT JOIN orders ON students.id = orders.student_id;

-- RIGHT JOIN: all rows from right table + matching from left
SELECT students.name, orders.course
FROM students
RIGHT JOIN orders ON students.id = orders.student_id;
```

| JOIN type | Returns |
|-----------|---------|
| `INNER JOIN` | Only rows with matches in **both** tables |
| `LEFT JOIN` | All rows from **left** table, NULLs if no match on right |
| `RIGHT JOIN` | All rows from **right** table, NULLs if no match on left |

### UNION
**UNION** combines the **results of two SELECT queries** into one result set.

```sql
SELECT name FROM students
UNION
SELECT name FROM teachers;
```

- `UNION` removes **duplicate** rows automatically.
- `UNION ALL` keeps **all rows** including duplicates.
- Both queries must have the **same number of columns** with compatible types.

```sql
-- UNION ALL (keeps duplicates)
SELECT name FROM students
UNION ALL
SELECT name FROM teachers;
```

### JOIN vs UNION:
| | JOIN | UNION |
|---|------|-------|
| Direction | Horizontal (adds columns) | Vertical (adds rows) |
| Purpose | Combine related data from multiple tables | Combine results of multiple queries |
| Requirement | A common key between tables | Same number and type of columns |

---
---
# MySQL Advanced — Quiz Answers

---

## Question #0 — What does DCL mean?

- [ ] Document Control Language
- [x] Data Control Language
- [ ] Data Concept Language
- [ ] Document Control Line

> **DCL (Data Control Language)** son los comandos que controlan los permisos y accesos en MySQL. Los comandos principales son `GRANT` (dar permisos) y `REVOKE` (quitar permisos).

---

## Question #1 — Is it possible to give only read access to a database to a user?

- [x] Yes
- [ ] No

> Con `GRANT SELECT ON database.* TO 'user'@'host';` le das acceso de **solo lectura** a toda una base de datos. El usuario podrá hacer `SELECT` pero no `INSERT`, `UPDATE` ni `DELETE`.

---

## Question #2 — Is it possible to give only read access to a table to a user?

- [x] Yes
- [ ] No

> Con `GRANT SELECT ON database.table TO 'user'@'host';` le das acceso de **solo lectura a una tabla específica**. El control de permisos en MySQL es granular hasta nivel de tabla e incluso columna.

---

## Question #3 — Is it possible to give only read access to multiple databases and tables to a user?

- [x] Yes
- [ ] No

> Podés ejecutar múltiples sentencias `GRANT` para diferentes bases de datos y tablas al mismo usuario:
> ```sql
> GRANT SELECT ON db1.* TO 'user'@'host';
> GRANT SELECT ON db2.table1 TO 'user'@'host';
> ```

---

## Question #4 — Is it possible to give only delete access to a table to a user?

- [x] Yes
- [ ] No

> Podés otorgar cualquier privilegio de forma individual. Con `GRANT DELETE ON database.table TO 'user'@'host';` el usuario solo podrá eliminar registros pero no leer ni insertar.

---

## Question #5 — Is it possible to give only insert access to a table to a user?

- [x] Yes
- [ ] No

> Igual que el caso anterior, con `GRANT INSERT ON database.table TO 'user'@'host';` el usuario solo podrá insertar registros. Cada privilegio (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) se puede otorgar de forma independiente.

---

## Question #6 — Which JOIN type doesn't exist? (select all correct answers)

- [ ] LEFT
- [x] IN LEFT
- [x] RIGHT AND LEFT
- [ ] INNER
- [x] TOP
- [ ] FULL OUTER
- [x] FULL INNER

> Los JOINs que **sí existen** en SQL son: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, y `FULL OUTER JOIN`.
>
> - ❌ **IN LEFT** — no existe, es una combinación inventada.
> - ❌ **RIGHT AND LEFT** — no existe como tipo de JOIN, aunque podés simular ese resultado con `FULL OUTER JOIN`.
> - ❌ **TOP** — `TOP` es una cláusula para limitar resultados (en SQL Server), no un tipo de JOIN.
> - ❌ **FULL INNER** — no existe. `INNER JOIN` ya existe pero sin "FULL". El concepto de "FULL" aplica solo a `FULL OUTER JOIN`.
>
> ⚠️ Nota: MySQL no soporta `FULL OUTER JOIN` nativamente, pero existe como concepto estándar en SQL y se puede simular con `UNION`.

---
---

#   Exercises
##  0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).  

`0-privileges.sql`
```sql
-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- The privileges are shown for localhost

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

```

### **Logica**
* **`SHOW GRANTS`**: Es el comando fundamental de administración de seguridad en MySQL. Se utiliza para consultar los permisos específicos (privilegios) que han sido otorgados a un usuario.
* **Estructura `'usuario'@'host'`**: En MySQL, la identidad de un usuario se compone de dos partes:
    * **User**: El nombre de la cuenta (ej. `user_0d_1`).
    * **Host**: Desde dónde se conecta (ej. `localhost` significa que solo puede entrar desde la misma máquina donde está el servidor).
* **Manejo de Errores (ERROR 1141)**: Si intentas ejecutar este comando para un usuario que **no existe** o que no tiene privilegios definidos aún, MySQL lanzará un error. En el contexto de Holberton, esto es normal en la primera ejecución del script porque los usuarios suelen crearse en las tareas siguientes.
* **Formato de Script**: Según los requisitos del proyecto, todas las palabras clave de SQL (`SHOW`, `GRANTS`, `FOR`) deben ir en **MAYÚSCULAS** y cada consulta debe estar precedida por un comentario descriptivo.  

### 🔍 Tip de Productividad: El archivo .my.cnf

* **Propósito**: Permite automatizar la conexión a MySQL sin escribir manualmente el usuario y la contraseña en cada comando.
* **Ubicación**: Debe estar en el directorio raíz del usuario (`~/.my.cnf`).
* **Seguridad (`chmod 600`)**: Es vital restringir los permisos de este archivo, ya que contiene la contraseña en texto plano. El comando `600` significa que solo el dueño del archivo puede leerlo y escribirlo.
* **Uso en Scripts**: Al tener este archivo, podemos ejecutar comandos simplemente con `mysql` o `mysql -e "QUERY"`, lo cual facilita mucho el testeo de tareas de Holberton.

### 🔍 Verificación de Entorno (MySQL Connectivity)

`mysql -e "SHOW DATABASES;"`

* **Comando `mysql -e "QUERY"`**: La bandera `-e` (execute) permite enviar una consulta SQL directamente desde la terminal de Linux sin entrar al monitor interactivo de MySQL. 
* **Automatización con `.my.cnf`**: Al obtener la tabla de bases de datos sin ingresar credenciales, confirmamos que el cliente de MySQL está leyendo correctamente el usuario `root` y la contraseña desde el archivo de configuración oculto.
* **Estado del Servidor**: Si el servicio `mysql` no estuviera activo, el comando devolvería un error de "Can't connect to local MySQL server". La salida actual confirma que el servicio está operativo en Ubuntu/WSL.  




### **Try**
```bash
cat 0-privileges.sql | mysql
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
```

---
---

##  1. Root user
Write a script that creates the MySQL server user `user_0d_1`.
-   `user_0d_1` should have all privileges on your MySQL server
-   The `user_0d_1` password should be set to `user_0d_1_pwd`
-   If the user `user_0d_1` already exists, your script should not fail
`1-create_user.sql`
```sql
-- Script that creates the MySQL server user user_0d_1
-- user_0d_1 has all privileges and password user_0d_1_pwd

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

```

### **Logica**
* **`CREATE USER IF NOT EXISTS`**: Es una cláusula de seguridad. Si el usuario `user_0d_1` ya existe en el sistema, MySQL simplemente saltará esta línea en lugar de lanzar un error que detendría la ejecución del script.
* **`IDENTIFIED BY 'user_0d_1_pwd'`**: Define la contraseña en texto plano para este usuario específico.
* **`GRANT ALL PRIVILEGES`**: Otorga el nivel más alto de permisos disponible. El usuario podrá realizar cualquier operación (DML, DDL, DCL) en el servidor.
* **`ON *.*`**: 
    * El primer `*` representa **todas las bases de datos**.
    * El segundo `*` representa **todas las tablas** dentro de esas bases de datos.
* **Privilegios Globales**: Al dar permisos sobre `*.*`, estamos creando un usuario con un nivel de acceso similar al `root`, ideal para tareas de administración.
### **Try**
```bash
cat 1-create_user.sql | mysql
```
```bash
cat 0-privileges.sql | mysql
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

---

##  2. Read user
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
-   `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
-   The `user_0d_2` password should be set to `user_0d_2_pwd`
-   If the database `hbtn_0d_2` already exists, your script should not fail
-   If the user `user_0d_2` already exists, your script should not fail
`2-create_read_user.sql`
```sql
-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- user_0d_2 password: user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 2: Read user)

* **`CREATE DATABASE IF NOT EXISTS`**: Crea la base de datos `hbtn_0d_2`. Al usar `IF NOT EXISTS`, el script es seguro de ejecutar múltiples veces sin lanzar errores si la base de datos ya está presente.
* **`CREATE USER IF NOT EXISTS`**: Crea la cuenta `user_0d_2` con su contraseña correspondiente.
* **`GRANT SELECT`**: A diferencia de `GRANT ALL`, aquí solo otorgamos el permiso de **lectura**. El usuario podrá hacer `SELECT`, pero no podrá hacer `INSERT`, `UPDATE` o `DELETE`.
* **`ON hbtn_0d_2.*`**: Esta es la parte más importante. 
    * No estamos usando `*.*` (todas las bases).
    * Estamos limitando al usuario a la base de datos `hbtn_0d_2`. El `.*` indica que tiene permiso sobre **todas las tablas** dentro de esa base de datos específica, pero en ninguna otra parte del servidor.
* **`GRANT USAGE ON *.*`**: Verás esto en el output de `SHOW GRANTS`. Es automático en MySQL y significa que el usuario tiene permiso para conectarse al servidor, aunque no tenga permisos globales sobre los datos.

### 🔍 Jerarquía de Asteriscos en Privilegios (MySQL)

En SQL, el asterisco `*` actúa como un comodín que significa "todo". La posición del asterisco antes o después del punto determina el nivel de acceso:

| Sintaxis | Nivel de Alcance | Descripción |
| :--- | :--- | :--- |
| **`*.*`** | **Global** | Acceso a **todas** las bases de datos y a **todas** las tablas del servidor. (Nivel Administrador/Root). |
| **`db_name.*`** | **Base de Datos** | Acceso a **una** base de datos específica y a **todas** sus tablas internas. |
| **`db_name.table_name`** | **Tabla** | Acceso únicamente a **una** tabla específica dentro de una base de datos. |
| **`db_name.view_name`** | **Vista** | Acceso únicamente a una vista (tabla virtual) específica. |

#### Puntos Clave:
* **Separación por Punto (`.`)**: El punto actúa como el separador de jerarquía: `[Contenedor].[Contenido]`.
* **Seguridad (Principio de Menor Privilegio)**: En entornos de producción, lo ideal es evitar el `*.*` para usuarios de aplicaciones. Se prefiere usar `db_name.*` para que, si la cuenta se ve comprometida, el atacante solo tenga acceso a una parte del servidor.
* **Privilegios Automáticos**: Cuando otorgas permisos en `db_name.*`, MySQL suele mostrar un permiso de `USAGE` en `*.*` automáticamente. Esto no significa que el usuario pueda ver otras bases de datos, sino que simplemente tiene permiso para conectarse al servidor.

### 🔍 Ejemplo: Permiso Específico (db_name.table_name)

Este es el nivel más alto de restricción antes de llegar a las columnas.  
Es ideal para entornos donde un usuario debe trabajar con datos específicos sin ver el resto de la base de datos.

* **Sintaxis**: `GRANT [permiso] ON [nombre_db].[nombre_tabla] TO 'usuario'@'host';`
* **Caso de Uso**: Imagina que tienes una base de datos `holberton_db` con tablas `users`, `projects` y `salaries`. 
    * Si usas `holberton_db.*`, el usuario ve **todo**.
    * Si usas `holberton_db.projects`, el usuario **solo puede interactuar con los proyectos**, y si intenta hacer un `SELECT` a `users`, MySQL le denegará el acceso.
* **Seguridad**: Este método se llama "Principio de Menor Privilegio". Le das al usuario exactamente lo que necesita para su tarea y nada más.

### **Try**
```bash
cat 2-create_read_user.sql | mysql
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
Grants for user_0d_2@localhost                                                                                                
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`                                                                                 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`  
guillaume@ubuntu:~/$ 
```

---

##  3. Always a name
Write a script that creates the table `force_name` on your MySQL server.
-   `force_name` description:
    +   `id` INT
    +   `name VARCHAR(256)` can't be null
    +   The database name will be passed as an argument of the `mysql` command
    +   If the table `force_name` already exists, your script should not fail
`3-force_name.sql`
```sql

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 3: Always a name)

* **`CREATE TABLE IF NOT EXISTS`**: Como ya es costumbre en Holberton, usamos esta cláusula para que el script sea "idempotente" y no falle si la tabla ya fue creada.
* **`name VARCHAR(256) NOT NULL`**: 
    * `VARCHAR(256)`: Reserva espacio para una cadena de hasta 256 caracteres.
    * `NOT NULL`: Es la **restricción (constraint)**. Le dice a MySQL: "Bajo ninguna circunstancia permitas que esta columna esté vacía (NULL)".
* **Manejo del Error 1364**: En el ejemplo que pusiste, cuando intentas hacer `INSERT INTO force_name (id) VALUES (333);`, MySQL nota que no incluiste el campo `name`. Como `name` es `NOT NULL` y no tiene un valor por defecto, MySQL bloquea la operación para proteger la calidad de los datos.
* **Paso de Argumentos**: Notarás que el comando de prueba es `cat 3-force_name.sql | mysql ... hbtn_0d_2`. El nombre de la base de datos se pone al final. Esto significa que el script se ejecutará "dentro" de esa base de datos automáticamente.
### **Try**
1. Ejecuta el script (recuerda que gracias a tu .my.cnf no necesitas el -p):
```bash
cat 3-force_name.sql | mysql hbtn_0d_2
```
2. Prueba la restricción intentando insertar algo sin nombre:
```bash
echo "INSERT INTO force_name (id) VALUES (1);" | mysql hbtn_0d_2
```
### **Output**
```bash
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
```
3. Prueba una inserción correcta:
```bash
echo "INSERT INTO force_name (id, name) VALUES (1, 'Julian');" | mysql hbtn_0d_2
```
4. La forma segura: Consultar los datos (SELECT)
```bash
echo "SELECT * FROM force_name;" | mysql hbtn_0d_2
```
### **Output**
```bash
id    name
1     Julian
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ 
```

---

##  4. ID can't be null
Write a script that creates the table `id_not_null` on your MySQL server.
-   `id_not_null` description:
    +   `id` INT with the default value 1
    +   `name VARCHAR(256)`
    +   The database name will be passed as an argument of the `mysql` command
    +   If the table `id_not_null` already exists, your script should not fail
`4-never_empty.sql`
```sql
-- Script that creates the table id_not_null on your MySQL server
-- id INT with the default value 1, name VARCHAR(256)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 4: ID can't be null)

* **`id INT DEFAULT 1`**: Esta es la clave de la tarea. La restricción `DEFAULT` le dice a MySQL: "Si en un `INSERT` no me pasan un valor para esta columna, rellénala automáticamente con el número 1".
* **Diferencia con NOT NULL**: 
    * `NOT NULL` (Tarea 3) lanza un **ERROR** si falta el dato.
    * `DEFAULT` (Tarea 4) **SOLUCIONA** la falta del dato asignando un valor predefinido.
* **Comportamiento en el INSERT**: En tu ejemplo, cuando ejecutas `INSERT INTO id_not_null (name) VALUES ("Best");`, solo estás enviando el nombre. MySQL nota que falta el `id`, revisa la definición de la tabla, ve que tiene un `DEFAULT 1` y lo inserta por ti.
* **Flexibilidad**: Aunque tenga un valor por defecto, todavía puedes insertar el `id` que tú quieras (como el 89 de tu ejemplo). El valor por defecto solo actúa como un "plan de respaldo".
### **Try**
1. Crea la tabla:
```bash
cat 4-never_empty.sql | mysql hbtn_0d_2
```
2. Inserta solo el nombre para ver el DEFAULT en acción:
```bash
echo "INSERT INTO id_not_null (name) VALUES ('Julian');" | mysql hbtn_0d_2
```
3. Verifica el resultado:
```bash
echo "SELECT * FROM id_not_null;" | mysql hbtn_0d_2
```
### **Output**
```bash
id      name
1       Julian
```

### **Output**
```bash
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
1    Best
guillaume@ubuntu:~/$ 
```

---

## 5. Unique ID
Write a script that creates the table `unique_id` on your MySQL server.

-   `unique_id` description:
    +   `id` INT with the default value `1` and must be unique
    +   `name VARCHAR(256)`
    +   The database name will be passed as an argument of the mysql command
    +   If the table `unique_id` already exists, your script should not fail
`5-unique_id.sql`
```sql
-- Script that creates the table unique_id on your MySQL server
-- id INT with default value 1 and must be unique, name VARCHAR(256)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 5: Unique ID)

* **`id INT DEFAULT 1 UNIQUE`**: Estamos aplicando dos reglas a la misma columna:
    1. **`DEFAULT 1`**: Si no pones ID, MySQL pone un 1.
    2. **`UNIQUE`**: MySQL crea un índice interno para vigilar que **ningún valor de esa columna se repita** en toda la tabla.
* **Manejo del Error 1062 (Duplicate entry)**: En tu ejemplo, intentaste insertar el ID `89` dos veces. La primera vez entró sin problemas, pero la segunda vez el guardián `UNIQUE` saltó y dijo: "¡Alto! El 89 ya existe en mi lista, no puedo dejarte pasar".
* **Integridad de Datos**: Esta restricción es vital para identificar filas de forma inequívoca. Es el paso previo a entender las `PRIMARY KEYS` (Llaves Primarias).
* **Dato Curioso**: Si usas el `DEFAULT 1` una vez, funcionará. Si intentas insertar otra fila sin ID (confiando en el default), fallará, porque el segundo "1" rompería la regla de ser único.
### **Try**
1. Crea la tabla:
```bash
cat 5-unique_id.sql | mysql hbtn_0d_2
```
2. Inserta el primer registro:
```bash
echo "INSERT INTO unique_id (id, name) VALUES (89, 'Julian');" | mysql hbtn_0d_2
```
3. Intenta insertar el mismo ID otra vez:
```bash
echo "INSERT INTO unique_id (id, name) VALUES (89, 'Otro Julian');" | mysql hbtn_0d_2
```
### **Output**
```bash
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id    name
89    Best School
guillaume@ubuntu:~/$ 
```

---

##  6. States table
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
-   `states` description:
    +   `id` INT unique, auto generated, can't be null and is a primary key
    +   `name VARCHAR(256)` can't be null
    +   If the database `hbtn_0d_usa` already exists, your script should not fail
    +   If the table `states` already exists, your script should not fail
`6-states.sql`
```sql
-- Script that creates the database hbtn_0d_usa and the table states
-- id INT unique, auto generated, can't be null and is a primary key
-- name VARCHAR(256) can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 6: States table)

* **`USE hbtn_0d_usa`**: Es fundamental. Como el script crea la base de datos, debemos decirle explícitamente a MySQL: "A partir de ahora, todo lo que haga es dentro de esta nueva carpeta".
* **`AUTO_INCREMENT`**: Esta es la "magia". Al insertar un estado, no necesitas pasar el `id`. MySQL lleva un contador interno y le asigna el siguiente número disponible automáticamente.
* **`PRIMARY KEY (id)`**: Es la restricción reina. Una llave primaria:
    1. Es obligatoriamente **ÚNICA**.
    2. **No puede ser NULL**.
    3. Es el **índice principal** que usa MySQL para buscar datos a toda velocidad.
* **`NOT NULL`**: Aplicado tanto al `id` como al `name`, asegura que nunca tengamos estados "fantasma" o sin identificación en nuestra base de datos de USA.
* **Relación con tu cuenta de Wise/BNP**: Imagina que cada transacción tiene un ID único autoincremental; así es como los bancos aseguran que no se confunda una compra de comida con el pago del alquiler.
### **Try**
1. Ejecuta el script completo:
```bash
cat 6-states.sql | mysql
```
2. Inserta nombres de estados sin poner el ID:
```bash
echo "INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');" | mysql hbtn_0d_usa
```
3. Verifica la magia del auto-incremento:
```bash
echo "SELECT * FROM states;" | mysql hbtn_0d_usa
```
### **Output**
```bash
id      name
1       California
2       Arizona
3       Texas
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    name
1    California
2    Arizona
3    Texas
guillaume@ubuntu:~/$ 
```

---

##  7. Cities table
Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

-   `cities` description:
    +   `id INT` unique, auto generated, can't be null and is a primary key
    +   `state_id INT`, can't be null and must be a `FOREIGN KEY` that references to id of the states table
    +   `name VARCHAR(256)` can't be null
    +   If the database `hbtn_0d_usa` already exists, your script should not fail
    +   If the table `cities` already exists, your script should not fail
`7-cities.sql`
```sql

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 7: Cities table)

* **`FOREIGN KEY (state_id) REFERENCES states(id)`**: Esta línea establece la regla de integridad referencial. Dice: "El valor que pongas en `state_id` debe existir previamente en la columna `id` de la tabla `states`".
* **Manejo del Error 1452 (Cannot add or update a child row)**: 
    * En tu ejemplo, intentaste insertar Paris con `state_id = 10`.
    * MySQL fue a la tabla `states`, buscó el ID 10 y no lo encontró (solo tenías el 1, 2 y 3 de la tarea anterior).
    * El sistema bloqueó la operación para evitar datos huérfanos. No permite que una ciudad apunte a un estado que no existe.
* **Integridad Referencial**: Esto es lo que evita, por ejemplo, que en tu cuenta de BNP Paribas se intente registrar un gasto en un "LEP" que no ha sido abierto. Los datos deben ser coherentes entre sí.
* **Orden de Creación**: Para que este script funcione, la tabla `states` debe existir antes que `cities`. Como las tareas son progresivas, MySQL ya tiene la tabla padre lista.
### **Try**
1. Ejecuta el script:
```bash
cat 7-cities.sql | mysql
```
2. Prueba un caso exitoso (California es ID 1):
```bash
echo "INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');" | mysql hbtn_0d_usa
```
3. Prueba el error (No existe el estado 10):
```bash
echo "INSERT INTO cities (state_id, name) VALUES (10, 'Paris');" | mysql hbtn_0d_usa
```
### ** My Output**
```bash
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
```
### **Output Expected**
```bash
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    state_id    name
1    1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    state_id    name
1    1   San Francisco
guillaume@ubuntu:~/$ 
```

---

##  8. Cities of California
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

-   The `states` table contains only one record where `name` = `California` (but the id can be different, as per the example)
-   Results must be sorted in ascending order by `cities.id`
-   You are not allowed to use the `JOIN` keyword
-   The database name will be passed as an argument of the `mysql` command  

`8-cities_of_california_subquery.sql`
```sql
-- Script that lists all cities of California found in hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results are sorted in ascending order by cities.id
-- JOIN keyword is not allowed

SELECT id, name 
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 8: Cities of California)

* **Subquery (La consulta interna)**: `SELECT id FROM states WHERE name = 'California'`. 
    * MySQL ejecuta esto primero. 
    * Busca en la tabla de estados cuál es el ID numérico de California (en tu ejemplo es el `1`).
* **Main Query (La consulta externa)**: `SELECT id, name FROM cities WHERE state_id = (...)`.
    * Una vez que MySQL sabe que el ID es `1`, la consulta se convierte internamente en: `WHERE state_id = 1`.
    * Así obtenemos las ciudades de California sin haber usado nunca un `JOIN`.
* **Restricción "No JOIN"**: Esta técnica es muy útil cuando necesitas filtrar datos basados en otra tabla pero no necesitas mostrar columnas de esa segunda tabla. 
* **Ordenamiento**: El `ORDER BY id ASC` asegura que los resultados aparezcan en el orden en que las ciudades fueron creadas (1, 2, 3...).

### 🔍 Tips de Estilo SQL (Identación)

* **Alineación a la derecha**: Muchos desarrolladores alinean las palabras clave (`SELECT`, `FROM`, `WHERE`) a la derecha para que los nombres de las columnas queden en una columna visual recta. Esto facilita la lectura rápida.
* **Subconsultas**: Es una excelente práctica poner los paréntesis de la subquery en líneas diferentes o identar todo el bloque interno. Esto ayuda a identificar visualmente que esa parte del código es "hija" de la consulta principal.
* **Mayúsculas**: Como bien hiciste, mantener las palabras reservadas (`SELECT`, `FROM`, `WHERE`, `ORDER BY`, `ASC`) en **MAYÚSCULAS** es un requisito estricto en este proyecto de Holberton.
* **Punto y coma ( ; )**: No olvides terminar siempre con `;`. Aunque en un script de una sola línea a veces se olvida, es el estándar para separar múltiples sentencias.

### 🔍 Legibilidad en SQL: ¿Por qué identar?

1. **Jerarquía Visual**: La identación en la subquery te permite ver instantáneamente qué parte depende de qué. Si no identas, cuando tengas 3 o 4 subqueries anidadas, será imposible saber dónde cierra cada paréntesis.
2. **Depuración (Debugging)**: Si tienes un error de sintaxis, es mucho más fácil comentar una línea específica (con `--`) para probar si el resto de la consulta funciona si cada cláusula está en su propio renglón.
3. **Estándares de Holberton**: El "Betty" de SQL no es tan estricto como en C, pero los revisores valoran que el código sea limpio. Un código bien identado grita: "Sé lo que estoy haciendo".
4. **Mantenimiento**: Mañana podrías querer agregar un `AND population > 100000`. Si tienes el `WHERE` bien identificado, sabes exactamente dónde insertarlo.
### **Try**
1. Verifica que California existe:
```bash
echo "SELECT * FROM states;" | mysql hbtn_0d_usa
```
### **Output**
```bash
id      name
1       California
2       Arizona
3       Texas
```
2. Ejecuta tu script:
```bash
cat 8-cities_of_california_subquery.sql | mysql hbtn_0d_usa
```
### **Output**
```bash
id      name
1       San Francisco
```


### **Output**
```bash
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    name
1    California
2    Arizona
3    Texas
4    Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    state_id    name
1    1   San Francisco
2    1   San Jose
4    2   Page
6    3   Paris
7    3   Houston
8    3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    name
1    San Francisco
2    San Jose
guillaume@ubuntu:~/$ 
```

---

##  9. Cities by States
Write a script that lists all cities contained in the database `hbtn_0d_usa`.
-   Each record should display: `cities.id` - `cities.name` - `states.name`
-   Results must be sorted in ascending order by `cities.id`
-   You can use only one SELECT statement
-   The database name will be passed as an argument of the `mysql` command
`9-cities_by_state_join.sql`
```sql
-- Script that lists all cities in hbtn_0d_usa
-- Display: cities.id - cities.name - states.name
-- Sorted by cities.id ASC
-- Only one SELECT statement allowed

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

```

### **Logica**
### 🔍 ¿Qué está pasando aquí? (Task 9: Cities by States)

* **El `JOIN` (o INNER JOIN)**: Es la operación que combina filas de dos tablas. MySQL busca coincidencias basándose en una condición lógica.
* **La cláusula `ON`**: Es el "pegamento". Aquí le decimos: "Une la fila de la ciudad con la fila del estado donde el `state_id` de la ciudad coincida exactamente con el `id` del estado".
* **Ambigüedad de nombres**: Notarás que ambas tablas tienen una columna llamada `name`. 
    * Para evitar confusiones, usamos la sintaxis `tabla.columna` (ej. `cities.name` y `states.name`).
    * En el resultado verás dos columnas llamadas "name", eso es normal según el ejemplo de Holberton.
* **Solo un `SELECT`**: Al usar `JOIN`, cumplimos el requisito de hacer todo en una sola sentencia, siendo mucho más eficiente que hacer subqueries cuando necesitamos datos de múltiples tablas.
### 🔗 Funcionamiento del JOIN (Explicación Julian)

* **Punto de Encuentro**: `cities.state_id = states.id` es la condición de igualdad.
* **Proceso**:
    1. MySQL escanea `cities`.
    2. Usa el `state_id` como "puntero" hacia la tabla `states`.
    3. Si hay coincidencia, fusiona las filas temporalmente.
* **Resultado**: El usuario no ve los IDs de unión (state_id), sino los nombres legibles de ambas tablas.
* **IMPORTANTE**: No se crea una "tabla" nueva físicamente, es solo una respuesta temporal que MySQL te da en la terminal.

-   `JOIN states ON cities.state_id = states.id`: Busca cada fila de ciudades y, si el número de su estado coincide con el ID de la tabla de estados, pégalas en una sola fila larga

### 🖥️ Trabajo con Vistas (Views) en MySQL

Las vistas son consultas almacenadas. Son útiles para simplificar el acceso a datos complejos.

* **Creación vía Terminal**: Se puede inyectar el código SQL directamente usando `echo`.
* **Alias (`AS`)**: En la vista usamos `cities.name AS city_name`. Esto es vital cuando dos tablas tienen columnas con el mismo nombre, permitiendo diferenciarlas en el resultado final.
* **Persistencia**: Una vez creada la vista, permanece en la base de datos `hbtn_0d_usa` hasta que la borres con `DROP VIEW`.
* **Borrar una Vista**: Si te equivocas y quieres repetirla, usa:
  `echo "DROP VIEW IF EXISTS view_cities_with_states;" | mysql hbtn_0d_usa`

### **Try**
#### Paso 1: Agregar los estados faltantes
```bash
echo "INSERT INTO states (name) VALUES ('Utah');" | mysql hbtn_0d_usa
```
#### Paso 2: Agregar las ciudades faltantes
```bash
echo "INSERT INTO cities (state_id, name) VALUES (2, 'Page'), (3, 'Paris'), (3, 'Houston'), (3, 'Dallas');" | mysql hbtn_0d_usa
```
1. 
```bash
echo 'SELECT * FROM states;' | mysql hbtn_0d_usa
```
### **Output**
```bash
id      name
1       California
2       Arizona
3       Texas
```

2. 
```bash
echo 'SELECT * FROM cities;' | mysql hbtn_0d_usa
```
### **Output**
```bash
```bash
id    state_id    name
1    1   San Francisco
2    1   San Jose
4    2   Page
6    3   Paris
7    3   Houston
8    3   Dallas
```

3. Ejecuta el script:
```bash
cat 9-cities_by_state_join.sql | mysql hbtn_0d_usa
```
### **Output**
```bash
id    name    name
1    San Francisco   California
2    San Jose    California
4    Page    Arizona
6    Paris   Texas
7    Houston Texas
8    Dallas  Texas
```

### **Output Expected**
```bash
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    name
1    California
2    Arizona
3    Texas
4    Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    state_id    name
1    1   San Francisco
2    1   San Jose
4    2   Page
6    3   Paris
7    3   Houston
8    3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id    name    name
1    San Francisco   California
2    San Jose    California
4    Page    Arizona
6    Paris   Texas
7    Houston Texas
8    Dallas  Texas
guillaume@ubuntu:~/$ 
```

---

##  10. Genre ID by show
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: `download`

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

-   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
-   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
-   You can use only one `SELECT` statement
-   The database name will be passed as an argument of the `mysql` command
`10-genre_id_by_show.sql`
```sql
-- Script that lists all shows in hbtn_0d_tvshows that have at least one genre linked
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement allowed

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

```

### **Logica**
### 🔍 Relaciones Muchos a Muchos (Many-to-Many)

En esta base de datos tienes tres tablas principales:
1. **`tv_shows`**: Contiene los nombres de las series (`id`, `title`).
2. **`tv_genres`**: Contiene los nombres de los géneros (`id`, `name`).
3. **`tv_show_genres`**: Es la **Tabla Intermedia**. Solo tiene dos columnas: `show_id` y `genre_id`.

* **¿Por qué el JOIN funciona así?**: Al hacer `JOIN tv_shows` con `tv_show_genres`, MySQL busca cuántas veces aparece el ID de un show en la tabla intermedia. 
    * Si *Breaking Bad* (ID 1) aparece 4 veces en la tabla intermedia con géneros distintos, el `JOIN` creará 4 filas en tu resultado.
* **Filtro Implícito**: Al usar un `JOIN` simple (que es un `INNER JOIN`), las series que **no tienen ningún género** asignado en la tabla intermedia desaparecen automáticamente del resultado. Esto cumple con el requisito de "at least one genre linked".
* **Ordenamiento Doble**: Usamos `ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC`. Esto significa que primero ordena por nombre de la serie, y si la serie se repite (como *Dexter*), ordena sus géneros de menor a mayor.
### **Try**
#### 📂 Gestión de Dumps en MySQL

Para trabajar con los proyectos de Holberton que requieren bases de datos externas:

1. **Descarga**: `curl -L -o hbtn_0d_tvshows.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"`
2. **Creación**: `CREATE DATABASE nombre_db;`
3. **Importación**: `mysql nombre_db < nombre.sql`

* **Tip**: El símbolo `<` le indica a la terminal que el archivo `hbtn_0d_tvshows.sql` debe enviarse como entrada al comando `mysql`.
#### ¿Cómo verificar que todo está bien?
`echo "SHOW TABLES;" | mysql hbtn_0d_tvshows`

**Output**
```bash
Tables_in_hbtn_0d_tvshows
tv_genres
tv_show_genres
tv_shows
```


### **Output**
```bash
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title    genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter    1
Dexter    2
Dexter    6
Dexter    7
Dexter    8
Game of Thrones    1
Game of Thrones    3
Game of Thrones    4
House    1
House    2
New Girl    5
Silicon Valley    5
The Big Bang Theory    5
The Last Man on Earth    1
The Last Man on Earth    5
guillaume@ubuntu:~/$ 
```

---

##  11. Genre ID for all shows
Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

-   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
-   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
-   If a show doesn't have a genre, display NULL
-   You can use only one `SELECT` statement
-   The database name will be passed as an argument of the mysql command  

`11-genre_id_all_shows.sql`
```sql
-- Script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- If a show doesn't have a genre, displays NULL
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC

```

### **Logica**
# 🔄 Entendiendo el LEFT JOIN (Task 11)

### 💡 La Analogía del Salón de Clases
Imagina que la tabla de la izquierda (`tv_shows`) son los **alumnos** y la tabla de la derecha (`tv_show_genres`) son los **libros prestados**.

* **INNER JOIN (Task 10):** Solo muestra a los alumnos que **SÍ** tienen un libro. Si no tienes libro, no apareces en la lista.
* **LEFT JOIN (Task 11):** Muestra a **TODOS** los alumnos. Si el alumno no tiene libro, la lista dice `NULL` en la columna del libro.

---

### 🔍 Paso a Paso del Motor de MySQL

Cuando ejecutas un `LEFT JOIN`, el motor de base de datos sigue esta lógica:

1.  **Prioridad Izquierda**: Mira la tabla que pusiste inmediatamente después del `FROM` (`tv_shows`). Esta es tu "Tabla Maestra".
2.  **Escaneo**: Recorre cada show, uno por uno.
3.  **Búsqueda de Vínculo**: Para cada show, va a la tabla de la derecha (`tv_show_genres`) buscando coincidencias con el `ON tv_shows.id = tv_show_genres.show_id`.
4.  **Casos de Resultado**:
    * **Coincidencia encontrada**: Une las filas. Si el show tiene 3 géneros, verás el título del show 3 veces.
    * **Coincidencia NO encontrada**: El show no se borra. MySQL dice: *"No encontré nada, así que pondré un `NULL` para avisar que aquí no hay datos"* (Ejemplo: *Better Call Saul*).

---

### 🛠️ Diferencia Visual de Sintaxis

| Tipo de Join | Resultado para shows sin género |
| :--- | :--- |
| `JOIN` (Inner) | El show **desaparece** del reporte final. |
| `LEFT JOIN` | El show **aparece** con el valor `NULL`. |



### 📝 Por qué es útil en el mundo real
Como tú que usas **Wise**, imagina que quieres un reporte de todos tus "Contactos de Pago". 
* Si usas `JOIN`, solo verías a los amigos a los que ya les has enviado dinero.
* Si usas `LEFT JOIN`, verías a **todos tus amigos**, y los que nunca recibieron dinero tendrían un `NULL` en "Última Transacción". ¡Es mucho más útil para saber a quién te falta pagarle!
### **Try**
```bash
11-genre_id_all_shows.sql | mysql hbtn_0d_tvshows
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title    genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter    1
Dexter    2
Dexter    6
Dexter    7
Dexter    8
Game of Thrones    1
Game of Thrones    3
Game of Thrones    4
Homeland    NULL
House    1
House    2
New Girl    5
Silicon Valley    5
The Big Bang Theory    5
The Last Man on Earth    1
The Last Man on Earth    5
guillaume@ubuntu:~/$ 
```

---

##  12. No genre
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

-   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
-   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
-   You can use only one SELECT statement
-   The database name will be passed as an argument of the mysql command
`12-no_genre.sql`
```sql
-- Script that lists all shows in hbtn_0d_tvshows without a genre linked
-- Displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC

```

### **Logica**
# 🔍 Filtrando lo inexistente: IS NULL (Task 12)

Para encontrar los shows que **no tienen género**, seguimos una lógica de eliminación:

1.  **LEFT JOIN**: Primero, forzamos a que aparezcan todos los shows (los que tienen género y los que no).
2.  **El Estado NULL**: Como vimos antes, los shows sin género (como *Better Call Saul*) quedan con la columna `genre_id` vacía (`NULL`).
3.  **La Cláusula WHERE**: Aquí está el truco. Le decimos a MySQL: *"De toda esa lista gigante, solo quédate con las filas donde el género sea un fantasma (`IS NULL`)"*.

### ⚠️ Regla de Oro: `IS NULL` vs `= NULL`
En SQL, `NULL` no es un valor, es un **estado**. 
* ❌ **MAL**: `WHERE genre_id = NULL` (Esto nunca devolverá nada porque nada es "igual" a la nada).
* ✅ **BIEN**: `WHERE genre_id IS NULL` (Esto pregunta si el espacio está vacío).
### **Try**
```bash
cat 12-no_genre.sql | mysql hbtn_0d_tvshows
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title    genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$ 
```

---

##  13. Number of shows by genre
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-   Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-   First column must be called genre
-   Second column must be called number_of_shows
-   Don't display a genre that doesn't have any shows linked
-   Results must be sorted in descending order by the number of shows linked
-   You can use only one SELECT statement
-   The database name will be passed as an argument of the mysql command
`13-count_shows_by_genre.sql`
```sql
-- Script that lists all genres and the number of shows linked to each
-- First column: genre, Second column: number_of_shows
-- Don't display genres without shows
-- Sorted in descending order by the number of shows

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

```
### **Logica**
#### 📊 Contando y Agrupando: GROUP BY (Task 13)

Para esta tarea, no queremos ver cada conexión show-género por separado, sino que queremos "colapsarlas" para ver el total.

### 1. El JOIN (La Unión)
Unimos `tv_genres` con la tabla intermedia `tv_show_genres`. 
* **Nota**: Usamos `JOIN` (Inner Join) porque el ejercicio dice "Don't display a genre that doesn't have any shows linked". El Inner Join elimina automáticamente los géneros que no tienen coincidencias.

### 2. GROUP BY (El Agrupamiento)
Es como si pusieras todas las filas de la tabla unida en una mesa y empezaras a hacer montoncitos. Un montón para "Drama", otro para "Comedy", etc.
* `GROUP BY tv_genres.id` le dice a MySQL: "Haz un solo registro por cada género único".

### 3. COUNT (El Contador)
Mientras MySQL hace los montoncitos, el `COUNT()` va contando cuántas filas hay en cada uno.
* `COUNT(tv_show_genres.genre_id)` cuenta cuántas veces aparece ese género en la tabla de relaciones.

### 4. Alias (AS)
Usamos `AS genre` y `AS number_of_shows` para cumplir con el requisito de Holberton de que las columnas tengan nombres específicos.
### **Try**
```bash
cat 13-count_shows_by_genre.sql | mysql hbtn_0d_tvshows
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre    number_of_shows
Drama    5
Comedy    4
Mystery    2
Crime    2
Suspense    2
Thriller    2
Adventure    1
Fantasy    1
guillaume@ubuntu:~/$ 
```

---

##  14. My genres
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: `download` (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

-   The `tv_shows` table contains only one record where `title` = `Dexter` (but the id can be different)
-   Each record should display: `tv_genres.name`
-   Results must be sorted in ascending order by the genre name
-   You can use only one `SELECT` statement
-   The database name will be passed as an argument of the `mysql` command
`14-my_genres.sql`
```sql
-- Script that lists all genres of the show Dexter in the database hbtn_0d_tvshows
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

```

### **Logica**
# 🔗 El Triple Join: Navegando Relaciones N:N

En esta base de datos, la tabla `tv_genres` y la tabla `tv_shows` **no tienen ninguna columna en común**. Están separadas por un muro. La única forma de conectarlas es usando la tabla intermedia `tv_show_genres` como puente.

### 🗺️ La Ruta del Detective (Paso a paso)

1. **Punto de Partida (`tv_genres`)**: MySQL empieza mirando los nombres de los géneros.
2. **Primer Salto (`JOIN tv_show_genres`)**: Conecta el ID del género con la tabla de relaciones. Ahora sabe qué géneros están vinculados a qué IDs de shows.
3. **Segundo Salto (`JOIN tv_shows`)**: Conecta esos IDs de shows con la tabla final para poder leer los **títulos** (como "Dexter").
4. **El Filtro (`WHERE`)**: Una vez que todas las tablas están pegadas en una sola gran fila virtual, le decimos: *"Solo muéstrame las filas donde el título sea exactamente 'Dexter'"*.



---

### ⚠️ ¿Por qué INNER JOIN y no LEFT JOIN?
Usamos `INNER JOIN` porque solo nos interesan las filas donde exista una pareja perfecta en ambos lados. Si un género no tiene show, o un show no tiene género, no queremos verlo en este reporte específico.
### **Try**
```bash

```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$ 
```

---

##  15. Only Comedy
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: `download` (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

-   The `tv_genres` table contains only one record where `name` = `Comedy` (but the id can be different)
-   Each record should display: `tv_shows.title`
-   Results must be sorted in ascending order by the show title
-   You can use only one `SELECT` statement
-   The database name will be passed as an argument of the `mysql` command
`15-comedy_only.sql`
```sql
-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

```

### **Logica**
# 🎭 Filtrando por Género: El Triple Join (Task 15)

Para obtener solo los shows de "Comedy", MySQL realiza este recorrido:

1. **Selección de Tabla Base (`tv_shows`)**: Empezamos con la tabla que contiene los títulos que queremos mostrar.
2. **Conexión Intermedia (`JOIN tv_show_genres`)**: Unimos los shows con sus IDs de género.
3. **Conexión Final (`JOIN tv_genres`)**: Unimos con la tabla de nombres de géneros para poder preguntar por el nombre "Comedy".
4. **El Filtro Específico (`WHERE`)**: Descartamos todo lo que no sea 'Comedy'.

### 💡 Diferencia con la Task 14
* En la **Task 14**: Filtramos por `tv_shows.title = 'Dexter'` para obtener géneros.
* En la **Task 15**: Filtramos por `tv_genres.name = 'Comedy'` para obtener títulos.



---

### 🧪 ¿Por qué es importante el orden?
Aunque MySQL es inteligente, en Holberton aprendemos a escribir los JOINs siguiendo el "hilo" de la relación:
`tv_shows (id)` -> `tv_show_genres (show_id / genre_id)` -> `tv_genres (id)`.
### **Try**
```bash
cat 15-comedy_only.sql | mysql hbtn_0d_tvshows
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$ 
```

---

##  16. List shows and genres
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-   If a show doesn't have a genre, display `NULL` in the genre column
-   Each record should display: `tv_shows.title` - `tv_genres.name`
-   Results must be sorted in ascending order by the show title and genre name
-   You can use only one SELECT statement
-   The database name will be passed as an argument of the mysql command
`16-shows_by_genre.sql`
```sql
-- Script that lists all shows, and all genres linked to that show
-- If a show doesn't have a genre, displays NULL
-- Results are sorted by show title and genre name ASC

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC

```

### **Logica**
# 🏁 El Gran Cierre: Triple LEFT JOIN (Task 16)

En este ejercicio, el objetivo es mostrar **absolutamente todos** los shows, tengan o no tengan géneros vinculados.

### 🧩 La Lógica de la Cadena
1. **`FROM tv_shows`**: Esta es nuestra tabla ancla. Queremos ver todos los títulos de esta lista.
2. **Primer `LEFT JOIN tv_show_genres`**: 
   * Si usamos `INNER JOIN`, shows como *Better Call Saul* (que no tienen entrada en la tabla intermedia) desaparecerían.
   * Al usar `LEFT JOIN`, nos aseguramos de que el show permanezca en la lista aunque no encuentre su ID en la tabla intermedia.
3. **Segundo `LEFT JOIN tv_genres`**: 
   * Una vez que pasamos por la tabla intermedia, necesitamos saltar a la tabla de **nombres** de géneros. 
   * Usamos `LEFT JOIN` nuevamente para mantener la consistencia: si el paso anterior nos dio un "hueco" (NULL), este paso simplemente mantendrá ese NULL en la columna `name`.

### ⚖️ Resultado Final
* **Shows con géneros**: Aparecen tantas veces como géneros tengan (ej. *Breaking Bad* aparece 4 veces).
* **Shows sin géneros**: Aparecen una sola vez con un `NULL` en la columna `name` (ej. *Better Call Saul*).
### **Try**
```bash
cat 16-shows_by_genre.sql | mysql hbtn_0d_tvshows
```
### **Output**
```bash
guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title    name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter    Crime
Dexter    Drama
Dexter    Mystery
Dexter    Suspense
Dexter    Thriller
Game of Thrones    Adventure
Game of Thrones    Drama
Game of Thrones    Fantasy
Homeland    NULL
House    Drama
House    Mystery
New Girl    Comedy
Silicon Valley    Comedy
The Big Bang Theory    Comedy
The Last Man on Earth    Comedy
The Last Man on Earth    Drama
guillaume@ubuntu:~/$ 
```

---
---


```bash
cat 0-privileges.sql | mysql
cat 1-create_user.sql | mysql
cat 2-create_read_user.sql | mysql
cat 3-force_name.sql | mysql hbtn_0d_2
cat 4-never_empty.sql | mysql hbtn_0d_2
cat 5-unique_id.sql | mysql hbtn_0d_2
cat 6-states.sql | mysql
cat 7-cities.sql | mysql
echo "SELECT * FROM states;" | mysql hbtn_0d_usa
cat 8-cities_of_california_subquery.sql | mysql hbtn_0d_usa
cat 9-cities_by_state_join.sql | mysql hbtn_0d_usa
cat 10-genre_id_by_show.sql | mysql hbtn_0d_tvshows
cat 11-genre_id_all_shows.sql | mysql hbtn_0d_tvshows
cat 12-no_genre.sql | mysql hbtn_0d_tvshows
cat 13-count_shows_by_genre.sql | mysql hbtn_0d_tvshows
cat 14-my_genres.sql | mysql hbtn_0d_tvshows
cat 15-comedy_only.sql | mysql hbtn_0d_tvshows
cat 16-shows_by_genre.sql | mysql hbtn_0d_tvshows

```

### Tablas
#### tv_shows
`echo "SELECT * FROM tv_shows LIMIT 10;" | mysql hbtn_0d_tvshows`
**Output**
```bash
id      title
1       House
2       Game of Thrones
3       The Big Bang Theory
4       New Girl
5       Silicon Valley
```
#### tv_genres
`echo "SELECT * FROM tv_genres LIMIT 10;" | mysql hbtn_0d_tvshows`
**Output**
```bash
id      name
1       Drama
2       Mystery
3       Adventure
4       Fantasy
5       Comedy
```
#### tv_show_genres
`echo "SELECT * FROM tv_show_genres LIMIT 10;" | mysql hbtn_0d_tvshows`
**Output**
```bash
show_id genre_id
1       1
1       2
2       3
2       1
2       4
3       5
4       5
5       5
6       6
6       1
```
