import mysql.connector
from mysql.connector import Error

# Data to be inserted
authors = [
    ("Author One", "Biography of Author One"),
    ("Author Two", "Biography of Author Two"),
    ("Author Three", "Biography of Author Three")
]

books = [
    ("Book One", 1, "1234567890", "2023-01-01"),
    ("Book Two", 2, "0987654321", "2023-02-01"),
    ("Book Three", 3, "1122334455", "2023-03-01")
]

users = [
    ("User One", "LIB001"),
    ("User Two", "LIB002"),
    ("User Three", "LIB003")
]

try:
    # Establishing the connection
    connection = mysql.connector.connect(
        host='localhost',
        database='library_db',
        user='root',
        password='568312'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Inserting data into authors table
        cursor.executemany("INSERT INTO authors (name, biography) VALUES (%s, %s)", authors)

        # Inserting data into books table
        cursor.executemany("INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)", books)

        # Inserting data into users table
        cursor.executemany("INSERT INTO users (name, library_id) VALUES (%s, %s)", users)

        # Committing the transaction
        connection.commit()
        print("Initial data inserted successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")