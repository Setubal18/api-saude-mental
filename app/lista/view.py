from flask import jsonify, abort, make_response
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


# Esta função entrgra uma descrição sobre a utilização do endpoint 
def descricao():
    descricao = {
        'listas': {
            'repositorios': f'{baseUrl}/listas/repositorios',
            'anos': f'{baseUrl}/listas/anos',
            'tipos': f'{baseUrl}/listas/tipos'
        }
    }
    return make_response(jsonify(descricao), 200, headers)

# Função que retorna a sigla de todos os repositórios
# (universidades) exsistentes na base de dados
def lista_repositorios():
    documentos = __colecoes.aggregate([{"$group": {"_id": '$repositorio'}}])
    resposta = json.loads(json_util.dumps(documentos))
    return make_response(jsonify(resposta), 200, headers)


# Função que retorna uma lista com os anos de publicação
# do trabalhos. Não há repetição de anos. Se no ano
# de 2000 foram realizados 100 trabalhos, o ano 2000 será
# apresentado apenas um vez
def lista_anos():
    lista_ano=[]
    documentos= __colecoes.distinct('data')

    for doc in documentos:
        if doc.year not in lista_ano:
            lista_ano.append(doc.year)

    return make_response(jsonify(lista_ano), 200, headers)


# Função que retorna uma lista com os tipos de trabalhos
# existentes na base dados, mestrado, artigo, etc.
def lista_tipos():
    documentos = __colecoes.aggregate([{"$group": {"_id": '$tipo'}}])
    resposta = json.loads(json_util.dumps(documentos))
    return make_response(jsonify(resposta), 200, headers)