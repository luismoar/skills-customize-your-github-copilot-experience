# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage a collection of items while practicing routes, request validation, and JSON responses. This assignment introduces students to the fundamentals of API design and server-side web development.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a FastAPI application and add a basic endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install and import the `fastapi` package.
- Create an app instance using `FastAPI()`.
- Add a root endpoint using the `@app.get("/")` decorator.
- Return a JSON response such as `{"message": "Welcome to the Tasks API"}`.
- Run the app locally with `uvicorn` and confirm the endpoint works.

### 🛠️ Create CRUD Endpoints

#### Description
Build routes to list and create tasks using in-memory storage.

#### Requirements
Completed program should:

- Define a list of sample tasks stored in memory.
- Add an endpoint to return all tasks with `GET /tasks`.
- Add an endpoint to create a new task with `POST /tasks`.
- Accept task data through a request body and return the created item.
- Use JSON responses so the client can consume the data easily.

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by validating input and handling missing resources cleanly.

#### Requirements
Completed program should:

- Define a Pydantic model for task data with required fields.
- Validate that each task has a valid title and boolean status.
- Add a `GET /tasks/{task_id}` endpoint that returns a single task.
- Return a `404` response when the requested task does not exist.
- Use clear error messages and keep the API easy to test with a browser or API client.

### 🛠️ Optional Challenge

#### Description
Extend the project with one additional feature to make the API more realistic.

#### Requirements
Completed program should:

- Add a feature such as updating a task, deleting a task, or filtering by completion status.
- Keep the code organized and readable.
- Test the new route with sample requests and confirm the behavior in JSON.
- Example update endpoint:
  ```python
  @app.put("/tasks/{task_id}")
  def update_task(task_id: int, task: TaskCreate):
      return {"task_id": task_id, "updated": task}
  ```
