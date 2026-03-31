from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models.database import SessionLocal
from services.book_service import list_books_cursor, create_book
from schemas.book import Book, BookCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books", response_model=list[Book])
def get_all_books(
    cursor: int = Query(
        default=None, 
        description="ID останньої книги з попередньої сторінки (залишити порожнім для першої сторінки)", 
        example=0
    ),
    limit: int = Query(
        default=10, 
        description="Кількість книг на сторінку", 
        example=5
    ),
    db: Session = Depends(get_db)
):
    print("cursor:", cursor, "limit:", limit)
    return list_books_cursor(db, cursor=cursor, limit=limit)

@router.post("/books", response_model=Book)
def create(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)