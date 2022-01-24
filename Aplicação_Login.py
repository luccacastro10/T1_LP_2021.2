from Aplicação_Operacoes import Aplicação_Operacoes
from Classe_Clientes import Clientes
from tkinter import *
from tkinter import Tk
from tkinter import font

# Aplicação para a Classe Clientes

class Aplicação_Login:

    def __init__(self, master=None):

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()


        # Container 1
        # Contem a escrita (Login:)
        self.titulo = Label(self.container1, text="Login:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        
        
        # Container 2
        # Contem a escrita (Numero da Conta:)
        # E uma entrada ao lado
        self.lblNconta = Label(self.container2,text="Numero da Conta:", width=15)
        self.lblNconta.pack(side=LEFT)

        self.txtNconta = Entry(self.container2)
        self.txtNconta["width"] = 20
        self.txtNconta.pack(side=LEFT)

        
        
        # Container 3
        # Contem a escrita (Senha:)
        # E uma entrada ao lado       
        self.lblsenha= Label(self.container3, text="Senha:", width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container3)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha.pack(side=LEFT)


        # Container 4
        # Contem um botao com a função de verificar o login
        # e abrir a janela de operações caso o login esteja correto
        self.autenticar = Button(self.container4)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.container4, text="")
        self.mensagem.pack()



    #Método verificar senha
    def verificaSenha(self):

        cliente = Clientes()

        Nconta = self.txtNconta.get()
        senha = self.txtsenha.get()

        self.txtNconta.delete(0, END)
        self.txtsenha.delete(0, END)


        # Verifica se o cliente é cadastrado
        cliente.Procura_Conta(Nconta)

        if Nconta == cliente.Nconta and senha == cliente.senha:
            
            # Se o numero da conta e a senha conferirem,
            # é aberta a janela de operações
            root2 = Tk()
            Aplicação_Operacoes(root2)
            root2.mainloop()
        else:
            self.mensagem["text"] = "Erro na autenticação"

  



root = Tk()
Aplicação_Login(root)
root.mainloop()