from sqlalchemy.orm import Session
from models.data import Book

def get_books(db: Session, limit: int = 10, offset: int = 0):
    return db.query(Book).offset(offset).limit(limit).all()

def create_book(db: Session, book_data):
    book = Book(**book_data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book