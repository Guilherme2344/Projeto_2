import streamlit as st
import pandas as pd
import time
from view import View
from datetime import datetime

class ManterAgendaUI:
    def main():
        st.header("Cadastro de Agendas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAgendaUI.listar()
        with tab2: ManterAgendaUI.inserir()
        with tab3: ManterAgendaUI.atualizar()
        with tab4: ManterAgendaUI.excluir()

    def listar():
        agendas = View.agenda_listar()
        if len(agendas) == 0:
            st.write("Nenhuma agenda cadastrada")
        else:
            dic = []
            for obj in agendas: dic.append([obj.get_id(), obj.get_datatime(), obj.get_idCurso(), obj.get_idProfessor()])
            df = pd.DataFrame(dic, columns=['Id', 'Data', 'IdCurso', 'IdProfessor'])
            st.dataframe(df, hide_index=True)

    def inserir():
        cursos = View.curso_listar()
        professores = View.professor_listar()
        data = st.text_input('Data no formato dd/mm/aaaa hh:mm')
        curso = st.selectbox('Curso', cursos, index=None, placeholder='Selecione o curso')
        professor = st.selectbox('Professor', professores, index=None, placeholder='Selecione o professor')
        if st.button("Inserir"):
            data = datetime.strptime(data, '%d/%m/%Y %H:%M')
            View.agenda_inserir(data, curso.get_id(), professor.get_id())
            st.success("Agenda inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        agendas = View.agenda_listar()
        cursos = View.curso_listar()
        professores = View.professor_listar()
        if len(agendas) == 0:
            st.write('Nenhuma agenda cadastrada')
        else:
            op = st.selectbox('Agenda', agendas)
            data = st.text_input('Nova data no formato dd/mm/aaaa hh:mm')
            curso = st.selectbox('Curso', cursos, index=None, placeholder='Selecione o novo curso')
            professor = st.selectbox('Professor', professores, index=None, placeholder='Selecione o novo professor')
            if st.button("Atualizar"):
                data = datetime.strptime(data, '%d/%m/%Y %H:%M')
                id = op.get_id()
                View.agenda_atualizar(id, data, curso.get_id(), professor.get_id())
                st.success("Agenda atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        agendas = View.agenda_listar()
        if len(agendas) == 0:
            st.write('Nenhuma agenda cadastrada')
        else:
            op = st.selectbox('Agenda', agendas, index=None, placeholder='Selecione a agenda a ser excluída')
            if st.button("Excluir"):
                id = op.get_id()
                View.agenda_excluir(id)
                st.success("Agenda excluída com sucesso")
                time.sleep(2)
                st.rerun()