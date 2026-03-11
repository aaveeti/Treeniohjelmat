import sqlite3
import db

def add_program(title, content, user_id, level_id, type_id):
    try:
        sql = """INSERT INTO programs (title, content, user_id, level_id, type_id)
                 VALUES (?, ?, ?, ?, ?)"""
        db.execute(sql, [title, content, user_id, level_id, type_id])
    except sqlite3.IntegrityError:
        return "Tapahtui virhe"