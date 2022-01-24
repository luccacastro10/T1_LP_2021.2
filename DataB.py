import sqlite3

# Cria uma database para o Banco
class db():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists banco (
                 Id integer primary key autoincrement,
                 Nconta text,
                 nome text,
                 cpf text,
                 saldo real,
                 senha text)""")
        self.conexao.commit()
        c.close()

