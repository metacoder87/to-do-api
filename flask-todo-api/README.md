# Flask Todo API

## Overview
This project is a simple Flask API for managing a todo list. It allows users to create, read, update, and delete todo items. The API is designed to be lightweight and easy to use, making it a great starting point for learning Flask and building RESTful APIs.

## Project Structure
```
flask-todo-api
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd flask-todo-api
   ```

2. **Install Dependencies**
   Make sure you have Python and pip installed. Then, install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**
   You can run the application locally using:
   ```
   export FLASK_APP=app
   export FLASK_ENV=development
   flask run
   ```
   The API will be available at `http://127.0.0.1:5000`.

## Docker Instructions

1. **Build the Docker Image**
   ```
   docker build -t flask-todo-api .
   ```

2. **Run the Docker Container**
   ```
   docker run -p 5000:5000 flask-todo-api
   ```

## API Endpoints

- **GET /todos**
  - Retrieves the list of todos.
  
- **POST /todos**
  - Adds a new todo. The request body should be a JSON object representing the todo item.

- **PUT /todos/<id>**
  - Updates an existing todo by ID. The request body should be a JSON object with the updated todo item.

- **DELETE /todos/<id>**
  - Deletes a todo by ID.

## Example Usage

### Get Todos
```
curl -X GET http://127.0.0.1:5000/todos
```

### Add Todo
```
curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d '{"task": "Learn Flask", "done": false}'
```

### Update Todo
```
curl -X PUT http://127.0.0.1:5000/todos/0 -H "Content-Type: application/json" -d '{"task": "Learn Flask", "done": true}'
```

### Delete Todo
```
curl -X DELETE http://127.0.0.1:5000/todos/0
```

## License
This project is licensed under the MIT License.