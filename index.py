from templates.agendahojeUI import AgendaHojeUI
from templates.editarperfiladminUI import EditarPerfilAdminUI
from templates.editarperfilprofessorUI import EditarPerfilProfessorUI
from templates.loginUI import LoginUI
from templates.manteragendaUI import ManterAgendaUI
from templates.mantercursoUI import ManterCursoUI
from templates.manterdiretoriaUI import ManterDiretoriaUI
from templates.manterprofessorUI import ManterProfessorUI
from templates.abrircontaUI import AbrirContaUI
from view import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Agenda", "Manter Professor", "Manter Diretoria", "Manter Curso", "Editar Perfil"])
    if op == "Manter Agenda": ManterAgendaUI.main()
    if op == "Manter Professor": ManterProfessorUI.main()
    if op == "Manter Diretoria": ManterDiretoriaUI.main()
    if op == "Manter Curso": ManterCursoUI.main()
    if op == "Editar Perfil": EditarPerfilAdminUI.main()

  def menu_professor():
    op = st.sidebar.selectbox("Menu", ["Agenda de Hoje", "Editar Perfil"])
    if op == "Agenda de Hoje": AgendaHojeUI.main()
    if op == "Editar Perfil": EditarPerfilProfessorUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["professor_id"]
      del st.session_state["professor_nome"]
      st.rerun()

  def sidebar():
    if "professor_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["professor_nome"])
      professores = View.professor_listar()
      if st.session_state["professor_nome"] == professores[0].get_nome(): IndexUI.menu_admin()
      else: IndexUI.menu_professor()
      IndexUI.btn_logout()  

  def main():
    View.professor_admin()
    IndexUI.sidebar()

IndexUI.main()