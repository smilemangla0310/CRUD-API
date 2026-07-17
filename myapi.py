from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import status

app = FastAPI(
    title="Todo API",
    description="Backend API built using FastAPI By Smile Mangla",
    version="1.0.0"
)

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

tasks=[
    {"id":1,
     "title":"Watch the Youtube Session of Backend AI by Flyrank",
     "done":True
    },
    {"id":2,
     "title":"Practice and understand The FastAPI Framework",
     "done":False
    },
    {"id":3,
     "title":"Complete the Todo List API Assignment",
     "done":False
    }
]

@app.post(
    "/tasks",
    tags=["Tasks"],
    status_code=status.HTTP_201_CREATED
)

@app.get("/")
def root():
    return {
    "app": "Todo API",
    "version": "1.0.0",
    "developer": "Smile Mangla",
    "status": "Running"
}

@app.get("/health")
def health_check():
    return {
    "status":"healthy",
    "server":"running"
}


@app.get("/tasks", tags=["Tasks"])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    return {"message": "Task not found"}


@app.post("/tasks", tags=["Tasks"])
def create_task(task: TaskCreate):
    new_task={
        "id": len(tasks)+1,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: TaskUpdate):
    for existing_task in tasks:
        if existing_task["id"]==task_id:
            existing_task["title"]=task.title
            existing_task["done"]=task.done
            return existing_task
    
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            return {
            "message":"Task deleted successfully.",
            "deleted_task_id": task_id
        }
    raise HTTPException(status_code=404, detail="Task not found")