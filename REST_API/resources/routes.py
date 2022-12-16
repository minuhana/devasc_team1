from resources.movie import MoviesApi, MovieApi
from resources.auth import LoginApi, SignupApi

def initialize_routes(api):
    api.add_resources(MoviesApi, '/api/movies')
    api.add_resources(MovieApi, '/api/movies/<id>')
    api.add_resources(SignupApi, '/api/auth/signup')
    api.add_resources(LoginApi, '/api/auth/login')