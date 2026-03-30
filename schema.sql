CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE levels (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE workout_types (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE programs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    level_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (level_id) REFERENCES levels(id),
    FOREIGN KEY (type_id) REFERENCES workout_types(id)
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE
);

CREATE INDEX idx_programs_user_id ON programs(user_id);
CREATE INDEX idx_programs_level_id ON programs(level_id);
CREATE INDEX idx_programs_type_id ON programs(type_id);
CREATE INDEX idx_reviews_program_id ON reviews(program_id);
CREATE INDEX idx_reviews_user_id ON reviews(user_id);