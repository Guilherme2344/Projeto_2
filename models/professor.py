import json
from models.modelo import Modelo

class Professor:
    def __init__(self, id, nome, email, fone, senha, idDiretoria):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha
        self.__iddiretoria = idDiretoria

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def set_senha(self, senha):
        self.__senha = senha
    def set_iddiretoria(self, idDiretoria):
        self.__iddiretoria = idDiretoria

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_senha(self):
        return self.__senha
    def get_iddiretoria(self):
        return self.__iddiretoria
    def __str__(self):
        return f'{self.__id}, {self.__nome}, {self.__email}, {self.__fone}, {self.__senha}, {self.__iddiretoria}'

class NProfessor(Modelo):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            with open('professores.json', 'r') as arquivo:
                a = json.load(arquivo)
                for professor in a:
                    d = Professor(professor['_Professor__id'], professor['_Professor__nome'], professor['_Professor__email'], professor['_Professor__fone'], professor['_Professor__senha'],professor['_Professor__iddiretoria'])
                    cls.objetos.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('professores.json', 'w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)