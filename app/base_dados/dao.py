import pymongo
from flask import abort


class Dao:
    def __init__(self):
        self.__url = 'mongodb+srv://pablo:ulbra2020@academicoencena-mykuh.azure.mongodb.net/test?retryWrites=true&w=majority'
        self.__conexao = pymongo.MongoClient(self.__url)
        self.__basedados = self.__conexao.get_database('db-trabalhosAcademicos')
        self.__colecoes = self.__basedados.get_collection('trabalhosSaudeMental')

    def verificação(self):
        if self.__conexao:
            return True
        abort(500)

    def colecoes_documentos(self):
        if self.verificação():
            return self.__colecoes
        abort(500)

