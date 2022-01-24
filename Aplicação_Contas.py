import Classe_Clientes
from Classe_Banco import Banco
from tkinter import *
from tkinter import Tk
from tkinter import font

# Aplicação para a Classe Banco 
class Aplicação_Contas:

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
        
        
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()


        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 10
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 10
        self.container7.pack()        
        
        self.container8 = Frame(master)
        self.container8["pady"] = 15
        self.container8.pack()


        # Container 1
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        # Container 2
        self.lblId = Label(self.container2, text="IdUsuario:", width=10)
        self.lblId.pack(side=LEFT)

        self.txtId = Entry(self.container2)
        self.txtId["width"] = 25
        self.txtId.pack(side=LEFT)
        
        
        # Container 3
        self.lblNconta = Label(self.container3,text="Numero da Conta:", width=20,height=5)
        self.lblNconta.pack(side=LEFT)

        self.txtNconta = Entry(self.container3)
        self.txtNconta["width"] = 15
        self.txtNconta.pack(side=LEFT)


        # Botao de Busca que procura pelo numero da conta
        self.btnBuscar = Button(self.container3, text="Buscar", width=10)
        self.btnBuscar["command"] = self.buscar_conta
        self.btnBuscar.pack(side=RIGHT)



        # Container 4
        self.lblnome = Label(self.container4, text="Nome:", width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["width"] = 25
        self.txtnome.pack(side=LEFT)



        # Container 5
        self.lblcpf = Label(self.container5, text="CPF:", width=10)
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container5)
        self.txtcpf["width"] = 25
        self.txtcpf.pack(side=LEFT)



        # Container 6
        self.lblsenha= Label(self.container6, text="Senha:", width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container6)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha.pack(side=LEFT)

        

        #Botoes (Container 7):

        #Criar Conta
        self.bntInsert = Button(self.container7, text="Criar", width=12)
        self.bntInsert["command"] = self.cria_conta
        self.bntInsert.pack (side=LEFT)

        #Atualizar Conta
        self.bntAlterar = Button(self.container7, text="Alterar", width=12)
        self.bntAlterar["command"] = self.atualiza_conta
        self.bntAlterar.pack (side=LEFT)

        #Excluir Conta
        self.bntExcluir = Button(self.container7, text="Excluir", width=12)
        self.bntExcluir["command"] = self.deleta_conta
        self.bntExcluir.pack(side=LEFT)

        
        
        # Container 8
        #Mensagem sobre o status da operação
        self.lblmsg = Label(self.container8, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def cria_conta(self):
        cliente = Banco()

        cliente.Id = self.txtId.get()
        cliente.Nconta = self.txtNconta.get()
        cliente.nome = self.txtnome.get()
        cliente.cpf = self.txtcpf.get()
        cliente.senha = self.txtsenha.get()

        self.lblmsg["text"] = cliente.Cria_Conta()

        self.txtId.delete(0, END)
        self.txtNconta.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtsenha.delete(0, END)



    def atualiza_conta(self):
        cliente = Banco()

        cliente.Id = self.txtId.get()
        cliente.Nconta = self.txtNconta.get()
        cliente.nome = self.txtnome.get()
        cliente.cpf = self.txtcpf.get()
        cliente.senha = self.txtsenha.get()

        self.lblmsg["text"] = cliente.Atualiza_Conta()

        self.txtId.delete(0, END)
        self.txtNconta.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtsenha.delete(0, END)



    def deleta_conta(self):
        cliente = Banco()

        cliente.Nconta = self.txtNconta.get()

        self.lblmsg["text"] = cliente.Remove_Conta()

        self.txtId.delete(0, END)
        self.txtNconta.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscar_conta(self):
        cliente = Banco()

        Nconta = self.txtNconta.get()

        self.lblmsg["text"] = cliente.Busca_Conta(Nconta)

        self.txtId.delete(0, END)
        self.txtId.insert(INSERT, cliente.Id)


        self.txtNconta.delete(0, END)
        self.txtNconta.insert(INSERT, cliente.Nconta)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, cliente.nome)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, cliente.cpf)



root = Tk()
Aplicação_Contas(root)
root.mainloop()



