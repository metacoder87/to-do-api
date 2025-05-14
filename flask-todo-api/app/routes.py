from flask import Blueprint, jsonify, request

todo_routes = Blueprint('todo', __name__)

todos = []

@todo_routes.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@todo_routes.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json
    todos.append(todo)
    return jsonify(todo), 201

@todo_routes.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id < len(todos):
        todos[todo_id] = request.json
        return jsonify(todos[todo_id])
    return jsonify({'error': 'Todo not found'}), 404

@todo_routes.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify({'result': True})
    return jsonify({'error': 'Todo not found'}), 404