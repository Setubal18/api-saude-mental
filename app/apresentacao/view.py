from flask import make_response, jsonify

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
    Este módulo serve como um index que
    apresenta as funções de pesquisas
    disponíveis.
'''


dados = {

    'consulta_conjunto': {
        'dissertacoes': f'{baseUrl}/dissertacoes',
        'repositorio' : f'{baseUrl}/repositorios',
        'tipo'        : f'{baseUrl}/tipos'
    },

    'consulta_avancada': {
        'avancado': f'{baseUrl}/consultas'
    },
    'consulta_anos': {
        'ano'             : f'{baseUrl}/anos',
        'anos_anteriores' : f'{baseUrl}/anos_anteriores',
        'anos_posteriores': f'{baseUrl}/anos_posteriores',
        'periodo'         : f'{baseUrl}/periodos',
    },

    'consulta_expressoes': {
        'palavrachave'      : f'{baseUrl}/expressoes/palavraschave',
        'expressoes_titulo' : f'{baseUrl}/expressoes/titulos',
        'expressoes_autores': f'{baseUrl}/expressoes/autores',
        'expressoes_resumo' : f'{baseUrl}/expressoes/resumos'
    },

    'consultas_palavras_chave': {
        'palavras_chave': f'{baseUrl}/palavraschave'
    },

    'listas': {
        'anos'        : f'{baseUrl}/listas/anos',
        'repositorios': f'{baseUrl}/listas/repositorios',
        'tipos'       : f'{baseUrl}/listas/tipos',
    },

    'contadores': {
        'trabalhos_anos'       : f'{baseUrl}/contadores/anos',
        'trabalhos_repositorio': f'{baseUrl}/contadores/repositorios',
        'trabalhos_tipos'      : f'{baseUrl}/contadores/tipos'
    }
}


def apresentacao():
    return make_response(jsonify(dados), 200, headers)
