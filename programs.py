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