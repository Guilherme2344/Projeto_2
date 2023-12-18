import json
from datetime import datetime
from models.modelo import Modelo

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

class NAgenda(Modelo):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            with open('agendas.json', 'r') as arquivo:
                a = json.load(arquivo)
                for agenda in a:
                    d = Agenda(agenda['__id'], datetime.strptime(agenda['__datatime'], '%d/%m/%Y %H:%M'), agenda['__idCurso'], agenda['__idProfessor'])
                    cls.objetos.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('agendas.json', 'w') as arquivo:
            json.dump(cls.objetos, arquivo, default=Agenda.to_json)