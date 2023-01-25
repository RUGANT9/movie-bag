from flask_restful import Resource
from flask import render_template, make_response

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("home.html"), 200, headers)
        

