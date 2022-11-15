from flask import Response, request
from models import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class MoviesApi(Resource):

    def get(self):
        movies = Move.object().to_json()
        return Response(movies, mimetype="appllication/json", status = 200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200

class MovieApi(Resource):
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return 'Movie was successfully update', 200

    @jwt_required()
    def delete(self, id):
        Movie.objects.get(id=id).delete()
        return 'Movie was successfully deleted'. 200