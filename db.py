import sqlite3
from flask import g

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def get_levels():
    con = get_connection()
    result = "SELECT title FROM levels;"
    levels = con.execute(result).fetchall()
    con.close()
    return [level[0] for level in levels]

def get_workout_type():
    con = get_connection()
    result = "SELECT title FROM workout_types;"
    types = con.execute(result).fetchall()
    con.close()
    return [type[0] for type in types]