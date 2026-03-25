import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, username, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    
    if not result:
        return None
    
    user = result[0]

    if check_password_hash(user["password_hash"], password):
        return user
    
    return None

def get_user(user_id):
    sql = """SELECT id, username
             FROM users
             WHERE id = ?;"""
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_programs(user_id):
    sql = """SELECT p.id, 
                    p.title, 
                    p.created_at,
                    l.title AS level,
                    w.title AS type
             FROM programs p
             JOIN levels l ON p.level_id = l.id
             JOIN workout_types w ON p.type_id = w.id
             WHERE p.user_id = ?
             ORDER BY p.id DESC;"""
    return db.query(sql, [user_id])