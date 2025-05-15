# Docker Dev Env for Python Flask

This repository provides a simple Flask API for managing a todo list, with a focus on Docker-based development and testing.

---

## Running Tests

This command builds a Docker image with the code from this repository and runs the repository's tests.

```sh
docker build -t flask-todo-api .
docker run -it flask-todo-api ./run_tests.sh
```

**Example output:**
```
[+] Building 0.1s (10/10) FINISHED
...
----------------------------------------------------------------------
Ran 4 tests in 0.069s

OK
```

---

## Running a Specific Test

You can run a single test by passing its name to the test runner:

```sh
docker build -t flask-todo-api .
docker run -it flask-todo-api ./run_tests.sh TodoTestCase.test_home
```

---

## Running a Flask Dev Server

To enable hot reloading and develop with Flask inside Docker, use the following commands:

```sh
docker build -t flask-todo-api .
docker run --network=host -v ${PWD}:/app -it flask-todo-api flask run --host=0.0.0.0
```

- `--network=host` allows the container to use the host network (on Windows, you may need to use `-p 5000:5000` instead).
- `-v ${PWD}:/app` mounts your current directory into the container for live code changes.

---

## API Endpoints

- **GET `/todos`**  
  Retrieves the list of todos.

- **POST `/todos`**  
  Adds a new todo. The request body should be a JSON object.

- **PUT `/todos/<id>`**  
  Updates an existing todo by ID.

- **DELETE `/todos/<id>`**  
  Deletes a todo by ID.

---

## Example Usage

**Get Todos**
```sh
curl -X GET http://127.0.0.1:5000/todos
```

**Add Todo**
```sh
curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d '{"task": "Learn Flask", "done": false}'
```

**Update Todo**
```sh
curl -X PUT http://127.0.0.1:5000/todos/0 -H "Content-Type: application/json" -d '{"task": "Learn Flask", "done": true}'
```

**Delete Todo**
```sh
curl -X DELETE http://127.0.0.1:5000/todos/0
```

---

## License

This project is licensed under the MIT License.