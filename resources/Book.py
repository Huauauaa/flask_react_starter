from flask_restful import Resource


class Book(Resource):
    def get(self):
        return {'data': {'name': 'python'}}
