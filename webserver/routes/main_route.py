from flask import Blueprint


bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return "Flask in a Docker!!! Hello World!"
