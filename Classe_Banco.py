import sqlite3
import DataB


# Cria e administra contas do banco

class Banco():
    
    def __init__(self,Id=0,Nconta="",nome="",cpf="",saldo=0,senha=""):
        self.Id = Id
        self.Nconta = Nconta
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.senha = senha

    
    # Metodos para trabalhar com as contas no DB

    def Cria_Conta(self):
        
        banco = DataB.db()

        try:

            c = banco.conexao.cursor()

            c.execute("INSERT INTO banco (Id,Nconta, nome, cpf, saldo, senha) VALUES('"+ self.Id +"','"+ self.Nconta +"','" + self.nome + "', '" + self.cpf + "', 0 ,'" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Conta Criada com sucesso"
        except:
            return "Ocorreu um erro na criação da conta"



    def Remove_Conta(self):

        banco = DataB.db()

        try:

            c = banco.conexao.cursor()

            c.execute("DELETE FROM banco WHERE Nconta ='"+ self.Nconta +"' ")

            banco.conexao.commit()
            c.close()

            return "Conta excluida com sucesso"
        except:
            return "Ocorreu um erro na exclusao da conta"



    def Atualiza_Conta(self):
        
        banco = DataB.db()

        try:

            c = banco.conexao.cursor()

            c.execute("UPDATE banco SET nome = '" + self.nome + "', senha = '" + self.senha +"' WHERE Nconta = '"+ self.Nconta + "' ")

            banco.conexao.commit()
            c.close()

            return "Conta atualizada com sucesso"
        except:
            return "Ocorreu um erro durante a alteração da conta"



    def Busca_Conta(self,Nconta):

        banco = DataB.db()
  
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM banco WHERE Nconta = '" + Nconta + "'  ")
            

            for linha in c:
                self.Id = linha[0]
                self.Nconta = linha[1]
                self.nome = linha[2]
                self.cpf = linha[3]
                self.saldo = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"        
