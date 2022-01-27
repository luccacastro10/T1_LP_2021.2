from tkinter import *
from tkinter import ttk
from ttkwidgets import CheckboxTreeview

class TableView(CheckboxTreeview):
    
    def __init__(self, aba, isCheckBox):
        self._isCheckBox = isCheckBox
        if (isCheckBox):
            super().__init__(aba, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings", "tree"))
        else:
            super().__init__(aba, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))

    def setTableView(self):
        if(self._isCheckBox):
            self.column("#0", width=45)
        self.column("Código",  width=60, anchor=CENTER, stretch=NO)
        self.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
        self.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
        self.column("C.H",  width=40, anchor=CENTER, stretch=NO)
        self.column("Período", width=60, anchor=CENTER, stretch=NO)
        self.heading("Código",  text="CÓDIGO")
        self.heading("Disciplina", text="DISCIPLINA")
        self.heading("Créditos",  text="CRÉDITOS")
        self.heading("C.H",  text="C.H")   
        self.heading("Período", text="PERÍODO")

    