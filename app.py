from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from resources.Video import Video, VideoId
from resources.Book import Book
import config
from extensions import db


app = Flask(__name__)
api = Api(app)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)

api.add_resource(Video, '/video', endpoint='video')
api.add_resource(VideoId, '/video/<int:id>', endpoint='video_id')
api.add_resource(Book, '/book', endpoint='book')


if __name__ == '__main__':
    app.run(debug=True)
