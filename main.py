from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": "1925-04-10",
        "page_count": 180,
        "language": "English"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "publisher": "Harper & Brothers",
        "published_date": "1851-11-14",
        "page_count": 635,
        "language": "English"
    },
    {
        "id": 4,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 214,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton, Whitehall",
        "published_date": "1813-01-28",
        "page_count": 432,
        "language": "English",
    }

]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher:str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher:str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)

    return new_book

@app.get("/books/{book_id}")
async def get_a_book(book_id:int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/books/{book_id}")
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books :
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.post("/books/{book_id}")
async def delete_book(book_id:int) -> dict:
    pass
