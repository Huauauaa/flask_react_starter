from flask_restful import reqparse

video_put_args = reqparse.RequestParser()

video_put_args.add_argument('name', type=str, help='name is required', required=True)
video_put_args.add_argument('likes', type=int, help='likes should be a number')
