from flask import Flask
from flask_restful import Api
from resources.Video import Video
from resources.Book import Book


app = Flask(__name__)
api = Api(app)


api.add_resource(Video, '/video/<int:id>')
api.add_resource(Book, '/book')


if __name__ == '__main__':
    app.run()
