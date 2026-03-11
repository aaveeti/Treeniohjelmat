import sqlite3
import db
import config
import programs
from flask import Flask
from flask import render_template, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_programs = programs.get_programs()
    return render_template("index.html", programs=all_programs)

@app.route("/program/<int:program_id>")
def show_program(program_id):
    program = programs.get_program(program_id)
    return render_template("show_program.html", program=program)

@app.route("/new_program")
def new_program():
    levels_data = db.get_levels()
    workout_type_data = db.get_workout_type()
    return render_template("new_program.html", levels=levels_data, types=workout_type_data)

@app.route("/create_program", methods=["POST"])
def create_program():
    user_id = session.get("user_id")
    title = request.form["title"]
    content = request.form["content"]
    level_name = request.form["experience"]
    level_result = db.query("SELECT id FROM levels WHERE title = ?", [level_name])
    type_name = request.form["workout_type"]
    type_result = db.query("SELECT id FROM workout_types WHERE title = ?", [type_name])

    level_id = level_result[0]["id"]
    type_id = type_result[0]["id"]

    programs.add_program(title, content, user_id, level_id, type_id)
    
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    result = db.query("SELECT id, password_hash FROM users WHERE username = ?", [username])
    
    if not result:
        return "VIRHE: väärä tunnus tai salasana"
    
    user = result[0]
    
    if check_password_hash(user["password_hash"], password):
        session["username"] = username
        session["user_id"] = user["id"]
        return redirect("/")
    else:
        return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")