import sqlite3
import db

def add_program(title, content, user_id, level_id, type_id):
    try:
        sql = """INSERT INTO programs (title, content, user_id, level_id, type_id)
                 VALUES (?, ?, ?, ?, ?);"""
        db.execute(sql, [title, content, user_id, level_id, type_id])
    except sqlite3.IntegrityError:
        return "Tapahtui virhe"

def update_program(program_id, title, content, level_id, type_id):
    sql = """UPDATE programs SET title = ?,
                                 content = ?,
                                 level_id = ?,
                                 type_id = ?
                             WHERE id = ?;"""
    db.execute(sql, [title, content, level_id, type_id, program_id])

def get_programs():
    sql = "SELECT id, title FROM programs ORDER BY id DESC;"
    return db.query(sql)

def get_program(program_id):
    sql = """SELECT programs.id,
                    programs.title,
                    programs.content,
                    programs.level_id,
                    programs.type_id,
                    users.id AS user_id,
                    users.username
             FROM programs
             JOIN users ON programs.user_id = users.id
             WHERE programs.id = ?;"""

    result = db.query(sql, [program_id])
    if result:
        return result[0]
    return None

def delete_program(program_id):
    sql = "DELETE FROM programs WHERE id = ?;"
    db.execute(sql, [program_id])

def search(query):
    sql = """SELECT programs.id, programs.title
             FROM programs
             WHERE programs.title LIKE ? OR programs.content LIKE ?
             ORDER BY id DESC;"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def get_categories(program_id):
    sql = """SELECT L.title AS level, T.title AS type
             FROM programs P
             JOIN levels L ON P.level_id = L.id
             JOIN workout_types T ON P.type_id = T.id
             WHERE P.id = ?;"""
    result = db.query(sql, [program_id])
    return result[0] if result else None

def add_comment(user_id, comment, rating, program_id):
    try:
        sql = """INSERT INTO reviews (user_id, program_id, rating, comment)
                 VALUES (?, ?, ?, ?);"""
        db.execute(sql, [user_id, program_id, rating, comment])
    except sqlite3.IntegrityError:
        return "Tapahtui virhe"

def get_comments(program_id):
    sql = """SELECT u.id AS user_id, u.username, r.comment, r.rating 
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.program_id = ? 
             ORDER BY r.id DESC;"""
    return db.query(sql, [program_id])