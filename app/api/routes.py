from flask_restful import Resource

class TodoItem(Resource):
    def get(self, id):
        if id == 25:
            return {'task': 'Magic task #25!'}
        return {'task': 'Say "Hello, World!"'}
