import streamlit as st
from view import View
import time

class EditarPerfilProfessorUI:

  def main():
    st.header("Editar Perfil")
    EditarPerfilProfessorUI.editar_perfil()

  def editar_perfil():
    id = st.session_state['professor_id']
    diretorias = View.diretoria_listar()
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    fone = st.text_input("Fone")
    senha = st.text_input("Senha")
    diretoria = st.selectbox('Diretoria', diretorias)
    if st.button("Editar"):
        View.editar_perfil_professor(id, nome, email, fone, senha, diretoria.get_id())
        st.success("Perfil editado com sucesso!")
        time.sleep(2)
        st.rerun()