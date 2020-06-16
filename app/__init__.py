from flask import Flask
from flask_cors import CORS

from werkzeug.exceptions import HTTPException


def create_app():
    app = Flask(__name__)
    CORS(app)

    with app.app_context():
        # incluindo rotas
        from .apresentacao import rotas_apresentacao
        from .conjunto import rotas_conjunto
        from .anos import rotas_anos
        from .expressoes import rotas_expressoes
        from .palavraschave import rotas_palavraschave
        from .lista import rotas_lista
        from .contadores import rotas_contadores
        from .avancado import rotas_avancado

        # tratamento de erros
        from .erros import manipulacao_erros

        # registrando Blueprints
        app.register_blueprint(rotas_apresentacao.apresentacao_bp)
        app.register_blueprint(rotas_conjunto.conjunto_bp)
        app.register_blueprint(rotas_anos.datas_bp)
        app.register_blueprint(rotas_expressoes.expressoes_bp)
        app.register_blueprint(rotas_palavraschave.palavraschave_bp)
        app.register_blueprint(rotas_lista.lista_bp)
        app.register_blueprint(rotas_contadores.contadores_bp)
        app.register_blueprint(rotas_avancado.avancado_bp)

        # resgistrado rota de erros
        app.register_error_handler(HTTPException, manipulacao_erros.identificador_erro)

    return app
