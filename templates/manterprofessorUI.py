import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfessorUI:
    def main():
        st.header("Cadastro de Professores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfessorUI.listar()
        with tab2: ManterProfessorUI.inserir()
        with tab3: ManterProfessorUI.atualizar()
        with tab4: ManterProfessorUI.excluir()

    def listar():
        professores = View.professor_listar()
        if len(professores) == 0:
            st.write("Nenhum professor cadastrado")
        else:
            dic = []
            for obj in professores: dic.append([obj.get_id(), obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_iddiretoria()])
            df = pd.DataFrame(dic, columns=['Id', 'Nome', 'E-mail', 'Fone', 'IdDiretoria'])
            st.dataframe(df, hide_index=True)

    def inserir():
        diretorias = View.diretoria_listar()
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        diretoria = st.selectbox('Diretoria', diretorias, index=None, placeholder='Selecione a diretoria')
        if st.button("Inserir"):
            View.professor_inserir(nome, email, fone, senha, diretoria.get_id())
            st.success("Professor inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        professores = View.professor_listar()
        diretorias = View.diretoria_listar()
        if len(professores) == 0:
            st.write("Nenhum professor cadastrado")
        else:
            op = st.selectbox("Atualização de professores", professores, index=None, placeholder='Selecione o professor')
            nome = st.text_input("Informe o novo nome")
            email = st.text_input("Informe o novo e-mail")
            fone = st.text_input("Informe o novo fone")
            senha = st.text_input("Informe a nova senha")
            diretoria = st.selectbox('Nova diretoria', diretorias, index=None, placeholder='Selecione a diretoria')
        if st.button("Atualizar"):
            id = op.get_id()
            View.professor_atualizar(id, nome, email, fone, senha, diretoria.get_id())
            st.success("Professor atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def excluir():
        professores = View.professor_listar()
        if len(professores) == 0:
            st.write("Nenhum professor cadastrado")
        else:
            op = st.selectbox("Exclusão de professores", professores, index=None, placeholder='Selecione o professor')
            if st.button("Excluir"):
                id = op.get_id()
                View.professor_excluir(id)
                st.success("Professor excluído com sucesso")
                time.sleep(2)
                st.rerun()
