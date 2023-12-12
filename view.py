from models.curso import Curso, NCurso
from models.professor import Professor, NProfessor
from models.diretoria import Diretoria, NDiretoria
from models.agenda import Agenda, NAgenda
from datetime import datetime
import streamlit as st

class View:
    def curso_inserir(nome, descricao, idDiretoria):
        curso = Curso(0, nome, descricao, idDiretoria)
        NCurso.inserir(curso)

    def curso_listar():
        return NCurso.listar()

    def curso_listar_id(id):
        return NCurso.listar_id(id)

    def curso_atualizar(id, nome, descricao, idDiretoria):
        curso = Curso(id, nome, descricao, idDiretoria)
        NCurso.atualizar(curso)

    def curso_excluir(id):
        curso = Curso(id, '', '', '')
        NCurso.excluir(curso)

    def professor_inserir(nome, email, fone, senha, idDiretoria):
        professor = Professor(0, nome, email, fone, senha, idDiretoria)
        NProfessor.inserir(professor)

    def professor_listar():
        return NProfessor.listar()

    def professor_listar_id(id):
        return NProfessor.listar_id(id)

    def professor_atualizar(id, nome, email, fone, senha, idDiretoria):
        professor = Professor(id, nome, email, fone, senha, idDiretoria)
        NProfessor.atualizar(professor)

    def professor_excluir(id):
        professor = Professor(id, '', '', '', '', '')
        NProfessor.excluir(professor)

    def professor_admin():
        for professor in View.professor_listar():
            if professor.get_email() == 'admin': return

    def professor_login(email, senha):
        for professor in View.professor_listar():
            if professor.get_email() == email and professor.get_senha() == senha:
                return professor
        return None

    def diretoria_inserir(nome, fone):
        diretoria = Diretoria(0, nome, fone)
        NDiretoria.inserir(diretoria)

    def diretoria_listar():
        return NDiretoria.listar()

    def diretoria_listar_id(id):
        return NDiretoria.listar_id(id)

    def diretoria_atualizar(id, nome, fone):
        diretoria = Diretoria(id, nome, fone)
        NDiretoria.atualizar(diretoria)

    def diretoria_excluir(id):
        diretoria = Diretoria(id, '', '')
        NDiretoria.excluir(diretoria)

    def agenda_inserir(data, idDiretoria, idProfessor):
        agenda = Agenda(0, data, idDiretoria, idProfessor)
        NAgenda.inserir(agenda)

    def agenda_listar():
        return NAgenda.listar()

    def agenda_listar_id(id):
        return NAgenda.listar_id(id)

    def agenda_atualizar(id, data, idDiretoria, idProfessor):
        agenda = Agenda(id, data, idDiretoria, idProfessor)
        NAgenda.atualizar(agenda)

    def agenda_excluir(id):
        agenda = Agenda(id, '', '', '')
        NAgenda.excluir(agenda)

    def agenda_listar_hoje():
        lista = []
        hoje = datetime.today()
        for data in View.agenda_listar():
            if data.get_datatime().date() == hoje.date() and data.get_idProfessor() == st.session_state['professor_id']:
                lista.append(data)
        return lista

    def editar_perfil_admin(id, nome, email, fone, senha, idDiretoria):
        NProfessor.atualizar(Professor(id, nome, email, fone, senha, idDiretoria))

    def editar_perfil_professor(id, nome, email, fone, senha, idDiretoria):
        NProfessor.atualizar(Professor(id, nome, email, fone, senha, idDiretoria))
