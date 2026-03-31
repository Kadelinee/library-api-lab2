# Library API

REST API бібліотеки на FastAPI

## Ендпоінти:
- GET /books
- GET /books/{id}
- POST /books
- DELETE /books/{id}

## Функціонал:
- фільтрація (author, status)
- сортування (title, year)
- async/await
- Pydantic валідація

## Тести:
pytest

## Запуск:
uvicorn main:app --reload
