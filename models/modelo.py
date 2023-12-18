from abc import ABC, abstractclassmethod

class Modelo(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for objeto in cls.objetos:
            if objeto.get_id() > id: id = objeto.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_id() == id: return objeto
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        objeto = cls.listar_id(obj.get_id())
        if objeto is not None:
            cls.objetos.remove(objeto)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        objeto = cls.listar_id(obj.get_id())
        if objeto is not None:
            cls.objetos.remove(objeto)
            cls.salvar()

    @abstractclassmethod
    def abrir(): pass

    @abstractclassmethod
    def salvar(): pass