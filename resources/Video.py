from flask_restful import Resource, abort, fields, marshal_with
from parses.video_put_args import video_put_args


videos = [{'id': 0, 'title': 'learn python', 'likes': 234}, {'id': 1, 'title': 'learn js'}]


resource_fields = {'title': fields.String, 'likes': fields.Integer}


class Video(Resource):
    def get(self, id):
        try:
            return videos[id]
        except:
            abort(404, message=f'video {id} is not found')

    @marshal_with(resource_fields)
    def post(self, id):
        return videos

    def put(self, id):
        args = video_put_args.parse_args()
        return args
