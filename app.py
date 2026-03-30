import sqlite3
import secrets
import math
import markupsafe

from flask import Flask
from flask import render_template, redirect, request, session, abort, flash

import db
import config
import programs
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br>")
    return markupsafe.Markup(content)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    page_size = 10
    program_count = programs.program_count()
    page_count = math.ceil(program_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    all_programs = programs.get_programs(page, page_size)
    return render_template("index.html", programs=all_programs, page=page, page_count=page_count)

@app.route("/user/<int:user_id>")
@app.route("/user/<int:user_id>/<int:page>")
def show_user(user_id, page=1):
    user = users.get_user(user_id)
    if not user:
        abort(404)

    page_size = 10
    program_count = programs.user_program_count(user_id)
    page_count = math.ceil(program_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect(f"/user/{user_id}/1")
    if page > page_count:
        return redirect(f"/user/{user_id}/{page_count}")

    user_programs = users.get_programs(user_id, page=page, page_size=page_size)

    return render_template("show_user.html", user=user, programs=user_programs,
                           program_count=program_count, page=page, page_count=page_count)

@app.route("/program/<int:program_id>")
def show_program(program_id):
    program = programs.get_program(program_id)
    categories = programs.get_categories(program_id)
    all_comments = programs.get_comments(program_id)

    if not program:
        abort(404)
    return render_template("show_program.html", program=program, level=categories["level"],
                            workout_type=categories["type"], comments=all_comments)

@app.route("/new_program")
def new_program():
    require_login()

    levels_data = db.get_levels()
    workout_type_data = db.get_workout_type()
    return render_template("new_program.html", levels=levels_data, types=workout_type_data)

@app.route("/create_program", methods=["POST"])
def create_program():
    require_login()
    check_csrf()

    user_id = session.get("user_id")
    title = request.form["title"]
    content = request.form["content"]
    level_id = request.form["experience"]
    type_id = request.form["workout_type"]

    if not title or len(title) > 50:
        abort(403)
    if not content or len(content) > 500:
        abort(403)

    programs.add_program(title, content, user_id, level_id, type_id)

    return redirect("/")

@app.route("/create_comment", methods=["POST"])
def create_comment():
    require_login()
    check_csrf()

    try:
        program_id = int(request.form["program_id"])
        rating = int(request.form["rating"])
    except (ValueError, KeyError):
        abort(400)

    program = programs.get_program(program_id)
    if not program:
        abort(403)

    user_id = session.get("user_id")
    comment = request.form["comment"]

    if not comment or len(comment) > 300:
        abort(400)
    if not 1 <= rating <= 5:
        abort(400)

    programs.add_comment(user_id, comment, rating, program_id)

    return redirect("/program/" + str(program_id))

@app.route("/delete_comment", methods=["POST"])
def delete_comment():
    require_login()
    check_csrf()

    comment_id = request.form["comment_id"]
    program_id = request.form["program_id"]
    comment = programs.get_comment(comment_id)

    if not comment or comment["user_id"] != session["user_id"]:
        abort(403)

    programs.delete_comment(comment_id, session["user_id"])

    return redirect("/program/" + str(program_id))

@app.route("/edit_program/<int:program_id>")
def edit_program(program_id):
    require_login()

    levels_data = db.get_levels()
    workout_type_data = db.get_workout_type()
    program = programs.get_program(program_id)
    if not program:
        abort(404)

    if program["user_id"] != session["user_id"]:
        abort(403)

    return render_template("edit_program.html", levels=levels_data,
                            types=workout_type_data, program=program)

@app.route("/update_program", methods=["POST"])
def update_program():
    require_login()
    check_csrf()
    program_id = request.form["program_id"]
    title = request.form["title"]
    content = request.form["content"]

    level_id = request.form["experience"]
    type_id = request.form["workout_type"]

    program = programs.get_program(program_id)
    if not program:
        abort(404)

    if program["user_id"] != session["user_id"]:
        abort(403)

    if not title or len(title) > 50:
        abort(403)
    if not content or len(content) > 500:
        abort(403)

    programs.update_program(program_id, title, content, level_id, type_id)

    return redirect("/program/" + str(program_id))

@app.route("/delete_program/<int:program_id>", methods=["GET", "POST"])
def delete_program(program_id):
    require_login()
    program = programs.get_program(program_id)

    if not program:
        abort(404)

    if program["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("delete_program.html", program=program)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            programs.delete_program(program_id)
            return redirect("/")

        return redirect("/program/" + str(program_id))

@app.route("/find_program")
@app.route("/find_program/<int:page>")
def find_program(page=1):
    query = request.args.get("query", "")
    page_size = 10

    if not query:
        return render_template("find_program.html", query="", results=[],
                               page=1, page_count=1)

    result_count = programs.count_search_results(query)
    page_count = math.ceil(result_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect(f"/find_program/1?query={query}")
    if page > page_count:
        return redirect(f"/find_program/{page_count}?query={query}")

    results = programs.search(query, page, page_size)
    return render_template("find_program.html", query=query, results=results,
                           page=page, page_count=page_count)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return render_template("register.html"), 400

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu")
        return render_template("register.html"), 409

    flash("Tunnus luotu onnistuneesti!")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    user = users.check_login(username, password)

    if not user:
        flash("VIRHE: väärä tunnus tai salasana")
        return render_template("login.html"), 401

    session["username"] = user["username"]
    session["user_id"] = user["id"]
    session["csrf_token"] = secrets.token_hex(16)

    return redirect("/")

@app.route("/logout")
def logout():
    require_login()
    session.clear()
    return redirect("/")