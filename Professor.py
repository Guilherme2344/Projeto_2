import json
from datetime import datetime

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
        return f'{self.__id}, {self.__nome},{self.__email}, {self.__fone},{self.__senha}, {self.__iddiretoria}'

class NProfessor:
    __Professor = []

    @classmethod
    def inserir(cls, obj):
        NProfessor.abrir()
        id = 0
        for Professor in cls.__Professores:
            if Professor.get_id() > id: id = Professor.get_id()
        obj.set_id(id + 1)
        cls.__Professor.append(obj)
        NProfessor.salvar()

    @classmethod
    def listar(cls):
        NProfessor.abrir()
        return cls.__Professor

    @classmethod
    def listar_id(cls, id):
        NProfessor.abrir()
        for professor in cls.__Professores:
            if professor.get_id() == id: return professor
        return None

    @classmethod
    def atualizar(cls, obj):
        NProfessor.abrir()
        professor = cls.listar_id(obj.get_id())
        if professor is not None:
            professor.set_id(obj.get_id())
            professor.set_nome(obj.get_nome())
            professor.set_fone(obj.get_fone())
            professor.set_email(obj.get_email())
            professor.set_senha(obj.get_senha())
            professor.set_idDiretoria(obj.get_idDiretoria())
            NProfessor.salvar()

    @classmethod
    def excluir(cls, obj):
        NProfessor.abrir()
        Professor = cls.listar_id(obj.get_id())
        if Professor is not None:
            cls.__Professores.remove(Professor)
            NProfessor.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__Professores = []
            with open('Professores.json', 'r') as arquivo:
                a = json.load(arquivo)
                for professor in a:
                    d = (professor['__id'], professor['__nome'], professor["__email"], professor ["fone"],professor ["senha"],professor ["idDiretoria"])
                    cls.__Professores.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('Professores.json', 'w') as arquivo:
            json.dump(cls.__Professores, arquivo, default=vars)

