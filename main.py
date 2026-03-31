from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import Base, engine, SessionLocal
from services.book_service import create_book, list_books, get_book, update_book, delete_book
from schemas.book import BookCreate, BookRead
from uuid import UUID

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=BookRead)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/", response_model=list[BookRead])
def read_books(db: Session = Depends(get_db)):
    return list_books(db)

@app.get("/books/{book_id}", response_model=BookRead)
def read_book(book_id: UUID, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=BookRead)
def edit_book(book_id: UUID, book: BookCreate, db: Session = Depends(get_db)):
    updated = update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}", response_model=BookRead)
def remove_book(book_id: UUID, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted