import streamlit as st
import pandas as pd
from view import View

class AgendaHojeUI:
  def main():
    st.header("Agenda de Hoje")
    AgendaHojeUI.listar()

  def listar():
    agendas = View.agenda_listar_hoje()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append([obj.get_datatime()])
      df = pd.DataFrame(dic, columns=['Data'])
      st.dataframe(df, hide_index=True)