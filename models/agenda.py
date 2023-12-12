import json
from datetime import datetime

class Agenda:
    def __init__(self, id, datatime,idCurso,idProfessor ):
        self.__id = id
        self.__datatime = datatime
        self.__idCurso = idCurso
        self.__idProfessor = idProfessor

    def set_id(self, id):
        self.__id = id
    def set_datatime(self, datatime):
        self.__datatime = datatime
    def set_idCurso(self, idCurso):
        self.__idCurso = idCurso
    def set_idProfessor(self, idProfessor):
        self.__idProfessor = idProfessor
    def get_id(self):
        return self.__id
    def get_datatime(self):
        return self.__datatime
    def get_idCurso(self):
        return self.__idCurso
    def get_idProfessor(self):
        return self.__idProfessor
    def to_json(self):
        return {'__id':self.__id, '__datatime':self.__datatime.strftime('%d/%m/%Y %H:%M'), '__idCurso':self.__idCurso, '__idProfessor':self.__idProfessor}
    def __str__(self):
        return f'{self.__id}, {self.__datatime}, {self.__idCurso}, {self.__idProfessor}'

class NAgenda:
    __agendas = []

    @classmethod
    def inserir(cls, obj):
        NAgenda.abrir()
        id = 0
        for agenda in cls.__agendas:
            if agenda.get_id() > id: id = agenda.get_id()
        obj.set_id(id + 1)
        cls.__agendas.append(obj)
        NAgenda.salvar()

    @classmethod
    def listar(cls):
        NAgenda.abrir()
        return cls.__agendas

    @classmethod
    def listar_id(cls, id):
        NAgenda.abrir()
        for agenda in cls.__agendas:
            if agenda.get_id() == id: return agenda
        return None

    @classmethod
    def atualizar(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        if agenda is not None:
            agenda.set_id(obj.get_id())
            agenda.set_datatime(obj.get_datatime())
            agenda.set_idCurso(obj.get_idCurso())
            agenda.set_idProfessor(obj.get_idProfessor())
            NAgenda.salvar()

    @classmethod
    def excluir(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        if agenda is not None:
            cls.__agendas.remove(agenda)
            NAgenda.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__agendas = []
            with open('agendas.json', 'r') as arquivo:
                a = json.load(arquivo)
                for agenda in a:
                    d = Agenda(agenda['__id'], datetime.strptime(agenda['__datatime'], '%d/%m/%Y %H:%M'), agenda['__idCurso'], agenda['__idProfessor'])
                    cls.__agendas.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('agendas.json', 'w') as arquivo:
            json.dump(cls.__agendas, arquivo, default=Agenda.to_json)

