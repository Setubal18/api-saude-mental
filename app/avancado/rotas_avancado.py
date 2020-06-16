from flask import Blueprint, request
from .view import *

avancado_bp = Blueprint('avancado_bp', __name__)

@avancado_bp.route('/consultas/', methods=['GET'])
def get_descricao():
    response = descricao()
    return make_response(response.data, response.status, response.headers)

@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>/<int:anoFim>/<string:resumo>/<string:titulo>/<int:numero_pagina>', methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>/<int:anoFim>/<string:resumo>/<string:titulo>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>/<int:anoFim>/<string:resumo>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>/<int:anoFim>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>/<string:tipo>',  methods=['GET'])
@avancado_bp.route('/consultas/<string:repositorio>',  methods=['GET'])
def get_avancado(
    repositorio='',
    tipo='',
    palavrachave='',
    anoInicio=0,
    anoFim=0,
    resumo='',
    titulo='',
    numero_pagina=0
):
    response = avancado_consulta(repositorio, tipo, palavrachave, anoInicio, anoFim, resumo, titulo, numero_pagina)
    return make_response(response.data, response.status, response.headers) 
