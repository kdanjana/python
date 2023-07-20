from utils_pkg import db

choice = """
Choose an option
-'a' to add new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit
Enter ur choice: """


def prompt_add_book():
    book_name = input("Please enter book name: ")
    auth_name = input("Please enter author name: ")
    db.add_book(book_name.title(), auth_name.title())
    print(f"{book_name.title()} written by {auth_name.title()} is added to database.")


def list_books():
    books = db.get_all_books()
    for book in books:
        if book['read'] == 0:
            read = "NO"
        else:
            read = 'YES'
        print(f"{book['name']} is written by {book['author']}, read: {read}.")


def mark_book():
    name = input("Enter book name u just finished reading: ")
    marked_books = db.mark_book_asread(name)
    if len(marked_books) == 0:
        print(f"{name.title()} is not in list of books.")
    else:
        for book in marked_books:
            print(f"{book['name']} written by {book['author']} is marked read.")


def del_book():
    name = input("Enter book name u want to delete: ")
    del_books = db.deleting_book(name)
    if len(del_books) == 0:
        print(f"{name.title()} is not in the list of books.")
    else:
        for book in del_books:
            print(f"{book['name']} written by {book['author']} is deleted.")
    

def main():
    # creating books file/ tabel  if doesnt exist
    db.create_booktable()
    user_choice = input(choice).lower()
    while user_choice != 'q':        
        if user_choice == 'a':
            prompt_add_book()
        elif user_choice == "l":
            list_books()
        elif user_choice == "r":
            mark_book()
        elif user_choice == "d":
            del_book()
        else:
            print("Unknown command.Please enter correct choice.")
        user_choice = input(choice).lower()
        

if __name__ == "__main__":
    main()
