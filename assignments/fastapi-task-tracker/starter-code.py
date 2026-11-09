from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API")

# Example in-memory data
TASKS = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a task API", "done": True},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Tracker API"}


# TODO: Add GET /tasks
# TODO: Add POST /tasks
# TODO: Add GET /tasks/{task_id}
# TODO: Add PUT or DELETE routes for extra practice
