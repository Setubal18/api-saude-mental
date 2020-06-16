from flask import json

'''
    Arquivo que contém uma função
    para tratamento simples de erros
'''


# Esta função recebe qualquer status de erro
# e retorna uma mensagem personalizada

def identificador_erro(e):
    response = e.get_response()

    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })

    response.content_type = "application/json"

    return response
