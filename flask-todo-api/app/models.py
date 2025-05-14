from flask import jsonify

todos = []

def get_todos():
    return jsonify(todos)

def add_todo(todo):
    todos.append(todo)
    return jsonify(todo), 201

def update_todo(todo_id, todo):
    if todo_id < len(todos):
        todos[todo_id] = todo
        return jsonify(todos[todo_id])
    return jsonify({'error': 'Todo not found'}), 404

def delete_todo(todo_id):
    if todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify({'result': True})
    return jsonify({'error': 'Todo not found'}), 404