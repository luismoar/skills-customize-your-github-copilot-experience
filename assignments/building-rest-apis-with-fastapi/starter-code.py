from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

# Sample in-memory data
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Tasks API"}


# TODO: Add GET /tasks
# TODO: Add POST /tasks
# TODO: Add GET /tasks/{task_id}
# TODO: Add validation and error handling
