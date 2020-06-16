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
    Os módulos realizam consultas por expressões,
    ou seja, por parte da string. Por exemplo, 
    pesquisa por "saude", qualquer parte do campo
    que houver a palavra pesquisa será retornado
    como resultado. 
'''


# Esta função entrgra uma descrição sobre a utilização do endpoint
def descricao():
    descricao = {
        'expressoes_palavrachave': {
            'modelo' : f'{baseUrl}/expressoes/palavraschave/<string:texto>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/expressoes/palavraschave/idoso/paginas/1'
        },
        'expressoes_titulo': {
            'modelo' : f'{baseUrl}/expressoes/titulos/<string:texto>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/expressoes/titulos/homem/paginas/1'
        },
        'expressoes_autores': {
            'modelo' : f'{baseUrl}/autores/<string:autores>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/expressoes/autores/Sandri/paginas/1'
        },
        'expressoes_resumo': {
            'modelo' : f'{baseUrl}/expressoes/resumos/<string:texto>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/expressoes/resumos/mulheres/paginas/1'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Consulta por expressões nos campo de resumo
def expressao_resumo(expressao, numero_pagina):
    if numero_pagina <= 0 or expressao == '':
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'resumo': {'$regex': expressao, '$options': 'i'}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por expressões nos campo de titulo
def expressao_titulo(expressao, numero_pagina):
    if numero_pagina <= 0 or expressao == '':
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'titulo': {'$regex': expressao, '$options': 'i'}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por expressões nos campo de palavras chave
def expressao_palavrachave(expressao, numero_pagina):
    if numero_pagina <= 0 or expressao == '':
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'palavrachave': {'$regex': expressao, '$options': 'i'}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)


# Consulta por expressão no campo de autores
def expressao_autores(autores, numero_pagina):
    if numero_pagina <= 0 or autores == '':
        abort(400)

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'autores': {'$regex': autores, '$options': 'i'}}).skip(indice).limit(10)
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)
