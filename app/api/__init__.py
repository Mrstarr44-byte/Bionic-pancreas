from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api/v1')

from app.api import routes  # noqa: F401, E402
