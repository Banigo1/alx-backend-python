import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create the `users` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO users (id, name, email) VALUES (?, ?, ?)
''', [
    (1, 'John Doe', 'john.doe@example.com'),
    (2, 'Jane Smith', 'jane.smith@example.com'),
    (3, 'Alice Johnson', 'alice.johnson@example.com')
])

# Commit and close the connection
conn.commit()
conn.close()

print("Table `users` created and sample data inserted.")