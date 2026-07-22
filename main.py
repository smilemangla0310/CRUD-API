from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import sqlite3

# ===========================
# Create FastAPI Application
# ===========================

app = FastAPI(
    title="Todo API",
    description="Backend API built using FastAPI by Smile Mangla",
    version="1.0.0"
)

# ===========================
# Pydantic Models
# ===========================

# Used when creating a new task
class TaskCreate(BaseModel):
    title: str


# Used when updating a task
class TaskUpdate(BaseModel):
    title: str
    done: bool


# ===========================
# Home Endpoint
# ===========================

@app.get("/")
def root():
    return {
        "app": "Todo API",
        "version": "1.0.0",
        "developer": "Smile Mangla",
        "status": "Running"
    }


# ===========================
# Health Check
# ===========================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "server": "running"
    }


# ===========================
# GET ALL TASKS
# ===========================

@app.get("/tasks", tags=["Tasks"])
def get_tasks():

    # Connect to database
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    # Read all tasks
    cursor.execute("SELECT * FROM tasks")

    # Returns a list of tuples
    rows = cursor.fetchall()

    # Close database connection
    conn.close()

    # Convert tuples into dictionaries
    tasks = []

    for row in rows:

        task = {
            "id": row[0],
            "title": row[1],

            # SQLite stores 0/1
            # bool() converts them into False/True
            "done": bool(row[2])
        }

        tasks.append(task)

    return tasks


# ===========================
# GET TASK BY ID
# ===========================

@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id: int):

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    # If task doesn't exist
    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # Convert tuple into dictionary
    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }


# ===========================
# CREATE TASK
# ===========================

@app.post(
    "/tasks",
    tags=["Tasks"],
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    # Only insert title
    # SQLite automatically inserts done = False
    cursor.execute(
        "INSERT INTO tasks(title) VALUES (?)",
        (task.title,)
    )

    # Get newly created task id
    task_id = cursor.lastrowid

    # Save changes
    conn.commit()

    conn.close()

    return {
        "id": task_id,
        "title": task.title,
        "done": False
    }


# ===========================
# UPDATE TASK
# ===========================

@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: TaskUpdate):

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title=?, done=?
        WHERE id=?
        """,
        (task.title, task.done, task_id)
    )

    # If nothing was updated
    if cursor.rowcount == 0:
        conn.close()

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    conn.commit()

    conn.close()

    return {
        "id": task_id,
        "title": task.title,
        "done": task.done
    }


# ===========================
# DELETE TASK
# ===========================

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    # No task found
    if cursor.rowcount == 0:

        conn.close()

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    conn.commit()

    conn.close()

    return {
        "message": "Task deleted successfully",
        "deleted_task_id": task_id
    }