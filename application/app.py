from flask import Flask, request, jsonify, render_template
import sqlite3
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')

@app.before_request
def count_requests():
    REQUEST_COUNT.inc()

def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        completed INTEGER)
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    conn = sqlite3.connect('tasks.db')
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    conn = sqlite3.connect('tasks.db')
    conn.execute("INSERT INTO tasks(title,completed) VALUES (?,0)", (task,))
    conn.commit()
    conn.close()
    return home()

@app.route("/complete/<int:id>")
def complete(id):
    conn = sqlite3.connect('tasks.db')
    conn.execute("UPDATE tasks SET completed=1 WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return home()

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect('tasks.db')
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return home()

@app.route("/metrics")
def metrics():
    return generate_latest()

@app.route("/health")
def health():
    return jsonify({"status":"UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)