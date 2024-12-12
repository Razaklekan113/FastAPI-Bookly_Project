from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

books_data = [
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
        "language": "English"
    }
]


@app.get("/books")
async def get_all_books() -> dict:
    pass

@app.post("/books")
async def create_a_book() -> dict:
    pass

@app.post("/books/{book_id}")
async def get_a_book(book_id:int) -> dict:
    pass

# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/greet")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}", "age": age}

# class BookCreateModel(BaseModel):
#     title: str
#     author: str


# @app.post("/create_book")
# async def create_book(book_data:BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }

# @app.get("/get_headers", status_code=200)
# async def get_headers(
#     accept: str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_headers = {}

#     request_headers["Accept"] = accept
#     request_headers["CONTENT-TYPE"] = content_type
#     request_headers["User-Agent"] = user_agent
#     request_headers["Host"] = host

#     return request_headers