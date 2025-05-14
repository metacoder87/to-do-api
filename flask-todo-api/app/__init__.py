from flask import Flask
from .routes import todo_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_routes)
    return app