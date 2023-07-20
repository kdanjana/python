# this db.py is an interface between our application code or business logic and database or storage
"""
this is concerned with storing and retrieving books form a json file, format of json file is list of dicts
[
    {
    "name": "potter",
    "author": "rowling",
    "read" : True
    },
    {
    "name": "venom",
    "author": "stephen",
    "read" : True
    },
]
"""

import json 

books_file = "books.json"


# to create a table , in this case we are creating a books.json file
def create_booktable():
    with open(books_file, "w") as file:
        json.dump([], file)


# to write books to json file
def _save_all_books(books):
    with open(books_file, "w") as file:
        json.dump(books, file)


# to read books from json file
def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


# to add book to the json file
def add_book(name: str, author: str):
    books = get_all_books()
    books.append({"name": name, "author": author, "read": "False"})
    _save_all_books(books)


# to mark book as read in the json file
def mark_book_asread(name: str):
    books = get_all_books()
    marked_books = []
    for book in books:
        if book['name'].lower() == name.lower():
            book['read'] = "True"
            marked_books.append(book)
    _save_all_books(books)
    return marked_books         


# to delete a book from the json file
def deleting_book(name: str):
    books = get_all_books()
    new_books = []
    del_books = []
    for book in books:
        if book['name'].lower() != name.lower():
            new_books.append(book)
        else:
            del_books.append(book)
    _save_all_books(new_books)
    return del_books
    