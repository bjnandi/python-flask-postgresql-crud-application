from flask import Flask, render_template, request, url_for, flash, redirect
import psycopg2
from psycopg2.extras import DictCursor

app = Flask(__name__)
app.secret_key = 'many random bytes'

# PostgreSQL configuration
app.config['DB_NAME'] = 'crud'
app.config['DB_HOST'] = '34.202.71.117'
app.config['DB_USER'] = 'postgres'
app.config['DB_PASSWORD'] = '12345678'
app.config['DB_PORT'] = '5432'

def get_db_connection():
    conn = psycopg2.connect(
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT']
    )
    return conn

@app.route('/')
def Index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', students=data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('Index'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
        UPDATE students SET name=%s, email=%s, phone=%s
        WHERE id=%s
        """, (name, email, phone, id_data))
        conn.commit()
        cur.close()
        conn.close()
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))
    
# =======================================
# For code quality test by Sonarqube  
def badFunctionName(x):
    a = 0
    if x > 10:
        return True
    else:
        return False
# ========================================

if __name__ == "__main__":
    app.run(debug=True)
