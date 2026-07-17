# 🚀 Todo API using FastAPI

A simple CRUD REST API built using **FastAPI**.

## Features

- ✅ Create Task
- ✅ Get All Tasks
- ✅ Get Task by ID
- ✅ Update Task
- ✅ Delete Task
- ✅ Interactive Swagger UI

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn myapi:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root |
| GET | `/health` | Health Check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get task by ID |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{task_id}` | Update task |
| DELETE | `/tasks/{task_id}` | Delete task |

## Author

**Smile Mangla**