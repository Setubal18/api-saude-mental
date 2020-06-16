import json
import math

from bson import json_util
from flask import jsonify, make_response

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
    Este módulo possui os métodos que buscam 
    por um conjunto de documentos , por exemplo,
    todos documentos, todos documentos de um 
    repositório ou documentos por tipo: "mestrado,
    doutorado" e etc.
'''


# Esta função entrgra uma descrição sobre a utilização do endpoint 
def descricao():
    descricao = {
        'dissertacoes': {
            'modelo' : f'{baseUrl}/dissertacoes/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/dissertacoes/paginas/1'
        },
        'repositorio': {
            'modelo' : f'{baseUrl}/repositorios/<string:sigla>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/repositorios/USP/paginas/1'
        },
        'tipo': {
            'modelo' : f'{baseUrl}/tipos/<string:tipo_doc>/paginas/<int:pagina>',
            'exemplo': f'{baseUrl}/tipos/Doutorado/paginas/1'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Função que busca por todos documentos no repositório
def conjunto_todos(numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find().skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Função que busca por todos documentos
# de uma universidade
def conjunto_repositorio(sigla, numero_pagina):
    if numero_pagina <= 0 or sigla == '':
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'repositorio': {'$regex': sigla, '$options': 'i'}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Função que busca por todos documentos
# de um tipo: "mestrado, doutorado" e
# etc.
def conjunto_tipo(tipo, numero_pagina):
    if numero_pagina <= 0:
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find(
        {
            '$or':[
                {'tipo': tipo},
                {'tipo': {'$regex': tipo, '$options': 'i'}},
            ]
        }
    ).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)
