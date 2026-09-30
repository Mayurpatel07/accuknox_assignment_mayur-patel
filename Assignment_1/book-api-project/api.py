
import requests

API_URL = "https://openlibrary.org/search.json?q=python"


def fetch_books():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()

        books = []

        for book in data["docs"][:10]:
            authors = book.get("author_name", [])

            books.append({
                "title": book.get("title"),
                "author": authors[0] if authors else "Unknown",
                "publication_year": book.get("first_publish_year")
            })

        return books

    except requests.exceptions.RequestException as e:
        print("Error fetching books:", e)
        return []
