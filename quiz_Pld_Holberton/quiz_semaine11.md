# REST API & Database Concepts — Explicaciones Completas

---

## Q0 — ¿Qué métodos HTTP corresponden a operaciones CRUD?
**Score: ✅ 1.0**

- [x] DELETE
- [ ] ~~KILL~~
- [ ] ~~REMOVE~~
- [x] POST
- [x] PUT / PATCH
- [ ] ~~ADD~~
- [x] GET
- [ ] ~~READ~~

> | HTTP | CRUD | Descripción |
> |------|------|-------------|
> | `GET` | **Read** | Obtener datos |
> | `POST` | **Create** | Crear un nuevo recurso |
> | `PUT / PATCH` | **Update** | Modificar un recurso existente |
> | `DELETE` | **Delete** | Eliminar un recurso |
>
> - ❌ `KILL`, `REMOVE`, `ADD`, `READ` — no son métodos HTTP válidos, son inventados.

---

## Q1 — ¿Cuáles son ventajas de usar un ORM?
**Score: ✅ 1.0**

- [x] Reduces need for raw SQL queries
- [ ] ~~Increases performance in all cases~~
- [ ] ~~Prevents all SQL injection attacks~~
- [x] Provides database abstraction

> - ✅ **Reduce la necesidad de SQL puro** — con un ORM escribís Python en vez de SQL.
> - ✅ **Provee abstracción de la base de datos** — podés cambiar de MySQL a PostgreSQL con mínimos cambios de código.
> - ❌ **NO aumenta el rendimiento en todos los casos** — en queries complejas el ORM puede ser más lento que SQL optimizado manualmente.
> - ❌ **NO previene todos los ataques de SQL injection** — ayuda, pero depende de cómo se use. No es una garantía total.

---

## Q2 — ¿En qué escenarios se usan comúnmente los JWT?
**Score: ✅ 1.0**

- [ ] ~~Storing user passwords~~
- [x] API authorization
- [ ] ~~Running database queries~~

> - ✅ **Autorización de APIs** — JWT es el estándar más usado para autenticar requests a APIs REST. El servidor genera un token cuando el usuario hace login, y el cliente lo envía en cada request en el header `Authorization: Bearer <token>`.
> - ❌ **Guardar contraseñas** — las contraseñas se hashean (bcrypt, argon2), nunca se guardan como JWT.
> - ❌ **Ejecutar queries** — JWT es un mecanismo de autenticación, no tiene ninguna relación con bases de datos.

---

## Q3 — ¿Cuáles son ventajas de RBAC?
**Score: ❌ 0.0**

- [x] Simplifies the assignment of permissions for large user bases.
- [ ] ~~Automatically encrypts all user credentials.~~
- [x] Makes it easy to visualize and manage which roles have access to which resources.

> - ✅ **Simplifica la asignación de permisos** — en vez de asignar permisos individualmente a cada usuario, se asignan roles (admin, editor, viewer) y cada rol tiene sus permisos. Mucho más fácil de gestionar con muchos usuarios.
> - ✅ **Fácil de visualizar y gestionar** — podés ver claramente qué rol tiene acceso a qué recurso sin revisar usuario por usuario.
> - ❌ **No encripta credenciales automáticamente** — RBAC es un modelo de control de acceso, no tiene absolutamente nada que ver con encriptación o hashing de contraseñas.

---

## Q4 — ¿Qué escenarios describen una relación uno-a-muchos?
**Score: ✅ 1.0**

- [x] A customer can place multiple orders, but each order belongs to only one customer.
- [x] A department can have multiple employees, but each employee belongs to only one department.
- [ ] ~~A student can enroll in multiple courses, and each course can have multiple students.~~
- [ ] ~~Each employee can work in multiple departments, and each department has multiple employees.~~

> Una relación **uno-a-muchos** significa que un registro de A puede relacionarse con muchos de B, pero cada B pertenece a solo uno de A.
>
> - ✅ **Cliente → Órdenes**: un cliente tiene muchas órdenes, pero cada orden pertenece a un solo cliente. (1:N)
> - ✅ **Departamento → Empleados**: un departamento tiene muchos empleados, pero cada empleado pertenece a un solo departamento. (1:N)
> - ❌ **Estudiante ↔ Cursos**: es **muchos-a-muchos** (N:M) — un estudiante puede estar en muchos cursos Y un curso puede tener muchos estudiantes.
> - ❌ **Empleado ↔ Departamentos**: también es **muchos-a-muchos** (N:M).

---

## Q5 — ¿Cómo agregar una nueva columna job_title a la tabla users?
**Score: ✅ 1.0**

- [ ] ~~ADD TABLE users, job_title VARCHAR(5);~~
- [ ] ~~UPDATE TABLE users ADD job_title VARCHAR(5);~~
- [x] ALTER TABLE users ADD job_title VARCHAR(5);

> `ALTER TABLE` es el comando DDL para modificar la estructura de una tabla existente:
> ```sql
> ALTER TABLE nombre_tabla ADD nombre_columna TIPO;
> ```
> - ❌ `ADD TABLE` — no existe como comando SQL.
> - ❌ `UPDATE TABLE` — `UPDATE` es DML, se usa para modificar **datos**, no la estructura de la tabla.

---

## Q6 — ¿El hashing es reversible o irreversible?
**Score: ✅ 1.0**

- [ ] ~~Hashing is reversible with the right private key.~~
- [x] Hashing is irreversible because it is a one-way function designed not to be decrypted.
- [ ] ~~Hashing is reversible if the algorithm is strong enough.~~

> El **hashing** es una función de **una sola vía** — tomás un input y obtenés un hash, pero no podés reconstruir el input original.
> ```
> "password123"  →  bcrypt  →  "$2b$12$abc..."  ✅
> "$2b$12$abc..."  →  ???   →  "password123"     ❌ imposible
> ```
> - ❌ **Reversible con la clave privada** — eso describe la **encriptación asimétrica**, no el hashing.
> - ❌ **Reversible si el algoritmo es fuerte** — un algoritmo más fuerte hace el hashing MÁS difícil de revertir, no más fácil.

---

## Q7 — ¿Qué afirmaciones sobre SQL JOINs son verdaderas?
**Score: ❌ 0.0**

- [ ] ~~A JOIN clause is used to combine columns from the same table.~~
- [x] A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
- [ ] ~~A JOIN clause is used to combine different databases to create a new one based on the selected columns.~~

> - ✅ **JOIN combina filas de dos o más tablas** basándose en una columna relacionada (generalmente una FK).
> ```sql
> SELECT states.name, cities.name
> FROM states
> JOIN cities ON states.id = cities.state_id;
> ```
> - ❌ **No combina columnas de la misma tabla** — para manipular columnas de la misma tabla usás expresiones o subconsultas.
> - ❌ **No combina bases de datos** — JOIN opera dentro de la misma base de datos entre tablas relacionadas.

---

## Q8 — ¿Qué significa CRUD?
**Score: ✅ 1.0**

- [ ] ~~Compute, Refactor, Unlink, Debug~~
- [ ] ~~Collect, Review, Unify, Display~~
- [x] Create, Read, Update, Delete
- [ ] ~~Connect, Reorganize, Upgrade, Dispose~~

> CRUD son las 4 operaciones básicas de cualquier sistema que maneja datos:
>
> | Letra | Operación | SQL | HTTP |
> |-------|-----------|-----|------|
> | C | **C**reate | INSERT | POST |
> | R | **R**ead | SELECT | GET |
> | U | **U**pdate | UPDATE | PUT/PATCH |
> | D | **D**elete | DELETE | DELETE |
>
> Las otras opciones son combinaciones de palabras inventadas sin relación con el concepto.

---

## Q9 — ¿Cuál es un ejemplo de relación muchos-a-muchos?
**Score: ✅ 1.0**

- [ ] ~~A user has one profile.~~
- [ ] ~~A product can have one category, and a category can have many products.~~
- [x] A product can belong to multiple categories, and a category can have many products.
- [ ] ~~A customer can have multiple orders, but an order belongs to exactly one customer.~~

> Una relación **muchos-a-muchos** significa que múltiples registros de A se relacionan con múltiples de B, y viceversa. Se implementa con una tabla intermedia:
> ```
> products ──── product_categories ──── categories
>                  (tabla intermedia)
> ```
> - ❌ **Usuario → Perfil**: es **uno-a-uno** (1:1).
> - ❌ **Producto → Una categoría**: es **uno-a-muchos** (1:N) — un producto tiene UNA categoría.
> - ❌ **Cliente → Órdenes**: es **uno-a-muchos** (1:N) — cada orden pertenece a un solo cliente.

---

## Q10 — ¿Qué significa JWT?
**Score: ✅ 1.0**

- [ ] ~~Java Web Token~~
- [ ] ~~JWT Web Transformer~~
- [x] JSON Web Token

> **JWT** = **JSON Web Token**. Es un estándar abierto (RFC 7519) para transmitir información entre partes de forma segura como un objeto JSON firmado digitalmente.
>
> - ❌ **Java** Web Token — no tiene nada que ver con Java. Funciona con cualquier lenguaje.
> - ❌ **JWT Web Transformer** — no existe, es inventado.

---

## Q11 — ¿Qué escenario describe una relación uno-a-uno?
**Score: ✅ 1.0**

- [ ] ~~Each employee works in exactly one department, and each department has many employees.~~
- [x] Each passport is assigned to exactly one person, and each person has exactly one passport.
- [ ] ~~Each order can have multiple items, but each item belongs to a single order.~~

> Una relación **uno-a-uno** significa que cada registro de A corresponde a exactamente un registro de B, y viceversa.
>
> - ✅ **Persona ↔ Pasaporte**: una persona tiene exactamente un pasaporte y un pasaporte pertenece a exactamente una persona. (1:1)
> - ❌ **Empleado → Departamento**: es **uno-a-muchos** — un departamento tiene MUCHOS empleados. (1:N)
> - ❌ **Orden → Items**: es **uno-a-muchos** — una orden tiene MUCHOS items. (1:N)

---

## Q12 — ¿Qué tipos de relaciones existen en diagramas ER?
**Score: ✅ 1.0**

- [x] One-to-One
- [x] One-to-Many
- [ ] ~~Zero-to-Zero~~
- [x] Many-to-Many

> Los 3 tipos de relaciones estándar en modelado de bases de datos son:
>
> | Tipo | Notación | Ejemplo |
> |------|----------|---------|
> | **One-to-One** (1:1) | `──────` | Persona ↔ Pasaporte |
> | **One-to-Many** (1:N) | `──────<` | Departamento → Empleados |
> | **Many-to-Many** (N:M) | `>──────<` | Estudiantes ↔ Cursos |
>
> - ❌ **Zero-to-Zero** — no existe como tipo de relación en modelado ER. Es un concepto inventado.

---

## Q13 — ¿Cómo actualizar el email del usuario con id = 1919?
**Score: ✅ 1.0**

- [ ] ~~UPDATE email = 'newadresse@mail.com' WHERE id = 1;~~
- [x] UPDATE users SET email = 'newadresse@mail.com' WHERE id = 1919;
- [ ] ~~SET UPDATE email = 'newadresse@mail.com' WHERE id = 1919;~~

> La sintaxis correcta de `UPDATE` es:
> ```sql
> UPDATE nombre_tabla SET columna = valor WHERE condicion;
> ```
> - ❌ Primera opción: no especifica la tabla y usa `id = 1` en vez de `id = 1919`.
> - ❌ Tercera opción: invierte el orden con `SET UPDATE`, que no es sintaxis SQL válida.
> - ⚠️ Siempre usar `WHERE` con `UPDATE` — sin él se actualizarían **todos** los registros de la tabla.

---

## Q14 — ¿Cómo cambiar el VARCHAR de job_title a 30?
**Score: ❌ 0.0**

- [x] ALTER TABLE users MODIFY COLUMN job_title VARCHAR(30);
- [x] ALTER TABLE users MODIFY job_title VARCHAR(30);
- [ ] ~~UPDATE TABLE users COLUMN job_title VARCHAR(30);~~

> En MySQL, ambas sintaxis son válidas — la palabra `COLUMN` es **opcional**:
> ```sql
> ALTER TABLE users MODIFY COLUMN job_title VARCHAR(30);  -- válido ✅
> ALTER TABLE users MODIFY job_title VARCHAR(30);          -- válido ✅
> ```
> - ❌ `UPDATE TABLE users COLUMN ...` — `UPDATE` es DML (modifica datos), no DDL (modifica estructura). Para cambiar la definición de una columna siempre se usa `ALTER TABLE`.

---

## Q15 — ¿Qué es un ORM?
**Score: ✅ 1.0**

- [x] Is a code library that automates the transfer of data stored in relational databases tables into objects.
- [x] Provides a high-level abstraction upon a relational database.
- [x] Allows a developer to write Python code instead of SQL (for Python ORM).

> Las tres afirmaciones son correctas:
> - ✅ **Automatiza la transferencia** de datos de tablas a objetos Python — cada fila se convierte en una instancia de clase.
> - ✅ **Abstrae la base de datos** — podés cambiar de MySQL a PostgreSQL cambiando solo la cadena de conexión.
> - ✅ **Reemplaza SQL con Python** — en vez de `SELECT * FROM states` escribís `session.query(State).all()`.

---

## Q16 — ¿Cuáles son los componentes de un JWT?
**Score: ❌ 0.0**

- [x] Header
- [x] Payload
- [ ] ~~Encryption Key~~
- [x] Signature

> Un JWT tiene exactamente **3 partes** separadas por puntos (`.`):
> ```
> eyJhbGciOiJIUzI1NiJ9  .  eyJ1c2VyX2lkIjoxfQ  .  SflKxwRJSMeKKF2QT4
>  ↑ Header (base64)         ↑ Payload (base64)     ↑ Signature
> ```
>
> | Parte | Contenido |
> |-------|-----------|
> | **Header** | Algoritmo (ej: HS256) y tipo de token |
> | **Payload** | Datos/claims (ej: user_id, rol, expiración) |
> | **Signature** | Verifica que el token no fue modificado |
>
> - ❌ **Encryption Key** — la clave secreta se usa para **firmar** el token, pero no va dentro del JWT como componente. Queda en el servidor.

---

## Q17 — ¿Cuándo usar RBAC?
**Score: ✅ 1.0**

- [x] When different categories of users (e.g., admin, manager, employee) have distinct sets of permissions.
- [ ] ~~When there is only one type of user and no need to differentiate permissions.~~

> **RBAC** es ideal cuando tenés distintos tipos de usuarios con diferentes niveles de acceso:
> ```
> admin    → leer, escribir, eliminar, gestionar usuarios
> manager  → leer y escribir
> employee → solo leer
> ```
> - ❌ **Si hay solo un tipo de usuario** sin diferencias de permisos, RBAC es innecesario y añade complejidad sin beneficio — sería sobre-ingeniería.
