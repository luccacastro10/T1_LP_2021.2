from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk,Image
from matplotlib.pyplot import text
from ttkwidgets import CheckboxTreeview
from openpyxl import Workbook,load_workbook
import pathlib


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
    nb.place(x=0, y=0, width=750, height=750)

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
    selectedDisciplines = []
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

        selectedDisciplines = []
        notSelectedDisciplines = []
        currentTv = 0
        currentLabel = 0

        if status == "Disciplinas Cursadas":
            currentTv = takenTv
            currentLabel = takenNumberLabel
            for row in takenTv.get_children():
                takenTv.delete(row)
            nb.select(aba3)
        elif status == "Disciplinas em Curso":
            currentTv = inCourseTv
            currentLabel = inCourseNumberLabel
            for row in inCourseTv.get_children():
                inCourseTv.delete(row)
            nb.select(aba4)
        elif status == "Disciplinas Pendentes":
            currentTv = pendingTv
            currentLabel = PendingNumberLabel
            for row in pendingTv.get_children():
                pendingTv.delete(row)
            nb.select(aba5)

        checkedDisciplines = curriculumTv.get_checked()

        for i in curriculumTv.get_children():
            if i in checkedDisciplines:
                selectedDisciplines.append(curriculumTv.item(i))
            else:
                notSelectedDisciplines.append(curriculumTv.item(i))
            

        for i in selectedDisciplines:
            if status == "Disciplinas Cursadas":
                takenTv.insert("", "end", values=i["values"])
            elif status == "Disciplinas em Curso":
                inCourseTv.insert("", "end", values=i["values"])
            elif status == "Disciplinas Pendentes":
                pendingTv.insert("", "end", values=i["values"])

        for i in notSelectedDisciplines:
            if status == "Disciplinas Cursadas":
                pendingTv.insert("", "end", values=i["values"])
                updateDisciplineNumber("Disciplinas Pendentes", pendingTv, PendingNumberLabel)
            elif status == "Disciplinas Pendentes":
                takenTv.insert("", "end", values=i["values"])
                updateDisciplineNumber("Disciplinas Cursadas", takenTv, takenNumberLabel)


        updateDisciplineNumber(status, currentTv, currentLabel)

        
    def updateDisciplineNumber(status, tv, label):
        label["text"] = "Você possui " + str(len(tv.get_children())) + " " + status



    # Aba 2

    saveButton = Button(aba2, text ="Salvar Disciplinas Selecionadas", command = selecionarDisciplinas)
    saveButton.pack(pady=5)
    
    curriculumTv = CheckboxTreeview(aba2, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings", "tree"), height=15)
    curriculumTv.column("#0", width=45)
    curriculumTv.column("Código",  width=60, anchor=CENTER, stretch=NO)
    curriculumTv.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    curriculumTv.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    curriculumTv.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    curriculumTv.column("Período", width=60, anchor=CENTER, stretch=NO)
    curriculumTv.heading("Código",  text="CÓDIGO")
    curriculumTv.heading("Disciplina", text="DISCIPLINA")
    curriculumTv.heading("Créditos",  text="CRÉDITOS")
    curriculumTv.heading("C.H",  text="C.H")   
    curriculumTv.heading("Período", text="PERÍODO")
    curriculumTv.pack()


    # Aba 3

    takenLabel = Label(aba3, text="Disciplinas Cursadas", bd=2, font=25, borderwidth=2, relief="flat")
    takenLabel.pack(pady=10)

    takenTv = ttk.Treeview(aba3, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))
    takenTv.column("Código",  width=60, anchor=CENTER, stretch=NO)
    takenTv.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    takenTv.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    takenTv.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    takenTv.column("Período", width=60, anchor=CENTER, stretch=NO)
    takenTv.heading("Código",  text="CÓDIGO")
    takenTv.heading("Disciplina", text="DISCIPLINA")
    takenTv.heading("Créditos",  text="CRÉDITOS")
    takenTv.heading("C.H",  text="C.H")   
    takenTv.heading("Período", text="PERÍODO")
    takenTv.pack()

    takenNumberLabel = Label(aba3, text="Você possui " + str(len(takenTv.get_children())) + " Disciplinas em cursadas", bd=2, font=25, borderwidth=2, relief="flat")
    takenNumberLabel.pack(pady=10)



    # Funçoes: Aba 4
    
    # Função para criar uma planilha excel

    def CriandoArquivo_Excl():
        arquivo_excel = pathlib.Path("relatorio.xlsx")
        if arquivo_excel.exists ():
            pass
        else:
            arquivo_excel = Workbook()
            sheet = arquivo_excel.active

            dados = inCourseTv.get_checked()
            
            # Os nomes que estao indo pro arquivo sao do tipo 'I0001',
            # Ajeitar para os nomes corretos das disciplinas
            sheet.append(dados)

            arquivo_excel.save("relatorio.xlsx")

    # Função para adicionar dados a planilha

    def submitExcell ():
        try:
            entrada = entry.get()
            entry.delete(0, END)

            file = load_workbook("relatorio.xlsx")
            sheet = file.active

            dado = inCourseTv.get_checked()
            # Aqui sera marcado apenas uma das checkbox
            # O nome da checkbox marcada deve ser usado
            # Para selecionar a coluna a que se deseja adicionar a informação

            # Da forma que esta, ele apenas adiciona a primeira coluna por causa do column = 1
            sheet.cell(column = 1,row = sheet.max_row+1,value = entrada)

            file.save("relatorio.xlsx")   

            lblmsg['text'] = 'Informação Adicionada'
            lblmsg.pack()

        except:
            lblmsg['text'] = 'Não foi possivel Adicionar'
            lblmsg.pack()    

    # Aba 4

    label1_Btn = Button(aba4,text="Gerar Arquivo Excel", bd=2, font=25, borderwidth=2,command=CriandoArquivo_Excl)
    label1_Btn.pack()

    inCourseLabel = Label(aba4, text="Disciplinas Em Curso", bd=2, font=25, borderwidth=2, relief="flat")
    inCourseLabel.pack(pady=10)

    inCourseTv = CheckboxTreeview(aba4, columns=("Código", "Disciplina"), show=("headings","tree"))
    inCourseTv.column("#0", width=45)
    inCourseTv.column("Código",  width=60, anchor=CENTER, stretch=NO)
    inCourseTv.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    inCourseTv.heading("Código",  text="CÓDIGO")
    inCourseTv.heading("Disciplina", text="DISCIPLINA")
    inCourseTv.pack()

    inCourseNumberLabel = Label(aba4, text="Você possui " + str(len(inCourseTv.get_children())) + " Disciplinas em Curso", bd=2, font=25, borderwidth=2, relief="flat")
    inCourseNumberLabel.pack()

    lbl_code = Label(aba4,text="Codigo", bd=2, font=25, borderwidth=2, relief="flat")
    lbl_code.pack()
    entry_code = Entry(aba4,width=10)
    entry_code.pack()

    lbl_discipline = Label(aba4,text="Disciplina", bd=2, font=25, borderwidth=2, relief="flat")
    lbl_discipline.pack()
    entry_discipline = Entry(aba4,width=10)
    entry_discipline.pack() 

 
    lbl_cred = Label(aba4,text="CRED", bd=2, font=25, borderwidth=2, relief="flat")
    lbl_cred.pack()
    entry_cred = Entry(aba4,width=10)
    entry_cred.pack()
    

    lbl_ch = Label(aba4,text="CH", bd=2, font=25, borderwidth=2, relief="flat")
    lbl_ch.pack()
    entry_ch = Entry(aba4,width=10)
    entry_ch.pack() 
    
    lbl_period = Label(aba4,text="PERIODO", bd=2, font=25, borderwidth=2, relief="flat")
    lbl_period.pack()
    entry_period = Entry(aba4,width=10)
    entry_period.pack()

    label2_Btn = Button(aba4,text="Adicionar ao Arquivo", bd=2, font=25, borderwidth=2,command=submitExcell)
    label2_Btn.pack()



    # Aba 5

    pendingLabel = Label(aba5, text="Disciplinas Pendentes", bd=2, font=25, borderwidth=2, relief="flat")
    pendingLabel.pack(pady=10)

    pendingTv = ttk.Treeview(aba5, columns=("Código", "Disciplina", "Créditos", "C.H", "Período"), show=("headings"))
    pendingTv.column("Código",  width=60, anchor=CENTER, stretch=NO)
    pendingTv.column("Disciplina",  width=180, anchor=CENTER, stretch=NO)
    pendingTv.column("Créditos",  width=65, anchor=CENTER, stretch=NO)
    pendingTv.column("C.H",  width=40, anchor=CENTER, stretch=NO)
    pendingTv.column("Período", width=60, anchor=CENTER, stretch=NO)
    pendingTv.heading("Código",  text="CÓDIGO")
    pendingTv.heading("Disciplina", text="DISCIPLINA")
    pendingTv.heading("Créditos",  text="CRÉDITOS")
    pendingTv.heading("C.H",  text="C.H")   
    pendingTv.heading("Período", text="PERÍODO")
    pendingTv.pack()

    PendingNumberLabel = Label(aba5, text="Você possui " + str(len(pendingTv.get_children())) + " Disciplinas Pendentes", bd=2, font=25, borderwidth=2, relief="flat")
    PendingNumberLabel.pack(pady=10)


    for materia in grade:
        values = materia.split(",")
        curriculumTv.insert("", "end", values=values)

    



splash_screen.after(2000, mainWindow)
mainloop()
