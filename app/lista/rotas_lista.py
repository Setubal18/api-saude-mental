from flask import Blueprint, make_response, request
from .view import *

lista_bp = Blueprint('lista_bp', __name__)


@lista_bp.route('/listas/', methods=['GET'])
def get_descricao_contadores():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@lista_bp.route('/listas/repositorios', methods=['GET'])
def get_repositorios():
    response = lista_repositorios()
    return make_response(response.data, response.status, response.headers)


@lista_bp.route('/listas/anos', methods=['GET'])
def get_ano():
    response = lista_anos()
    return make_response(response.data, response.status, response.headers)


@lista_bp.route('/listas/tipos', methods=['GET'])
def get_tipo():
    response = lista_tipos()
    return make_response(response.data, response.status, response.headers)
