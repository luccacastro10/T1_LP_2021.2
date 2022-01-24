from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import disciplina


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
    menu.geometry("500x700+450+250")
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
    grade = f.readlines()

    gradeLabel = Label(aba2, text="Grade Curricular: Engenharia de Controle e Automação", bd=2, font=25, borderwidth=2, relief="flat")
    gradeLabel.pack()

    tv = ttk.Treeview(aba2, columns=("Código", "Disciplina", "Créditos", "C.H", "Período", "Situação"), show="headings", height=500)
    tv.tag_configure('highlight', background='lightblue')
    tv.column("Código",  width=60, anchor=CENTER)
    tv.column("Disciplina",  width=180, anchor=CENTER)
    tv.column("Créditos",  width=65, anchor=CENTER)
    tv.column("C.H",  width=40, anchor=CENTER)
    tv.column("Período", width=60, anchor=CENTER)
    tv.column("Situação", width=65, anchor=CENTER)
    tv.heading("Código",  text="CÓDIGO")
    tv.heading("Disciplina", text="DISCIPLINA")
    tv.heading("Créditos",  text="CRÉDITOS")
    tv.heading("C.H",  text="C.H")   
    tv.heading("Período", text="PERÍODO")
    tv.heading("Situação",text="SITUAÇÃO")
    tv.pack(pady=5)

    for materia in grade:
        values = materia.split(",")
        tv.insert("", "end", values=values)

    def select(event):
        curItem = tv.focus()
        print(tv.item(curItem)["values"])

    tv.bind("<<TreeviewSelect>>", select, "+")


splash_screen.after(2000, mainWindow)
mainloop()