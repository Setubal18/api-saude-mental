import json
import math

from bson import json_util
from flask import jsonify, make_response
from pymongo import TEXT

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

# Função que cria um 'lista' de palavras chaves para consulta
# Uma vez criado, fica disponpivel para todo código,
# o serviço Atlas armazena (em nuvem) o índice (lista de palavras) para
# consultas de palavras chave, diferente da pesquisa por expressões. 
__colecoes.create_index([('palavrachave', TEXT)],name='palavra_autor_index')


# Esta função entrgra uma descrição sobre a utilização do endpoint 
def descricao():
    descricao = {
        'palavras_chave': {
            'modelo' : f'{baseUrl}/palavraschave/<string:palavras>/paginas/<int:numero_pagina>',
            'exemplo': f'{baseUrl}/palavraschave/idoso;acolhimento/paginas/1'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Função retorna documento que contenham pelo menos 
# uma das palavras chaves passadas no parâmetro
def palavraschave_palavraschave(palavras, numero_pagina):
    
    if numero_pagina <= 0 or palavras=='':
        abort(400)

    aux = f'{palavras}'.replace(' ', '')
    lista_palavras = aux.split(';')

    print(f'Type: {type(lista_palavras)} - Lista de Palavras: {lista_palavras}')

    indice = (numero_pagina - 1) * 10
    documentos = __colecoes.find({'$text': {'$search': f'{lista_palavras}'}}).skip(indice).limit(10).sort('_id')
    resposta = json.loads(json_util.dumps(documentos))

    if len(resposta) == 0:
        return make_response(jsonify(''), 204, headers)

    headers['X-Total-Count'] = math.ceil((documentos.count()) / 10)

    return make_response(jsonify(resposta), 200, headers)
