from flask import Response, request, render_template, make_response
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime
from flask_login import current_user
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError

class SignupApi(Resource):
    def post(self):
        try:
            body = {'email': request.form['email'], 'password': request.form['password']}
            user =  User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return make_response(render_template('login.html'), 200)
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            user = User.objects.get(email=request.form['email'])
            authorized = user.check_password(request.form['password'])
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return make_response(render_template('success_landing.html'), 200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

class LoginPageApi(Resource):
    def get(self):
        return make_response(render_template('login.html'), 200)

class SignupPageApi(Resource):
    def get(self):
        return make_response(render_template('signup.html'), 200)