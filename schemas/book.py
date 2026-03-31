from pydantic import BaseModel
from uuid import UUID

class BookCreate(BaseModel):
    title: str
    author: str
    description: str | None = None
    year: int
    status: str

class BookRead(BookCreate):
    id: UUID