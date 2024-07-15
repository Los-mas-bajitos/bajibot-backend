from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from config.db import db
from user.user_model import User

users = Blueprint('user', __name__)


@users.route('/user/insert', methods=['POST'])
def create_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify(
            {
                'message': 'User already exists',
                'status': 400
            }
        )
    user = User(data['username'], data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(
        {
            'message': 'User created',
            'user': user.to_dict(),
            'status': 200
        }
    )


@users.route('/user/get', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify(
        {
            'users': [user.to_dict() for user in users],
            'status': 200
        }
    )


@users.route('/user/get/<int:id>', methods=['GET'])
def get_user_by(id):
    user = User.query.get(id)
    if user:
        return jsonify(
            {
                'user': user.to_dict(),
                'status': 200
            }
        )
    return jsonify(
        {
            'message': 'User not found',
            'status': 404
        }
    )


@users.route('/user/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        return jsonify(
            {
                'message': 'User logged in',
                'jwt': create_access_token(identity=user.id),
                'status': 200
            }
        )
    return jsonify(
        {
            'message': 'Invalid credentials',
            'status': 401
        }
    )
