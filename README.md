# Python Flask PostgreSQL CRUD Application

This project is a web application built with Python Flask and PostgreSQL to manage student records.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/aaravchauhan18/python-flask-postgresql-crud-application.git
cd python-flask-postgresql-crud-application
```

2. **Set up the database**

Create a PostgreSQL database named crud.

```bash
CREATE TABLE students (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
phone VARCHAR(255) NOT NULL
);

INSERT INTO students (id, name, email, phone) VALUES
(1, 'Aarav Chauhan', 'aaravchauhan2211@gmail.com', '7310628048');
```

3. **Configure database settings in app.py** (e.g., DB_HOST, DB_USER, DB_PASSWORD).

4. **Install dependencies:**      
```bash
   pip install Flask psycopg2-binary

```   

4. **Start the Flask application:**

```bash
python app.py
```
