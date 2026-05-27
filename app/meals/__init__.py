from flask import Blueprint

bp = Blueprint('meals', __name__)

from app.meals import routes  # noqa: F401, E402
