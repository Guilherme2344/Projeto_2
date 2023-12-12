import streamlit as st
from view import View
import time

class LoginUI:
  def main():
    st.header("Entrar no Sistema")
    LoginUI.entrar()
  def entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      professor = View.professor_login(email, senha) 
      if professor is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + professor.get_nome())
        st.session_state["professor_id"] = professor.get_id()
        st.session_state["professor_nome"] = professor.get_nome()
      else:
        st.error("Usuário ou senha inválido(s)")
      time.sleep(2)
      st.rerun()