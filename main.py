import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="568312",
            database="library_db"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def add_author(connection):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    query = f"INSERT INTO authors (name, biography) VALUES ('{name}', '{biography}')"
    execute_query(connection, query)

def add_book(connection):
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    query = f"INSERT INTO books (title, author_id, isbn, publication_date) VALUES ('{title}', {author_id}, '{isbn}', '{publication_date}')"
    execute_query(connection, query)

def add_user(connection):
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    query = f"INSERT INTO users (name, library_id) VALUES ('{name}', '{library_id}')"
    execute_query(connection, query)

def display_authors(connection):
    query = "SELECT * FROM authors"
    authors = fetch_query(connection, query)
    for author in authors:
        print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")

def display_books(connection):
    query = "SELECT * FROM books"
    books = fetch_query(connection, query)
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, ISBN: {book[3]}, Publication Date: {book[4]}, Availability: {book[5]}")

def display_users(connection):
    query = "SELECT * FROM users"
    users = fetch_query(connection, query)
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")

def main_menu():
    connection = create_connection()
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations(connection)
        elif choice == '2':
            user_operations(connection)
        elif choice == '3':
            author_operations(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations(connection):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(connection)
        elif choice == '2':
            # Implement borrow book functionality
            pass
        elif choice == '3':
            # Implement return book functionality
            pass
        elif choice == '4':
            # Implement search book functionality
            pass
        elif choice == '5':
            display_books(connection)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations(connection):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user(connection)
        elif choice == '2':
            # Implement view user details functionality
            pass
        elif choice == '3':
            display_users(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations(connection):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_author(connection)
        elif choice == '2':
            # Implement view author details functionality
            pass
        elif choice == '3':
            display_authors(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()