from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Connect to the Neon database
connection = psycopg2.connect(
    host     = os.environ['DB_HOST'],
    database = os.environ['DB_NAME'],
    user     = os.environ['DB_USER'],
    password = os.environ['DB_PASSWORD'],
    sslmode  = 'require'
)

@app.route('/')
def show_students():
    cur = connection.cursor()
    cur.execute("SELECT id, name FROM students ORDER BY id;")
    # Build a list of dicts, so Jinja can do student.name
    students = [ { 'id': r[0], 'name': r[1] } for r in cur.fetchall() ]
    cur.close()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    # bind 0.0.0.0 + use $PORT if Render gives you one
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
