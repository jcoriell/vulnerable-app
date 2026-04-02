from flask import Flask, request, redirect, url_for, session, render_template_string
import sqlite3
import os
from templates import HOME, LOGIN, REGISTER, DASHBOARD

app = Flask(__name__)
app.secret_key = "supersecretkey123"

DB = "users.db"

# --- Database setup ---
def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()

def get_db():
    return sqlite3.connect(DB)


# --- Routes ---

@app.route("/")
def home():
    return render_template_string(HOME)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Vulnerable: SQL injection
        conn = get_db()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password."

    return render_template_string(LOGIN, error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            error = "Username and password are required."
        else:
            conn = get_db()
            # Vulnerable: no duplicate check, plain-text passwords, SQL injection
            conn.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
            conn.commit()
            conn.close()
            success = f"Account created! You can now log in."

    return render_template_string(REGISTER, error=error, success=success)


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template_string(DASHBOARD, username=session["username"], user_id=session["user_id"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
