from flask import Blueprint, jsonify
from .models import Post

routes = Blueprint('routes', __name__)

@routes.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

