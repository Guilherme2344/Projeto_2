import streamlit as st
import pandas as pd
import time
from view import View

class ManterDiretoriaUI:
    def main():
        st.header("Cadastro de Diretorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterDiretoriaUI.listar()
        with tab2: ManterDiretoriaUI.inserir()
        with tab3: ManterDiretoriaUI.atualizar()
        with tab4: ManterDiretoriaUI.excluir()

    def listar():
        diretorias = View.diretoria_listar()
        if len(diretorias) == 0:
            st.write("Nenhuma diretoria cadastrada")
        else:
            dic = []
            for obj in diretorias: dic.append([obj.get_id(), obj.get_nome(), obj.get_fone()])
            df = pd.DataFrame(dic, columns=['Id', 'Nome', 'Fone'])
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            if nome == '': st.error('Informe um nome')
            elif fone == '': st.error('Informe um fone')
            else:
                View.diretoria_inserir(nome, fone)
                st.success("Diretoria inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        diretorias = View.diretoria_listar()
        if len(diretorias) == 0:
            st.write("Nenhum diretoria cadastrado")
        else:
            op = st.selectbox("Atualização de Diretorias", diretorias)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            fone = st.text_input("Informe o novo fone", op.get_fone())
        if st.button("Atualizar"):
            if op == None: st.error('Selecione uma diretoria')
            elif nome == '': st.error('Informe um nome')
            elif fone == '': st.error('Informe um fone')
            else:
                id = op.get_id()
                View.diretoria_atualizar(id, nome, fone)
                st.success("diretoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        diretorias = View.diretoria_listar()
        if len(diretorias) == 0:
            st.write("Nenhum diretoria cadastrado")
        else:
            op = st.selectbox("Exclusão de diretorias", diretorias)
        if st.button("Excluir"):
            if op == None: st.error('Selecione uma diretoria')
            else:
                id = op.get_id()
                View.diretoria_excluir(id)
                st.success("diretoria excluída com sucesso")
                time.sleep(2)
                st.rerun()