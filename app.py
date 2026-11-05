from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DB_PATH = Path(__file__).with_name("tasks.db")


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def index():
    with get_db() as db:
        tasks = db.execute(
            "SELECT * FROM tasks ORDER BY completed ASC, created_at DESC"
        ).fetchall()
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    return render_template(
        "index.html", tasks=tasks, total=total, completed=completed
    )


@app.route("/tasks", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if not title:
        flash("Please enter a task title.", "error")
        return redirect(url_for("index"))

    if len(title) > 100:
        flash("Task titles must be 100 characters or fewer.", "error")
        return redirect(url_for("index"))

    with get_db() as db:
        db.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description)
        )
    flash("Task added.", "success")
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    with get_db() as db:
        task = db.execute(
            "SELECT completed FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        if task is None:
            flash("Task not found.", "error")
        else:
            db.execute(
                "UPDATE tasks SET completed = ? WHERE id = ?",
                (0 if task["completed"] else 1, task_id)
            )
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    with get_db() as db:
        db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    flash("Task deleted.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
