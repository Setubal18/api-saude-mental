from flask import jsonify, make_response
from bson import json_util
import json

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
    Este módulo retorna algumas informações 
    númericas sobre a base de dados. Não
    realiza nenhum tipo de consulta.
'''

# Esta função entrgra uma descrição sobre a utilização do endpoint 
def descricao():
    descricao = {
        'contadores': {
            'repositorios': f'{baseUrl}/contadores/repositorios',
            'anos'        : f'{baseUrl}/contadores/anos',
            'tipos'       : f'{baseUrl}/contadores/tipos'
        }
    }
    return make_response(jsonify(descricao), 200, headers)


# Função que retorna o número de trabalhos por repositório
def contadores_repositorios():
    repositorios = __colecoes.aggregate([{"$group": {'_id': "$repositorio", 'count': {'$sum': 1}}}])
    resposta = json.loads(json_util.dumps(repositorios))
    return make_response(jsonify(resposta), 200, headers)


# Função que retorna o número de trabalhos por ano de publicação
def contadores_anos():
    anos = __colecoes.aggregate(
        [{'$group': {'_id': {'$dateToString': {'format': '%Y', 'date': '$data'}}, 'count': {'$sum': 1}}}])
    resposta = json.loads(json_util.dumps(anos))
    return make_response(jsonify(resposta), 200, headers)


# Função que retorna o número de trabalhos por tipo de trabalho
def contadores_tipos():
    tipos = __colecoes.aggregate([{"$group": {'_id': "$tipo", 'count': {'$sum': 1}}}])
    resposta = json.loads(json_util.dumps(tipos))
    return make_response(jsonify(resposta), 200, headers)
