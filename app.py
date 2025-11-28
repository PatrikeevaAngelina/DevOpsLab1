from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'db'),
        database=os.getenv('POSTGRES_DB', 'testdb'),
        user=os.getenv('POSTGRES_USER', 'testuser'),
        password=os.getenv('POSTGRES_PASSWORD', 'testpass')
    )
    return conn

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return "Привет Докер и postgres!"
    except Exception as e:
        return f"Извините, но подключения к базе не случилось :( Ошибка: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
