from sqlalchemy.orm import Session
from models.data import Book
from schemas.book import BookCreate
from uuid import UUID

def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def list_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: UUID):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: UUID, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: UUID):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book