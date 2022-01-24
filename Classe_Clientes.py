import sqlite3
from Classe_Banco import Banco
import DataB


# Permite ao cliente realizar operações em sua conta

class Clientes(Banco):
    
    def __init__(self,Id = 0,Nconta="",nome="",cpf="",saldo=0,senha=""):
        Banco.__init__(self,Id,Nconta,nome,cpf,saldo,senha)


        # Metodos com as operações que podem ser realizadas
        # pelo cliente

    def Depositar(self,event):
        pass


    def Ver_Saldo(self,Id):
        
        banco = DataB.db()

        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM banco WHERE Nconta = '" + Id + "'  ")            


            for linha in c:
                self.saldo = linha[4]

            c.close()
        
            return "Saldo disponivel na conta"
        except:
            return "Não foi possivel visualizar o saldo"


    def Transação(self):
        pass

    def historico(self):
        pass

    
    # Metodo para confirmar a presença de uma conta no DB
    # antes de verificar se o Login esta correto
    def Procura_Conta(self,Nconta):

        banco = DataB.db()
  
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM banco WHERE Nconta = '" + Nconta + "'  ")
            

            for linha in c:
                self.Nconta = linha[1]
                self.senha = linha[5]

            c.close()
        
        except:
            self.Nconta = False