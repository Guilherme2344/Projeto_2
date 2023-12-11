import json
from datetime import datetime

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

class NDiretoria:
    __Diretorias = []

    @classmethod
    def inserir(cls, obj):
        NDiretoria.abrir()
        id = 0
        for Diretoria in cls.__Diretorias:
            if Diretoria.get_id() > id: id = Diretoria.get_id()
        obj.set_id(id + 1)
        cls.__Diretorias.append(obj)
        NDiretoria.salvar()

    @classmethod
    def listar(cls):
        NDiretoria.abrir()
        return cls.__Diretorias

    @classmethod
    def listar_id(cls, id):
        NDiretoria.abrir()
        for Diretoria in cls.__Diretorias:
            if Diretoria.get_id() == id: return Diretoria
        return None

    @classmethod
    def atualizar(cls, obj):
        NDiretoria.abrir()
        diretoria = cls.listar_id(obj.get_id())
        if Diretoria is not None:
            diretoria.set_id(obj.get_id())
            diretoria.set_nome(obj.get_nome())
            diretoria.set_fone(obj.get_fone())
            NDiretoria.salvar()

    @classmethod
    def excluir(cls, obj):
        NDiretoria.abrir()
        Diretoria = cls.listar_id(obj.get_id())
        if Diretoria is not None:
            cls.__Diretorias.remove(Diretoria)
            NDiretoria.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__Diretorias = []
            with open('Diretoria.json', 'r') as arquivo:
                a = Diretoria.load(arquivo)
                for diretoria in a:
                    d = Diretoria(diretoria['__id'], diretoria['__nome'], diretoria['__fone'])
                    cls.__Diretorias.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('Diretoria.json', 'w') as arquivo:
            json.dump(cls.__Diretorias, arquivo, default=vars)
