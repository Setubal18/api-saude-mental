from flask import jsonify, make_response
from bson import json_util
from datetime import datetime
import json, math

from app.base_dados.conexao import *

# Acesso a colecao da base de dados
__colecoes = colecoes()

# Variáveis Globais
baseUrl = 'https://api-saude-mental.herokuapp.com'

# headers utilizados nas respostas da requisições
headers = {
    'Access-Control-Expose-Headers': '*',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0',
    'X-Total-Count': '0'
}

'''
    Este módulo possui uma função de pesquisa
    encadeada, que envolve diversos parâmetros.
    O resultado retornará documentos que atendam 
    a pelo menos um dos parâmetros
'''


# Esta função entrgra uma descrição sobre a utilização do endpoint
def descricao():
    descricao = {
        'avancado': {
            'modelo': f'{baseUrl}/consultas/<string:repositorio>/<string:tipo>/<string:palavrachave>/<int:anoInicio>/<int:anoFim>/<string:resumo>/<string:titulo>/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/consultas/USP/mestrado/crianca/2005/2010/crianca/crianca/1'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Esta funçõa verifica se algum parâmetro da URL está vazio ou invállido
def verifica_status(repositorio, tipo, palavrachave, anoInicio, anoFim, resumo, titulo, numero_pagina):
    status = True
    if repositorio == '' or tipo == '' or palavrachave == '' or resumo == '' or titulo == '':
        status = False
    if anoInicio < 1900 or anoInicio > 2100 or anoFim < 1900 or anoFim > 2100:
        status = False
    if anoInicio > anoFim:
        status = False
    if numero_pagina <= 0:
        status = False

    return status


def avancado_consulta(repositorio, tipo, palavrachave, anoInicio, anoFim, resumo, titulo, numero_pagina):
    if not verifica_status(repositorio, tipo, palavrachave, anoInicio, anoFim, resumo, titulo, numero_pagina):
        abort(400)

    indice = (numero_pagina - 1) * 10
    ano_inicio = datetime(anoInicio, 1, 1)
    ano_fim = datetime(anoFim, 12, 31)

    documentos = __colecoes.find({
        '$and':
            [
                {'repositorio': {'$regex': repositorio, '$options': 'i'}},
                {'$or': [
                    {'tipo': {'$regex': tipo, '$options': 'i'}},
                    {'palavrachave': {'$regex': palavrachave, '$options': 'i'}},
                    {'ano': {'gte': ano_inicio, '$lte': ano_fim}},
                    {'resumo': {'$regex': resumo, '$options': 'i'}},
                    {'titulo': {'$regex': titulo, '$options': 'i'}}
                ]}
            ]
    }).skip(indice).limit(10)

    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)
