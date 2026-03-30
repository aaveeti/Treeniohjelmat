import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM reviews")
db.execute("DELETE FROM programs")
db.execute("DELETE FROM users")

level_ids = [row[0] for row in db.execute("SELECT id FROM levels").fetchall()]
type_ids = [row[0] for row in db.execute("SELECT id FROM workout_types").fetchall()]

user_count = 1000
program_count = 10**5
review_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
               ["user" + str(i), "dummyhash"])

for i in range(1, program_count + 1):
    user_id = random.randint(1, user_count)
    level_id = random.choice(level_ids)
    type_id = random.choice(type_ids)
    db.execute("""INSERT INTO programs (title, content, user_id, level_id, type_id)
                  VALUES (?, ?, ?, ?, ?)""",
               ["program" + str(i), "description" + str(i), user_id, level_id, type_id])

for i in range(1, review_count + 1):
    user_id = random.randint(1, user_count)
    program_id = random.randint(1, program_count)
    rating = random.randint(1, 5)
    db.execute("""INSERT INTO reviews (user_id, program_id, rating, comment, created_at)
                  VALUES (?, ?, ?, ?, datetime('now'))""",
               [user_id, program_id, rating, "comment" + str(i)])

db.commit()
db.close()