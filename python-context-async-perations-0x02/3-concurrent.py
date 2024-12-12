import sqlite3
import asyncio
import aiosqlite

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Establishes the database connection and returns the connection object."""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """Closes the database connection and handles exceptions."""
        if self.connection:
            self.connection.close()
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate exceptions if any

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else []
        self.results = None

    def __enter__(self):
        """Executes the query and returns the results."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        """Closes the database connection and cursor, handling exceptions."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Propagate exceptions if any

async def async_fetch_users(db_name):
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users(db_name):
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    """Run multiple database queries concurrently."""
    db_name = "example.db"
    results = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    )
    print("All Users:", results[0])
    print("Users Older Than 40:", results[1])

if __name__ == "__main__":
    # Create a sample database and table for demonstration purposes
    db_name = "example.db"
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 45), ('Diana', 50)")
        conn.commit()

    # Run the concurrent fetch
    asyncio.run(fetch_concurrently())
