from flask import Blueprint, make_response, request,jsonify
from .view import *


conjunto_bp = Blueprint('conjunto_bp', __name__)


@conjunto_bp.route('/dissertacoes/', methods=['GET'])
@conjunto_bp.route('/repositorios/', methods=['GET'])
@conjunto_bp.route('/tipos/', methods=['GET'])
def get_descricao():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@conjunto_bp.route('/dissertacoes/paginas/<int:numero_pagina>', methods=['GET'])
@conjunto_bp.route('/dissertacoes/paginas', methods=['GET'])
def get_todos(numero_pagina):
    response = conjunto_todos(numero_pagina)
    return make_response(response.data, response.status, response.headers)


@conjunto_bp.route('/repositorios/<string:sigla>/paginas/<int:numero_pagina>', methods=['GET'])
@conjunto_bp.route('/repositorios/<string:sigla>/paginas', methods=['GET'])
@conjunto_bp.route('/repositorios/<string:sigla>', methods=['GET'])
def get_repositorio(sigla='', numero_pagina=0):
    print(request.url)
    response = conjunto_repositorio(sigla, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@conjunto_bp.route('/tipos/<string:tipo_doc>/paginas/<int:numero_pagina>', methods=['GET'])
@conjunto_bp.route('/tipos/<string:tipo_doc>/paginas', methods=['GET'])
@conjunto_bp.route('/tipos/<string:tipo_doc>', methods=['GET'])
def get_tipo(tipo_doc='', numero_pagina=0):
    response = conjunto_tipo(tipo_doc, numero_pagina)
    return make_response(response.data, response.status, response.headers)
