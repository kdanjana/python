from typing import List, Dict
from .database_connection import DatabaseConnection


def create_booktable() -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books (name text PRIMARY KEY, author text, read int)")
    

def add_book(name: str, author: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?, 0)', (name, author))
        

def get_all_books():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        # fetch all rows from the books table as list of tuples(list of each row as tuple)
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    return books
    

def deleting_book(name: str) -> List[Dict]:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE name=?", (name,))
        del_books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
        cursor.execute("DELETE FROM books WHERE name=?", (name,))
    return del_books


def mark_book_asread(name) -> List[Dict]:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE name=?", (name,))
        marked_books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))
    return marked_books
