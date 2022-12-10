from flask import Blueprint, jsonify

from logger import get_logger
from utils import load_post_by_pk, load_posts

api_bp = Blueprint('api', __name__)
logger = get_logger(__name__)


@api_bp.route("/api/posts/")
def view_main_api():
    posts = load_posts()
    logger.info('api_posts')
    return jsonify(posts)


@api_bp.route("/api/post/<int:pk>")
def view_post_api(pk):
    post = load_post_by_pk(pk)
    logger.info('api_post')
    return jsonify(post)
