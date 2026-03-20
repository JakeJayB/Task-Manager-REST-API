# Task Manager REST API

A FastAPI project with two versions of the same task-management API:

- `List-Version/`: in-memory storage using a Python list
- `MongoDB-Version/`: persistent storage using MongoDB

Both versions expose the same core task endpoints for creating, reading, updating, filtering, and deleting tasks.

## Features

- Build a REST API with FastAPI
- Create, read, update, patch, and delete tasks
- Filter tasks by `completed` status and `priority`
- Use either:
  - an in-memory list for simple local testing
  - MongoDB for persistent storage

## Tech Stack

- Python
- FastAPI
- Uvicorn
- MongoDB / PyMongo Async client
- Pydantic

## Project Structure

```text
Task-Manager-REST-API/
├── List-Version/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── repositories/
│   ├── services/
│   └── routers/
├── MongoDB-Version/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models.py
│   ├── repositories/
│   ├── services/
│   ├── routers/
│   └── .env
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running The API

Each version is started from its own folder.

### List Version

This version stores tasks in memory. Data resets every time the server restarts.

```bash
cd List-Version
uvicorn main:app --reload
```

Open:

- `http://127.0.0.1:8000/docs`

### MongoDB Version

This version stores tasks in MongoDB.

1. Make sure MongoDB is running locally.
2. Configure environment variables in `MongoDB-Version/.env`.

Example:

```env
MONGODB_URI=mongodb://127.0.0.1:27017
DB_NAME=TaskManager
COLLECTION_NAME=Tasks
```

Run:

```bash
cd MongoDB-Version
uvicorn main:app --reload
```

Open:

- `http://127.0.0.1:8000/docs`

## Task Model

### Fields

- `title`: string
- `description`: string
- `completed`: boolean
- `priority`: `low`, `medium`, or `high`

## API Endpoints

Base route: `/tasks`

### Get all tasks

```http
GET /tasks
```

Optional query parameters:

- `completed=true|false`
- `priority=low|medium|high`

Example:

```http
GET /tasks?completed=false&priority=high
```

### Get task by ID

List version:

```http
GET /tasks/{id}
```

- `id` is an integer

MongoDB version:

```http
GET /tasks/{id}
```

- `id` is a MongoDB ObjectId string

### Create a task

```http
POST /tasks
```

Request body:

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "priority": "low"
}
```

### Replace a task

```http
PUT /tasks/{id}
```

This replaces the full task body.

### Partially update a task

```http
PATCH /tasks/{id}
```

Example:

```json
{
  "completed": true
}
```

### Delete a task

```http
DELETE /tasks/{id}
```

## Responses

- `201 Created` when a task is created
- `204 No Content` when a task is deleted
- `404 Not Found` when a task does not exist
- MongoDB version also returns `400 Bad Request` for an invalid ObjectId

## Notes

- The list-based API is useful for learning the repository/service/router structure without needing a database.
- The MongoDB version adds persistence and validates MongoDB ObjectIds before querying.
- The home route `/` returns a small HTML message that points to `/docs`.
