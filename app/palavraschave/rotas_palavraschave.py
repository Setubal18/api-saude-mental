from flask import Blueprint

from .view import *

palavraschave_bp = Blueprint('palavraschave_bp', __name__)


@palavraschave_bp.route('/palavraschave/', methods=['GET'])
def get_descricao_contadores():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@palavraschave_bp.route('/palavraschave/<string:palavras>/paginas/<int:numero_pagina>', methods=['GET'])
@palavraschave_bp.route('/palavraschave/<string:palavras>/paginas', methods=['GET'])
@palavraschave_bp.route('/palavraschave/<string:palavras>', methods=['GET'])
def get_palavraschave(palavras='', numero_pagina=0):
    response = palavraschave_palavraschave(palavras, numero_pagina)
    return make_response(response.data, response.status, response.headers)
