# Python - Object Relational Mapping

## Description

This project explores the connection between Python and MySQL databases using two approaches:

1. **MySQLdb** — connecting directly to MySQL and executing raw SQL queries from Python
2. **SQLAlchemy ORM** — interacting with the database using Python objects instead of SQL queries

The biggest advantage of ORM is abstraction: instead of writing `SELECT * FROM states`, you write `session.query(State).all()` — no SQL needed, just Python objects.

---

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- MySQL 8.0
- Ubuntu 20.04 LTS

### Installation

```bash
# Install MySQLdb
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# Install SQLAlchemy
sudo pip3 install SQLAlchemy==1.4.22
```

---

## Files

### Models

| File | Description |
|------|-------------|
| `model_state.py` | Defines the `State` class linked to the `states` MySQL table |
| `model_city.py` | Defines the `City` class linked to the `cities` MySQL table |

---

## Tasks

### Task 0 — List databases
**File:** `0-list_databases.sql`

Lists all databases of the MySQL server.

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

---

### Task 1 — Filter states
**File:** `1-filter_states.py`

Lists all states with a name starting with `N` (upper N) from `hbtn_0e_0_usa`, sorted by `states.id`.

```bash
./1-filter_states.py <mysql_username> <mysql_password> <database_name>
```

```
(4, 'New York')
(5, 'Nevada')
```

---

### Task 2 — Filter states by user input
**File:** `2-my_filter_states.py`

Lists all states matching the name passed as argument. Uses `.format()` to build the SQL query.

```bash
./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
```

```
(2, 'Arizona')
```

---

### Task 3 — SQL Injection free
**File:** `3-my_safe_filter_states.py`

Same as Task 2 but safe from SQL injection. Uses `%s` parameterized queries instead of `.format()`.

```bash
./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
```

> Using `.format()` is vulnerable — a malicious input like `"Arizona'; TRUNCATE TABLE states; --"` would execute the TRUNCATE. Parameterized queries prevent this by treating input as a string literal, never as SQL code.

---

### Task 6 — First state model
**File:** `model_state.py`

Python file containing the `State` class definition and `Base = declarative_base()` instance using SQLAlchemy ORM.

```python
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
```

---

### Task 7 — All states via SQLAlchemy
**File:** `7-model_state_fetch_all.py`

Lists all `State` objects from `hbtn_0e_6_usa`, sorted by `states.id` using SQLAlchemy ORM.

```bash
./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
```

```
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

---

### Task 8 — First state
**File:** `8-model_state_fetch_first.py`

Prints the first `State` object from `hbtn_0e_6_usa` ordered by `states.id`. Prints `Nothing` if the table is empty.

```bash
./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
```

```
1: California
```

> Uses `.first()` which generates `LIMIT 1` in SQL — does NOT fetch all states first.

---

### Task 9 — Contains `a`
**File:** `9-model_state_filter_a.py`

Lists all `State` objects containing the letter `a` in their name, sorted by `states.id`.

```bash
./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
```

```
1: California
2: Arizona
3: Texas
5: Nevada
```

---

### Task 10 — Get a state
**File:** `10-model_state_my_get.py`

Prints the `id` of the `State` object matching the name passed as argument. Prints `Not found` if no match exists. Safe from SQL injection.

```bash
./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
```

```
# Found
3

# Not found
Not found
```

---

### Task 11 — Add a new state
**File:** `11-model_state_insert.py`

Adds the `State` object `"Louisiana"` to `hbtn_0e_6_usa` and prints its new `id`.

```bash
./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
```

```
6
```

---

### Task 12 — Update a state
**File:** `12-model_state_update_id_2.py`

Changes the name of the `State` where `id = 2` to `New Mexico`.

```bash
./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
```

---

### Task 13 — Delete states
**File:** `13-model_state_delete_a.py`

Deletes all `State` objects with a name containing the letter `a`.

```bash
./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
```

```
# After deletion, only states without 'a' remain:
2: New Mexico
4: New York
```

---

### Task 14 — Cities in state
**Files:** `model_city.py`, `14-model_city_fetch_by_state.py`

`model_city.py` defines the `City` class linked to the `cities` table, with a Foreign Key referencing `states.id`.

`14-model_city_fetch_by_state.py` prints all `City` objects with their state name, sorted by `cities.id`.

```bash
./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
```

```
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
...
```

---

## Key Concepts

### MySQLdb vs SQLAlchemy

| Action | MySQLdb | SQLAlchemy |
|--------|---------|-----------|
| Connect | `MySQLdb.connect(host, user, passwd, db)` | `create_engine('mysql+mysqldb://user:pass@localhost/db')` |
| Query | `cursor.execute("SELECT * FROM states")` | `session.query(State).all()` |
| Access data | `row[0]`, `row[1]` | `state.id`, `state.name` |
| Insert | `cursor.execute("INSERT ...")` + `db.commit()` | `session.add(obj)` + `session.commit()` |
| Update | `cursor.execute("UPDATE ...")` + `db.commit()` | `obj.attr = value` + `session.commit()` |
| Delete | `cursor.execute("DELETE ...")` + `db.commit()` | `session.delete(obj)` + `session.commit()` |

### SQLAlchemy CRUD

```python
# CREATE
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()

# READ
states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

# UPDATE
state = session.query(State).filter(State.id == 2).first()
state.name = "New Mexico"
session.commit()

# DELETE
states = session.query(State).filter(State.name.like('%a%')).all()
for state in states:
    session.delete(state)
session.commit()
```

---

## Author
**Julian** — Holberton School C#28
