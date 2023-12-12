import streamlit as st
import pandas as pd
from view import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.inserir()
  
  def inserir():
    diretorias = View.diretoria_listar()
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    diretoria = st.selectbox('Diretoria', diretorias, index=None, placeholder='Selecione a diretoria')
    if st.button("Inserir"):
      View.professor_inserir(nome, email, fone, senha, diretoria.get_id())
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()