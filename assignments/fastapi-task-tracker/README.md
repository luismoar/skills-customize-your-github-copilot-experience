# 📘 Assignment: FastAPI Task Tracker

## 🎯 Objective

Build a small task-tracking API using FastAPI and practice working with routes, request data, and JSON responses. This assignment helps students understand how web APIs connect client requests to server-side logic.

## 📝 Tasks

### 🛠️ Create the API

#### Description
Set up a FastAPI application and create a simple endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a root route that responds with a JSON message.
- Start the app locally with `uvicorn`.
- Confirm the endpoint works in a browser or API client.

### 🛠️ Manage Tasks

#### Description
Create endpoints for reading and adding tasks to an in-memory list.

#### Requirements
Completed program should:

- Create a list of sample tasks stored in memory.
- Add a `GET /tasks` endpoint that returns all tasks.
- Add a `POST /tasks` endpoint that accepts a new task.
- Return the created task as JSON.
- Make sure each task includes an `id`, `title`, and completion status.

### 🛠️ Validate Input and Handle Errors

#### Description
Improve the API by validating incoming data and returning helpful errors when a task is missing.

#### Requirements
Completed program should:

- Use a Pydantic model for task creation.
- Validate that the task title is not empty.
- Add a `GET /tasks/{task_id}` endpoint.
- Return a `404` error if the task does not exist.
- Use clear and readable JSON responses.

### 🛠️ Optional Extension

#### Description
Extend the project with an update or delete operation to complete the CRUD flow.

#### Requirements
Completed program should:

- Add an endpoint to update a task.
- Add an endpoint to delete a task.
- Keep the API logic organized and easy to follow.
- Test the full workflow using a browser or API testing tool.
