import sqlite3
import db

def program_count():
    sql = "SELECT COUNT(id) FROM programs;"
    return db.query(sql)[0][0]

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

def get_programs(page, page_size):
    sql = """SELECT p.id,
                    p.title,
                    p.created_at,
                    l.title AS level,
                    w.title AS type,
                    u.username
             FROM programs p
             JOIN users u ON p.user_id = u.id
             JOIN levels l ON p.level_id = l.id
             JOIN workout_types w ON p.type_id = w.id
             ORDER BY p.id DESC
             LIMIT ? OFFSET ?;"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

def get_program(program_id):
    sql = """SELECT programs.id,
                    programs.title,
                    programs.content,
                    programs.level_id,
                    programs.type_id,
                    programs.created_at,
                    users.id AS user_id,
                    users.username
             FROM programs
             JOIN users ON programs.user_id = users.id
             WHERE programs.id = ?;"""

    result = db.query(sql, [program_id])
    if result:
        return result[0]
    return None

def user_program_count(user_id):
    sql = "SELECT COUNT(id) FROM programs WHERE user_id = ?;"
    result = db.query(sql, [user_id])
    return result[0][0] if result else 0

def get_user_programs(user_id, page, page_size):
    sql = """SELECT p.id,
                    p.title,
                    p.created_at,
                    l.title AS level,
                    w.title AS type
             FROM programs p
             JOIN levels l ON p.level_id = l.id
             JOIN workout_types w ON p.type_id = w.id
             WHERE p.user_id = ?
             ORDER BY p.id DESC
             LIMIT ? OFFSET ?;"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [user_id, limit, offset])

def delete_program(program_id):
    sql = "DELETE FROM programs WHERE id = ?;"
    db.execute(sql, [program_id])

def count_search_results(query):
    sql = "SELECT COUNT(id) FROM programs WHERE title LIKE ? OR content LIKE ?"
    like = "%" + query + "%"
    result = db.query(sql, [like, like])
    return result[0][0] if result else 0

def search(query, page, page_size):
    sql = """SELECT p.id,
                    p.title, 
                    p.created_at, 
                    u.username,
                    l.title AS level,
                    w.title AS type
             FROM programs p
             JOIN users u ON p.user_id = u.id
             JOIN levels l ON p.level_id = l.id
             JOIN workout_types w ON p.type_id = w.id
             WHERE p.title LIKE ? OR p.content LIKE ?
             ORDER BY p.id DESC
             LIMIT ? OFFSET ?;"""
    like = "%" + query + "%"
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [like, like, limit, offset])

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
    sql = """SELECT r.id, u.id AS user_id, u.username, r.comment, r.rating
             FROM reviews r 
             JOIN users u ON r.user_id = u.id 
             WHERE r.program_id = ? 
             ORDER BY r.id DESC;"""
    return db.query(sql, [program_id])

def get_comment(comment_id):
    sql = """SELECT r.id,
                    r.user_id,
                    r.program_id,
                    r.rating,
                    r.comment,
                    p.id,
                    u.id
             FROM reviews r
             JOIN programs p ON r.program_id = p.id
             JOIN users u ON r.user_id = u.id 
             WHERE r.id = ?;"""
    result = db.query(sql, [comment_id])
    return result[0] if result else None

def delete_comment(comment_id, user_id):
    try:
        sql = "DELETE FROM reviews WHERE id = ? AND user_id = ?"
        db.execute(sql, [comment_id, user_id])
    except sqlite3.IntegrityError:
        return "Tapahtui virhe"