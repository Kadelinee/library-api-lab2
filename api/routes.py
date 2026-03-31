from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import SessionLocal
from services.book_service import list_books, add_book
from schemas.book import BookCreate, Book

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books", response_model=list[Book])
def get_all_books(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return list_books(db, limit, offset)

@router.post("/books", response_model=Book)
def create(book: BookCreate, db: Session = Depends(get_db)):
    return add_book(db, book)