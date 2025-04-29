from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    # each call returns a fresh connection
    return psycopg2.connect(
        host     = os.environ['DB_HOST'],
        database = os.environ['DB_NAME'],
        user     = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        sslmode  = 'require'
    )

@app.route('/')
def show_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students ORDER BY id;")
    students = [ {'id': r[0], 'name': r[1]} for r in cur.fetchall() ]
    cur.close()
    conn.close()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
