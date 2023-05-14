from .movie import MoviesApi, MovieApi, MovieApibyname
from .auth import SignupApi, LoginApi, LoginPageApi, SignupPageApi
from .home import Home

def initialize_routes(api):
    api.add_resource(Home, '/api/home')
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(MovieApibyname, '/api/moviesbyname/name')
    api.add_resource(LoginPageApi, '/api/login_page')
    api.add_resource(SignupPageApi, '/api/signup_page')