import logging
from flask import Blueprint, jsonify
from models.user import User

logger = logging.getLogger('flaskapp') 

user_bp = Blueprint('user', __name__)

@user_bp.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

