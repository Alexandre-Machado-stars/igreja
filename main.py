######################### main.py 2.0 #####################################################################
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from ui_Cadastro import Ui_MainWindow
from database import Database
from PySide6 import QtCore
import pandas as pd
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("CCD™ - Conectando Corações e Dados")
        self.db = Database("Database")
        self.db.create_tables()

        # Atualiza a tabela de membros
        self.update_cadastramento_table()

        # Atualiza a tabela de lançamento de ofertas
        self.update_lancamentoofertas_table()

        # Connect signals and slots tela listadecadastro
        self.ui.btn_executar1.clicked.connect(self.cadastramento)
        self.ui.btn_excluir.clicked.connect(self.excluir_dados_listadecadastro)
        self.ui.btn_excel.clicked.connect(self.gerar_excel_listadecadastro)
        # Connect signals and slots tela consultasalteracoes
        self.ui.btn_executar2.clicked.connect(self.lancamentoofertas)
        self.ui.btn_excluir2.clicked.connect(self.excluir_dados_consultasalteracoes)
        self.ui.btn_excel2.clicked.connect(self.gerar_excel_consultasalteracoes)

        self.ui.btn_toggle.clicked.connect(self.leftMenu)
        self.ui.btn_home.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_home))
        self.ui.btn_lancar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_lancar))
        self.ui.btn_sobre.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_sobre))
        self.ui.btn_cadastrar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_cadastrar))

############################# botao excluir e gerar excel tela Lista de Cadastro de Membros##############################################

    def excluir_dados_listadecadastro(self):
        # Obtenha a linha selecionada
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            # Obtenha o CPF da linha selecionada
            cpf = self.ui.tableWidget.item(selected_row, 1).text()

            # Exclua os dados do banco de dados
            self.db.delete_cadastramento(cpf)   
            self.db.show_success_message("Dados excluídos com sucesso")
            
            # Atualize a tabela após a exclusão
            self.update_cadastramento_table()

    def gerar_excel_listadecadastro(self):
        # Obtenha os dados da tabela
        dados = []
        for row in range(self.ui.tableWidget.rowCount()):
            rowData = []
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column)
                if item is not None:
                    rowData.append(item.text())
                else:
                    rowData.append("")
            dados.append(rowData)

        # Pandas com os dados
        df = pd.DataFrame(dados, columns=["Nome", "CPF", "Contato", "Email"])

        # caixa de diálogo para salvar o arquivo Excel
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar como", "", "Arquivo Excel (*.xlsx)")
        if file_path:
            # Salve o DataFrame como um arquivo Excel
            df.to_excel(file_path, index=False)
            self.db.show_success_message("Dados Gerados com sucesso")

############################# botao excluir e gerar excel tela Consultas/Alterações de Ofertas #################################################

    def excluir_dados_consultasalteracoes(self):
        # Obtenha a linha selecionada
        selected_row = self.ui.tableWidget2.currentRow()
        if selected_row != -1:
            # Obtenha o CPF da linha selecionada
            cpf = self.ui.tableWidget2.item(selected_row, 1).text()

            # Exclua os dados do banco de dados
            self.db.delete_lancamentoofertas(cpf)
            self.db.show_success_message("Dados excluídos com sucesso")

            # Atualize a tabela após a exclusão
            self.update_lancamentoofertas_table()

    def gerar_excel_consultasalteracoes(self):
        # Obtenha os dados da tabela
        dados = []
        for row in range(self.ui.tableWidget2.rowCount()):
            rowData = []
            for column in range(self.ui.tableWidget2.columnCount()):
                item = self.ui.tableWidget2.item(row, column)
                if item is not None:
                    rowData.append(item.text())
                else:
                    rowData.append("")
            dados.append(rowData)

        # Pandas com os dados
        df = pd.DataFrame(dados, columns=["Nome", "CPF", "Valor"])

        # caixa de diálogo para salvar o arquivo Excel
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar como", "", "Arquivo Excel (*.xlsx)")
        if file_path:
            # Salve o DataFrame como um arquivo Excel
            df.to_excel(file_path, index=False)
            self.db.show_success_message("Dados Gerados com sucesso")

    def update_cadastramento_table(self):
        dados = self.db.fetch_cadastramento()
        self.populate_table(self.ui.tableWidget, dados)

    def update_lancamentoofertas_table(self):
        dados = self.db.fetch_lancamentoofertas()
        self.populate_table(self.ui.tableWidget2, dados)

    def populate_table(self, table_widget, data):
        table_widget.clearContents()
        table_widget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(str(item)))

    def leftMenu(self):
        width = self.ui.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.ui.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def cadastramento(self):
        nome = self.ui.txt_nome.text()
        cpf = self.ui.txt_cpf.text()
        contato = self.ui.txt_contato.text()
        email = self.ui.txt_email.text()

        # Verifica se todos os campos foram preenchidos
        if nome and cpf and contato and email:
            try:
                # Insere os dados no banco de dados
               self.db.insert_cadastramento(nome, cpf, contato, email)
               # Atualiza a tabela de membros
               self.update_cadastramento_table()
               # Limpa os campos de entrada após a inserção
               self.clear_input_fields()
               # Exibe uma mensagem de sucesso
               self.db.show_success_message("Cadastro realizado com sucesso!")
            except sqlite3.IntegrityError:
               # Exibe uma mensagem de erro se já existir um cadastro com o mesmo CPF
               self.db.show_error_message("Já existe um cadastro com este número de CPF, favor verifique na tabela Membros")
        else:
               # Exibe uma mensagem de erro se algum campo estiver vazio
               self.db.show_error_message("Por favor, preencha todos os campos.")

    def lancamentoofertas(self):
        nome = self.ui.txt_nome2.text()
        cpf = self.ui.txt_cpf2.text()
        valor = self.ui.txt_valor2.text()

        # Verifica se todos os campos foram preenchidos
        if nome and cpf and valor:
            try:
               # Insere os dados no banco de dados
               self.db.insert_lancamentoofertas(nome, cpf, valor)
               # Atualiza a tabela de lançamento de ofertas
               self.update_lancamentoofertas_table()
               # Limpa os campos de entrada após a inserção
               self.clear_input_fields()
               self.db.show_success_message("Cadastro realizado com sucesso!")
            except sqlite3.IntegrityError:
               # Exibe uma mensagem de erro se já existir um cadastro com o mesmo CPF
               self.db.show_error_message("Já existe um Lançamento com este número de CPF, favor verifique na tabela Consultas/Alterações")
        else:
               # Exibe uma mensagem de erro se algum campo estiver vazio
               self.db.show_error_message("Por favor, preencha todos os campos.")

    def clear_input_fields(self):
        self.ui.txt_nome.clear()
        self.ui.txt_cpf.clear()
        self.ui.txt_contato.clear()
        self.ui.txt_email.clear()
        self.ui.txt_nome2.clear()
        self.ui.txt_cpf2.clear()
        self.ui.txt_valor2.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())