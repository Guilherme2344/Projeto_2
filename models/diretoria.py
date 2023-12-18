import json
from models.modelo import Modelo

class Diretoria:
    def __init__(self, id, nome, fone):
        self.__id = id
        self.__nome = nome
        self.__fone = fone

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_fone(self, fone):
        self.__fone = fone

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f'{self.__id}, {self.__nome}, {self.__fone}'

class NDiretoria(Modelo):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            with open('diretoria.json', 'r') as arquivo:
                a = json.load(arquivo)
                for diretoria in a:
                    d = Diretoria(diretoria['_Diretoria__id'], diretoria['_Diretoria__nome'], diretoria['_Diretoria__fone'])
                    cls.objetos.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('diretoria.json', 'w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
