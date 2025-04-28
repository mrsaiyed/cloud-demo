from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Connect to the Neon database
connection = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    sslmode='require'
)

@app.route('/')
def hello():
    cursor = connection.cursor()
    cursor.execute('SELECT message FROM hello LIMIT 1;')
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 'No message found in database.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
