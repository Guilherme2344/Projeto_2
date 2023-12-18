import json
from models.modelo import Modelo

class Curso:
    def __init__(self, id, nome, descricao,iddiretoria):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__iddiretoria = iddiretoria

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_iddiretoria(self, iddiretoria):
        self.__iddiretoria = iddiretoria

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_iddiretoria(self):
        return self.__iddiretoria
    def __str__(self):
        return f'{self.__id}, {self.__nome},{self.__descricao}, {self.__iddiretoria}'

class NCurso(Modelo):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            with open('cursos.json', 'r') as arquivo:
                a = json.load(arquivo)
                for curso in a:
                    d = Curso(curso['_Curso__id'], curso['_Curso__nome'], curso['_Curso__descricao'], curso["_Curso__iddiretoria"])
                    cls.objetos.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('cursos.json', 'w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)