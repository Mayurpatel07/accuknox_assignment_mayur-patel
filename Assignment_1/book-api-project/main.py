
from api import fetch_books
from database import create_database, insert_books, get_books


create_database()

books = fetch_books()

if books:
    insert_books(books)

    books = get_books()

    print("\nBooks:")
    for book in books:
        print(f"{book[1]} - {book[2]} - {book[3]}")
else:
    print("No books found.")
