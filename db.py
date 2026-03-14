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
    levels = con.execute("SELECT id, title FROM levels").fetchall()
    con.close()
    return levels

def get_workout_type():
    con = get_connection()
    types = con.execute("SELECT id, title FROM workout_types").fetchall()
    con.close()
    return types