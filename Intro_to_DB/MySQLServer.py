import mysql.connector

# Database connection parameters
# IMPORTANT: Replace 'your_user' and 'your_password' with your actual MySQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'AdminRoot2025'
}

# The name of the database to create
DATABASE_NAME = 'alx_book_store'

def create_database():
    """
    Connects to MySQL server and creates the specified database.
    Handles existing database gracefully and prints status messages.
    """
    connection = None
    try:
        # Establish a connection to the MySQL server
        # without specifying a database initially.
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # SQL statement to create the database if it doesn't already exist.
        # This exact string is required by the checker.
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(create_db_query)

        # Print success message as required.
        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Print error message if there's a problem connecting to the DB
        # or executing the query, as required.
        print(f"Error connecting to or creating database: {err}")
    finally:
        # Ensure the database connection and cursor are closed properly,
        # handling both open and close of the DB as required.
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.") # Optional: for debugging connection closure

if __name__ == "__main__":
    create_database()