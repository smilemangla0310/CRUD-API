import sqlite3

# ===========================
# Connect to SQLite Database
# ===========================
# If tasks.db doesn't exist, SQLite creates it automatically.

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# ===========================
# Create Tasks Table
# ===========================
# IF NOT EXISTS ensures the table isn't recreated
# every time this file is run.

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0
)
""")

# ===========================
# Insert Sample Data (Only Once)
# ===========================
# Check if the table is empty.

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

# Add sample tasks only if there are no records.
if count == 0:
    cursor.executemany("""
    INSERT INTO tasks (title, done)
    VALUES (?, ?)
    """, [
        ("Watch the YouTube Session of Backend AI by FlyRank", 1),
        ("Practice and understand the FastAPI Framework", 0),
        ("Complete the Todo List API Assignment", 0)
    ])

# Save changes permanently.
conn.commit()

# Close the database connection.
conn.close()

print("Database initialized successfully!")
