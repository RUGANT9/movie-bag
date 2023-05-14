from flask_restful import Resource
from flask import render_template, make_response
from flask_login import current_user

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("home.html", current_user=current_user), 200, headers)

