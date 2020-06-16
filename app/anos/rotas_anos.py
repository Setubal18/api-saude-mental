from flask import Blueprint

from .view import *

datas_bp = Blueprint('datas_bp', __name__)


@datas_bp.route('/anos/', methods=['GET'])
@datas_bp.route('/anos_anteriores/', methods=['GET'])
@datas_bp.route('/anos_posteriores/', methods=['GET'])
@datas_bp.route('/periodos/', methods=['GET'])
def get_descricao_ano():
    response = descricao()
    return make_response(response.data, response.status, response.headers)


@datas_bp.route('/anos/<int:ano>/paginas/<int:numero_pagina>', methods=['GET'])
@datas_bp.route('/anos/<int:ano>/paginas', methods=['GET'])
@datas_bp.route('/anos/<int:ano>', methods=['GET'])
def get_ano_dissetacoes(ano=0, numero_pagina=0):
    response = data_ano(ano, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@datas_bp.route('/anos_anteriores/<int:ano>/paginas/<int:numero_pagina>', methods=['GET'])
@datas_bp.route('/anos_anteriores/<int:ano>/paginas', methods=['GET'])
@datas_bp.route('/anos_anteriores/<int:ano>', methods=['GET'])
def get_anos_anteriores(ano=0, numero_pagina=0):
    response = data_anos_anteriores(ano, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@datas_bp.route('/anos_posteriores/<int:ano>/paginas/<int:numero_pagina>', methods=['GET'])
@datas_bp.route('/anos_posteriores/<int:ano>/paginas', methods=['GET'])
@datas_bp.route('/anos_posteriores/<int:ano>', methods=['GET'])
def get_anos_posteriores(ano=0, numero_pagina=0):
    response = data_anos_posteriores(ano, numero_pagina)
    return make_response(response.data, response.status, response.headers)


@datas_bp.route('/periodos/inicio/<int:ano_inicio>/fim/<int:ano_fim>/paginas/<int:numero_pagina>', methods=['GET'])
@datas_bp.route('/periodos/inicio/<int:ano_inicio>/fim/<int:ano_fim>/paginas', methods=['GET'])
@datas_bp.route('/periodos/inicio/<int:ano_inicio>/fim/<int:ano_fim>', methods=['GET'])
@datas_bp.route('/periodos/inicio/<int:ano_inicio>/fim', methods=['GET'])
@datas_bp.route('/periodos/inicio/<int:ano_inicio>', methods=['GET'])
@datas_bp.route('/periodos/inicio/', methods=['GET'])
def get_anos_periodo(ano_inicio=0, ano_fim=0, numero_pagina=0):
    response = data_anos_periodo(ano_inicio, ano_fim, numero_pagina)
    return make_response(response.data, response.status, response.headers)


