CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE Levels (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE WorkoutTypes (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE Programs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    level_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (level_id) REFERENCES Levels(id),
    FOREIGN KEY (type_id) REFERENCES WorkoutTypes(id)
);

CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);