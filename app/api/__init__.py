from flask import Blueprint
from flask_restful import Api

from .routes import TodoItem

api_bp = Blueprint('api_bp', __name__)
api = Api(api_bp)

api.add_resource(TodoItem, '/todos/<int:id>')