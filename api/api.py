from flask import Blueprint, jsonify

import logger
import utils

api_bp = Blueprint('api', __name__, url_prefix='/api', template_folder="")
log = logger.get_logger('api')


@api_bp.route("/post/")
def api_posts():
    posts = utils.load_posts()
    log.info(f"api_posts - > {len(posts)}")
    return jsonify(posts)


@api_bp.route("/post/<int:pk>")
def api_post(pk):
    post = utils.load_post(pk)
    log.info(f"api_post - > {pk}")
    return jsonify(post)