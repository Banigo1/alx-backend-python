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

# Example usage
if __name__ == "__main__":
    # Create a sample database and table for demonstration purposes
    db_name = "example.db"
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25)")
        conn.commit()

    # Using the custom context manager to query the database
    with DatabaseConnection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)
