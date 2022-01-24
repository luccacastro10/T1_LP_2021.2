from tkinter import *
from tkinter import Tk
from tkinter import font

from Classe_Clientes import Clientes

class Aplicação_Operacoes:

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
        self.container7["pady"] = 15
        self.container7.pack()


        # Container 1
        self.titulo = Label(self.container1, text="Operações")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        # Container 2
        self.BtnSaldo = Button(self.container2)
        self.BtnSaldo["text"] = "Ver Saldo"
        self.BtnSaldo["font"] = ("Calibri", "12")
        self.BtnSaldo["width"] = 24
        self.BtnSaldo["command"] = self.ver_saldo
        self.BtnSaldo.pack(side=LEFT)

        self.BTnTransaçao = Button(self.container2)
        self.BTnTransaçao["text"] = "Transação"
        self.BTnTransaçao["font"] = ("Calibri", "12")
        self.BTnTransaçao["width"] = 24
        self.BTnTransaçao.pack(side=RIGHT)

        # Container 3
        self.BtnSacar = Button(self.container3)
        self.BtnSacar["text"] = "Sacar"
        self.BtnSacar["font"] = ("Calibri", "12")
        self.BtnSacar["width"] = 24
        self.BtnSacar.pack(side=LEFT)

        self.BtnHistorico = Button(self.container3)
        self.BtnHistorico["text"] = "Historico"
        self.BtnHistorico["font"] = ("Calibri", "12")
        self.BtnHistorico["width"] = 24
        self.BtnHistorico.pack(side=RIGHT)


        # Container 7
        self.lblmsg = Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()




    def ver_saldo(self):
        
        cliente =  Clientes()

        Id = self.txtId.get()

        self.lblmsg["text"] = cliente.Ver_Saldo(Id)

        self.txtValor.delete(0, END)
        self.txtValor.insert(INSERT, cliente.saldo)        