from flask_restful import Resource, abort, fields, marshal_with, request
from parses.video_args import video_put_args, video_patch_args

from models.VideoModel import VideoModel
from extensions import db


resource_fields = {'id': fields.Integer, 'name': fields.String, 'likes': fields.Integer}


class Video(Resource):
    def __init__(self):
        print('init')

    @marshal_with(resource_fields)
    def get(self):
        q = request.args.get('q') or ''
        videos = VideoModel.query.filter(VideoModel.name.contains(q)).order_by(-VideoModel.id).all()
        return videos, 200

    @marshal_with(resource_fields)
    def post(self):
        args = video_put_args.parse_args()
        video = VideoModel(name=args['name'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


class VideoId(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        video = VideoModel.query.get(id)
        if video:
            return video, 200
        else:
            abort(404, message='not found')

    def delete(self, id):
        video = VideoModel.query.get(id)
        if video:
            db.session.delete(video)
            db.session.commit()
            return '', 204
        else:
            abort(404, message='not found')

    @marshal_with(resource_fields)
    def patch(self, id):
        args = video_patch_args.parse_args()
        result = VideoModel.query.get(id)
        if not result:
            abort(404, message='not found')

        if args['name']:
            result.name = args['name']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result
