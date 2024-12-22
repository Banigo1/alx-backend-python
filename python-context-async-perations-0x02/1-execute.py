import sqlite3

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

# Example usage
if __name__ == "__main__":
    # Create a sample database and table for demonstration purposes
    db_name = "example.db"
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)")
        conn.commit()

    # Using the ExecuteQuery context manager
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with ExecuteQuery(db_name, query, params) as results:
        for row in results:
            print(row)
