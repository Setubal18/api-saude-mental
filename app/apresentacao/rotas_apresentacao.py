from flask import Blueprint
from .view import *

apresentacao_bp = Blueprint('apresentacao_bp', __name__)


@apresentacao_bp.route('/')
def index():
    response = apresentacao()
    return make_response(response.data, response.status, response.headers)
