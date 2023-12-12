import streamlit as st
import pandas as pd
import time
from view import View

class ManterCursoUI:
    def main():
        st.header("Cadastro de Cursos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCursoUI.listar()
        with tab2: ManterCursoUI.inserir()
        with tab3: ManterCursoUI.atualizar()
        with tab4: ManterCursoUI.excluir()

    def listar():
        cursos = View.curso_listar()
        if len(cursos) == 0:
            st.write("Nenhum curso cadastrado")
        else:
            dic = []
            for obj in cursos: dic.append([obj.get_id(), obj.get_nome(), obj.get_descricao(), obj.get_iddiretoria()])
            df = pd.DataFrame(dic, columns=['Id', 'Nome', 'Descrição', 'IdDiretoria'])
            st.dataframe(df, hide_index=True)

    def inserir():
        diretorias = View.diretoria_listar()
        nome = st.text_input("Informe o nome")
        descricao = st.text_input("Informe a descrição")
        diretoria = st.selectbox('Diretoria', diretorias, index=None, placeholder='Selecione a diretoria')
        if st.button("Inserir"):
            View.curso_inserir(nome, descricao, diretoria.get_id())
            st.success("Curso inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        cursos = View.curso_listar()
        diretorias = View.diretoria_listar()
        if len(cursos) == 0:
            st.write("Nenhum Curso cadastrado")
        else:
            op = st.selectbox("Atualização de cursos", cursos, index=None, placeholder='Selecione o curso')
            nome = st.text_input("Informe o novo nome")
            descricao = st.text_input("Informe a nova descrição")
            diretoria = st.selectbox('Nova diretoria', diretorias, index=None, placeholder='Selecione a diretoria')
        if st.button("Atualizar"):
            id = op.get_id()
            View.curso_atualizar(id, nome, descricao, diretoria.get_id())
            st.success("Curso atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def excluir():
        cursos = View.curso_listar()
        if len(cursos) == 0:
            st.write("Nenhum curso cadastrado")
        else:
            op = st.selectbox("Exclusão de cursos", cursos, index=None, placeholder='Selecione o curso')
            if st.button("Excluir"):
                id = op.get_id()
                View.curso_excluir(id)
                st.success("Curso excluído com sucesso")
                time.sleep(2)
                st.rerun()