#################################### database.py versão 1.0 ###################################################################
import sqlite3
from PySide6.QtWidgets import QMessageBox

class Database:
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        try:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS cadastramento (
                            nome TEXT,
                            cpf TEXT PRIMARY KEY,
                            contato TEXT,
                            email TEXT
                            )""")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS lancamentoofertas ( 
                            id INTEGER PRIMARY KEY,                       
                            nome,
                            cpf TEXT,
                            valor TEXT
                            )""")
            self.conn.commit()
        except sqlite3.Error as e:
            self.show_error_message("Erro na criação das tabelas: " )


    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def show_success_message(self, message):
        QMessageBox.information(None, "Sucesso", message)

    def show_error_message(self, message):
        QMessageBox.critical(None, "Erro", message)


    def insert_cadastramento(self, nome, cpf, contato, email):
        self.cur.execute("INSERT INTO cadastramento VALUES (?, ?, ?, ?)", (nome, cpf, contato, email))
        self.conn.commit()

    def fetch_cadastramento(self):
        self.cur.execute("SELECT * FROM cadastramento")
        return self.cur.fetchall()

    def update_cadastramento(self, nome, cpf, contato, email):
        self.cur.execute("UPDATE cadastramento SET nome=?, contato=?, email=? WHERE cpf=?", (nome, contato, email, cpf))
        self.conn.commit()

    def delete_cadastramento(self, cpf):
        self.cur.execute("DELETE FROM cadastramento WHERE cpf=?", (cpf,))
        self.conn.commit()

    def insert_lancamentoofertas(self, nome, cpf, valor):
        self.cur.execute("INSERT INTO lancamentoofertas VALUES (?, ?, ?)", (nome, cpf, valor))
        self.conn.commit()

    def fetch_lancamentoofertas(self):
        self.cur.execute("SELECT * FROM lancamentoofertas")
        return self.cur.fetchall()

    def update_lancamentoofertas(self, nome, cpf, valor):
        self.cur.execute("UPDATE lancamentoofertas SET nome=?, valor=? WHERE cpf=?", (nome, valor, cpf))
        self.conn.commit()

    def delete_lancamentoofertas(self, cpf):
        self.cur.execute("DELETE FROM lancamentoofertas WHERE cpf=?", (cpf,))
        self.conn.commit()