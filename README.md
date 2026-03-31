Library API

REST API бібліотеки на FastAPI

Ендпоінти
GET /books – отримати список всіх книг
GET /books/{id} – отримати деталі книги по ID
POST /books – додати нову книгу
DELETE /books/{id} – видалити книгу по ID

Функціонал
Фільтрація: author, status
Сортування: title, year
Використання async/await
Валідація через Pydantic

Тести
Використовується pytest для перевірки CRUD операцій

Запуск
Через uvicorn (для локальної розробки):
uvicorn main:app --reload
Через Docker Compose:
docker-compose up --build
Контейнери:
postgres_db – PostgreSQL
fastapi_app – FastAPI

Swagger UI доступний за адресою:

http://localhost:8000/docs
