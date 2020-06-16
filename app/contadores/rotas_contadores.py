from flask import Blueprint, make_response, request
from .view import *

contadores_bp = Blueprint('contadores_bp', __name__)


@contadores_bp.route('/contadores/', methods=['GET'])
def get_descricao_contadores():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@contadores_bp.route('/contadores/repositorios', methods=['GET'])
def get_repositorios():
    response = contadores_repositorios()
    return make_response(response.data, response.status, response.headers)


@contadores_bp.route('/contadores/anos', methods=['GET'])
def get_datas():
    response = contadores_anos()
    return make_response(response.data, response.status, response.headers)


@contadores_bp.route('/contadores/tipos', methods=['GET'])
def get_tipos():
    response = contadores_tipos()
    return make_response(response.data, response.status, response.headers)