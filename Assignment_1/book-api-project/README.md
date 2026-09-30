# Book API Project

This project fetches book details from the Open Library API and stores them in a SQLite database.

The program gets the data from the API, extracts the book details, saves them in the database and displays the books in the terminal.

## Technologies Used

Python  
Requests  
SQLite

## Files

```text
main.py         - runs the project
api.py          - gets book data from API
database.py     - handles SQLite database
requirements.txt
README.md
books.db        - created when the program runs
```

## How to Run

Create virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install requests:

```powershell
pip install -r requirements.txt
```

Run the project:

```powershell
python main.py
```

## Working

The program first sends a request to the API and gets the book data in JSON format.

It then takes the title, author and publication year from the response and stores them in SQLite.

After inserting the data, a SELECT query is used to get the books from the database and display them in the terminal.

The program also handles API errors and avoids inserting the same book again.

## Database

The database file is `books.db`.

The table used is `books`.

It contains `id`, `title`, `author` and `publication_year`.