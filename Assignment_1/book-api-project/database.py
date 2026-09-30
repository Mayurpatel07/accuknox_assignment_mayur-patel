
import sqlite3


def create_database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER,
            UNIQUE(title, author)
        )
    """)

    conn.commit()
    conn.close()


def insert_books(books):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    for book in books:
        cursor.execute("""
            INSERT OR IGNORE INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (
            book["title"],
            book["author"],
            book["publication_year"]
        ))

    conn.commit()
    conn.close()


def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    conn.close()

    return books
