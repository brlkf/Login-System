import sqlite3

def insert_dummy_data():
    dummy_data = [
        ("John", "password123"),
        ("Alex", "123456"),
        ("Peter", "qwertyu"),
    ]

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        for username, password in dummy_data:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

# Create the "users" table if it doesn't exist
with sqlite3.connect("users.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

# Insert dummy data into the "users" table
insert_dummy_data()
