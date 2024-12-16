from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.database.db import db

from app.models.user import User
from app.schemas.user import UserSchema



user_bp = Blueprint('user', __name__, description='User related operations')


@user_bp.route('/')
class UserHandler(MethodView):

    ''' Create new user'''
    @user_bp.response(201, UserSchema)
    @user_bp.arguments(UserSchema)
    def post(self, body):

        user = User(**body)

        db.session.add(user)
        db.session.commit()
        
        return user

@user_bp.route('/<int:user_id>')
class UserByIdHandler(MethodView):

    ''' Get single user'''
    @user_bp.response(200, UserSchema)
    def get(self, user_id):
        user = db.session.execute(
            db.select(User).where(User.id == user_id)
        ).scalar()

        if not user:
            abort(404, message='User not found')

            
        return user
