# from flask import Flask, render_template, request, redirect, session, url_for
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# def init_db():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE NOT NULL,
#         password TEXT NOT NULL
#     )''')
#     conn.commit()
#     conn.close()

# @app.route("/")
# def home():
#     if "username" in session:
#         return f"Привет, {session['username']}! <a href='/logout'>Выйти</a>"
#     return redirect("/login")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE username=?", (username,))
#         user = c.fetchone()
#         conn.close()

#         if user and check_password_hash(user[2], password):
#             session["username"] = username
#             return redirect("/")
#         else:
#             return "Неверный логин или пароль"

#     return render_template("login.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = generate_password_hash(request.form["password"])

#         try:
#             conn = sqlite3.connect("users.db")
#             c = conn.cursor()
#             c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             conn.close()
#             return redirect("/login")
#         except sqlite3.IntegrityError:
#             return "Пользователь уже существует"

#     return render_template("register.html")

# @app.route("/logout")
# def logout():
#     session.pop("username", None)
#     return redirect("/login")

# if __name__ == "__main__":
#     init_db()
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # замените на свой ключ

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    if 'username' in session:
        return f'Привет, {session["username"]}! <a href="/logout">Выйти</a>'
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect('/')
        else:
            return 'Неверные данные'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect('/login')
        except sqlite3.IntegrityError:
            return 'Имя пользователя уже занято'
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
