from flask import Blueprint

from .view import *

expressoes_bp = Blueprint('expressoes_bp', __name__)


@expressoes_bp.route('/expressoes/', methods=['GET'])
@expressoes_bp.route('/expressoes/resumos/', methods=['GET'])
@expressoes_bp.route('/expressoes/titulos/', methods=['GET'])
@expressoes_bp.route('/expressoes/palavraschave/', methods=['GET'])
@expressoes_bp.route('/expressoes/autores/', methods=['GET'])
def get_descricao():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@expressoes_bp.route('/expressoes/resumos/<string:texto>/paginas/<int:numero_pagina>', methods=['GET'])
@expressoes_bp.route('/expressoes/resumos/<string:texto>/paginas', methods=['GET'])
@expressoes_bp.route('/expressoes/resumos/<string:texto>', methods=['GET'])
def get_resumo(texto='', numero_pagina=0):
    response = expressao_resumo(texto, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@expressoes_bp.route('/expressoes/titulos/<string:texto>/paginas/<int:numero_pagina>')
@expressoes_bp.route('/expressoes/titulos/<string:texto>/paginas')
@expressoes_bp.route('/expressoes/titulos/<string:texto>')
def get_titulo(texto='', numero_pagina=0):
    response = expressao_titulo(texto, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@expressoes_bp.route('/expressoes/palavraschave/<string:texto>/paginas/<int:numero_pagina>')
@expressoes_bp.route('/expressoes/palavraschave/<string:texto>/paginas')
@expressoes_bp.route('/expressoes/palavraschave/<string:texto>')
def get_pchave(texto='', numero_pagina=0):
    response = expressao_palavrachave(texto, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@expressoes_bp.route('/expressoes/autores/<string:autores>/paginas/<int:numero_pagina>')
@expressoes_bp.route('/expressoes/autores/<string:autores>/paginas')
@expressoes_bp.route('/expressoes/autores/<string:autores>')
def get_autores(autores='', numero_pagina=0):
    response = expressao_autores(autores, numero_pagina)
    return make_response(response.data, response.status, response.headers)
