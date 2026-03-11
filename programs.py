import sqlite3
import db

def add_program(title, content, user_id, level_id, type_id):
    try:
        sql = """INSERT INTO programs (title, content, user_id, level_id, type_id)
                 VALUES (?, ?, ?, ?, ?)"""
        db.execute(sql, [title, content, user_id, level_id, type_id])
    except sqlite3.IntegrityError:
        return "Tapahtui virhe"

def get_programs():
    sql = "SELECT id, title FROM programs ORDER BY id DESC;"
    return db.query(sql)

def get_program(program_id):
    sql = """SELECT programs.title,
                    programs.content,
                    users.username
             FROM programs, users
             WHERE programs.user_id = users.id AND
                   programs.id = ?;"""
    
    return db.query(sql, [program_id])[0]