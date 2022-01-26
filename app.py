from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk,Image
from matplotlib.pyplot import text
from ttkwidgets import CheckboxTreeview
import disciplina

status = "Disciplinas Cursadas"

splash_screen = Tk()
splash_screen.geometry("+500+250")
splash_screen.overrideredirect(True) #Desabilita o título da janela
splash_screen.wm_attributes("-transparentcolor", 'grey')

img = ImageTk.PhotoImage(Image.open("minerva.icon.png"))
label = Label(image=img, bg="grey")
label.grid()


def mainWindow():
    splash_screen.destroy()
    menu = Tk()
    menu.title("Trabalho LP")
    menu.geometry("500x500+450+250")
    menu.minsize(200,200)
    menu.iconbitmap("minerva.icon.png")

    nb = ttk.Notebook(menu)
    nb.place(x=0, y=0, width=500, height=500)

    aba1 = Frame(nb)
    nb.add(aba1, text="Menu")
    aba2 = Frame(nb)
    nb.add(aba2, text="Grade Curricular")
    aba3 = Frame(nb)
    nb.add(aba3, text="Disciplinas Cursadas")
    aba4 = Frame(nb)
    nb.add(aba4, text="Disciplinas em Curso")
    aba5 = Frame(nb)
    nb.add(aba5, text="Disciplinas Pendentes")

    f = open("grade.txt", encoding="utf8")
    disciplinasSelecionadas = []
    grade = f.readlines()

    gradeLabel = Label(aba2, text="Grade Curricular: Engenharia de Controle e Automação", bd=2, font=25, borderwidth=2, relief="flat")
    gradeLabel.pack(pady=10)
    
    def value_changed():
        status = mySpin.get()
        selectLabel["text"] = ("Selecione as " + status)

    mySpin = Spinbox(aba2, values=("Disciplinas Cursadas", "Disciplinas em Curso", "Disciplinas Pendentes"), width=50, relief="groove", command=value_changed)
    mySpin.pack( padx=5)

    selectLabel = Label(aba2, text= ("Selecione as " + status), bd=2, font=25, borderwidth=2, relief="flat")
    selectLabel.pack()

    def selecionarDisciplinas():
        status = mySpin.get()

        disciplinasSelecionadas = []

        if status == "Disciplinas Cursadas":
            for row in tv2.get_children():
                tv2.delete(row)
            nb.select(aba3)
        elif status == "Disciplinas em Curso":
            for row in tv3.get_children():
                tv3.delete(row)
            nb.select(aba4)
        elif status == "Disciplinas Pendentes":
            for row in tv4.get_children():
                tv4.delete(row)
            nb.select(aba5)
        
        aux = tv.get_checked()

        for i in aux:
            disciplinasSelecionadas.append(tv.item(i))

        for i in disciplinasSelecionadas:
            if status == "Disciplinas Cursadas":
                tv2.insert("", "end", values=i["values"])
            elif status == "Disciplinas em Curso":
                tv3.insert("", "end", values=i["values"])
            elif status == "Disciplinas Pendentes":
                tv4.insert("", "end", values=i["values"])
        

    

    saveButton = Button(aba2, text ="Salvar Disciplinas Selecionadas", command = selecionarDisciplinas)
    saveButton.pack(pady=5)
    
    tv = CheckboxTreeview(aba2, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings", "tree"), height=15)
    tv.column("#0", width=45)
    tv.column("Código",  width=60, anchor=CENTER, stretch=NO)
    tv.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    tv.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    tv.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    tv.column("Período", width=60, anchor=CENTER, stretch=NO)
    tv.heading("Código",  text="CÓDIGO")
    tv.heading("Disciplina", text="DISCIPLINA")
    tv.heading("Créditos",  text="CRÉDITOS")
    tv.heading("C.H",  text="C.H")   
    tv.heading("Período", text="PERÍODO")
    tv.pack()

    cursadasLabel = Label(aba3, text="Disciplinas Cursadas", bd=2, font=25, borderwidth=2, relief="flat")
    cursadasLabel.pack(pady=10)

    tv2 = ttk.Treeview(aba3, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))
    tv2.column("Código",  width=60, anchor=CENTER, stretch=NO)
    tv2.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    tv2.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    tv2.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    tv2.column("Período", width=60, anchor=CENTER, stretch=NO)
    tv2.heading("Código",  text="CÓDIGO")
    tv2.heading("Disciplina", text="DISCIPLINA")
    tv2.heading("Créditos",  text="CRÉDITOS")
    tv2.heading("C.H",  text="C.H")   
    tv2.heading("Período", text="PERÍODO")
    tv2.pack()

    emCursoLabel = Label(aba4, text="Disciplinas Em Curso", bd=2, font=25, borderwidth=2, relief="flat")
    emCursoLabel.pack(pady=10)

    tv3 = ttk.Treeview(aba4, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))
    tv3.column("Código",  width=60, anchor=CENTER, stretch=NO)
    tv3.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    tv3.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    tv3.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    tv3.column("Período", width=60, anchor=CENTER, stretch=NO)
    tv3.heading("Código",  text="CÓDIGO")
    tv3.heading("Disciplina", text="DISCIPLINA")
    tv3.heading("Créditos",  text="CRÉDITOS")
    tv3.heading("C.H",  text="C.H")   
    tv3.heading("Período", text="PERÍODO")
    tv3.pack()

    pendentesLabel = Label(aba5, text="Disciplinas Pendentes", bd=2, font=25, borderwidth=2, relief="flat")
    pendentesLabel.pack(pady=10)

    tv4 = ttk.Treeview(aba5, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))
    tv4.column("Código",  width=60, anchor=CENTER, stretch=NO)
    tv4.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    tv4.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    tv4.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    tv4.column("Período", width=60, anchor=CENTER, stretch=NO)
    tv4.heading("Código",  text="CÓDIGO")
    tv4.heading("Disciplina", text="DISCIPLINA")
    tv4.heading("Créditos",  text="CRÉDITOS")
    tv4.heading("C.H",  text="C.H")   
    tv4.heading("Período", text="PERÍODO")
    tv4.pack()


    for materia in grade:
        values = materia.split(",")
        tv.insert("", "end", values=values)


splash_screen.after(2000, mainWindow)
mainloop()