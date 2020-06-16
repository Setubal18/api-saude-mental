from flask import abort

from app.base_dados import dao

base_dados = dao.Dao()
documentos = base_dados.colecoes_documentos()


def colecoes():
    if documentos:
        return documentos
    else:
        abort(500)
