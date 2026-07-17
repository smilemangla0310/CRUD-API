# 🚀 Todo API using FastAPI

A simple CRUD REST API built using **FastAPI** as part of the **FlyRank Backend AI Engineering Internship**.

---

## Features

- Create Tasks
- Read All Tasks
- Read Task by ID
- Update Tasks
- Delete Tasks
- Request Validation using Pydantic
- Interactive Swagger Documentation

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Installation

Clone the repository

```bash
git clone https://github.com/smilemangla0310/CRUD-API.git
```

Move inside the project

```bash
cd CRUD-API
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn myapi:app --reload
```

---

## Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Root |
| GET | `/health` | Health Check |
| GET | `/tasks` | Get All Tasks |
| GET | `/tasks/{task_id}` | Get Task by ID |
| POST | `/tasks` | Create Task |
| PUT | `/tasks/{task_id}` | Update Task |
| DELETE | `/tasks/{task_id}` | Delete Task |

---

## Example cURL

```bash
curl -i http://127.0.0.1:8000/tasks
```

Example Output

```http
HTTP/1.1 200 OK
content-type: application/json

[
  {
    "id":1,
    "title":"Watch Backend AI Session",
    "done":false
  }
]
```

---

## Swagger UI

![Swagger UI](images/swagger-ui.png)

---

## Project Author

Smile Mangla

Backend AI Engineering Intern

FlyRank AI