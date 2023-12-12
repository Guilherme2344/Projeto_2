import json
from datetime import datetime

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

class NCurso:
    __Cursos = []

    @classmethod
    def inserir(cls, obj):
        NCurso.abrir()
        id = 0
        for curso in cls.__Cursos:
            if curso.get_id() > id: id = curso.get_id()
        obj.set_id(id + 1)
        cls.__Cursos.append(obj)
        NCurso.salvar()

    @classmethod
    def listar(cls):
        NCurso.abrir()
        return cls.__Cursos

    @classmethod
    def listar_id(cls, id):
        NCurso.abrir()
        for Curso in cls.__Cursos:
            if Curso.get_id() == id: return Curso
        return None

    @classmethod
    def atualizar(cls, obj):
        NCurso.abrir()
        curso = cls.listar_id(obj.get_id())
        if Curso is not None:
            curso.set_id(obj.get_id())
            curso.set_nome(obj.get_nome())
            curso.set_descricao(obj.get_descricao())
            curso.set_iddiretoria(obj.get_iddiretoria())
            NCurso.salvar()

    @classmethod
    def excluir(cls, obj):
        NCurso.abrir()
        Curso = cls.listar_id(obj.get_id())
        if Curso is not None:
            cls.__Cursos.remove(Curso)
            NCurso.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__Cursos = []
            with open('cursos.json', 'r') as arquivo:
                a = json.load(arquivo)
                for curso in a:
                    d = Curso(curso['_Curso__id'], curso['_Curso__nome'], curso['_Curso__descricao'], curso["_Curso__iddiretoria"])
                    cls.__Cursos.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('cursos.json', 'w') as arquivo:
            json.dump(cls.__Cursos, arquivo, default=vars)



