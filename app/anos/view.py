import json
import math
from datetime import datetime

from bson import json_util
from flask import jsonify, make_response

from app.base_dados.conexao import *

# Acesso a colecao da base de dados
__colecoes = colecoes()

'''
    Este módulo possui métodos de pesquisa
    por ano de publicação de trabalho, anterior,
    posterior e dentro de um período de ano. 
'''

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


# Esta função verifica se o ano passado no
# parâmetro é um ano válido. O tipo de dado
# 'datetime' do python não reconhece mais de 
# 5 dígitos para verificação de anos
# O anos definidos manualmente abragem todos
# os trabalhos da base de dados, visto que não
# há anos anteriores a 1900 e superiores a 2100,
# informações validadas pelo recurso '/lista_anos'
def validacao_ano(ano):
    year = int(ano)
    if 1900 <= year <= 2100:
        return True
    return False


# Esta função entrgra uma descrição sobre a utilização do endpoint
def descricao():
    descricao = {
        'ano': {
            'modelo' : f'{baseUrl}/anos/<int:ano>/paginas/<int:pagina>',
            'exemplo': f'{baseUrl}/anos/2020/paginas/1'
        },
        'anos_anteriores': {
            'modelo' : f'{baseUrl}/anos_anteriores/<int:ano>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/anos_anteriores/2005/paginas/1'
        },
        'anos_posteriores': {
            'modelo' : f'{baseUrl}/anos_posteriores/<int:ano>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/anos_posteriores/2000/paginas/1'
        },
        'periodo': {
            'modelo' : f'{baseUrl}/periodos/inicio/<int:ano_inicio>/fim/<int:ano_fim>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/periodos/inicio/2000/fim/2005/paginas/1'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Consulta de documentos por ano de publicação
def data_ano(ano, numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    if validacao_ano(ano) is False:
        return make_response(jsonify(''), 204, headers)

    indice = (numero_pagina - 1) * 10
    ano_inicio = datetime(ano, 1, 1)
    ano_fim = datetime(ano, 12, 31)

    documentos = __colecoes.find({'data': {'$gte': ano_inicio, '$lte': ano_fim}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por período anterior
def data_anos_anteriores(ano_ant, numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    if validacao_ano(ano_ant) is False:
        abort(400)

    indice = (numero_pagina - 1) * 10
    data = datetime(ano_ant, 1, 1)

    documentos = __colecoes.find({'data': {'$lt': data}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por um período posterior
def data_anos_posteriores(ano_pos, numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    if validacao_ano(ano_pos) is False:
        return make_response(jsonify(''), 204, headers)

    indice = (numero_pagina - 1) * 10
    data = datetime(ano_pos, 12, 31)

    documentos = __colecoes.find({'data': {'$gt': data}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por um período de tempo
def data_anos_periodo(ano_inicio, ano_fim, numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    if validacao_ano(ano_inicio) is False or validacao_ano(ano_fim) is False:
        return make_response(jsonify(''), 204, headers)

    index = (numero_pagina - 1) * 10
    inicio_ano = datetime(ano_inicio, 1, 1)
    fim_ano = datetime(ano_fim, 12, 31)

    documentos = __colecoes.find({'data': {'$gte': inicio_ano, '$lte': fim_ano}}).sort('id').skip(index).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)
