from distutils import command
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk,Image
from matplotlib.pyplot import text
from numpy import take
from ttkwidgets import CheckboxTreeview
from openpyxl import Workbook,load_workbook
import pathlib
import classes.disciplina as disciplina
from datetime import datetime
from classes.TableView import TableView
import matplotlib.pyplot as pyplot
from openpyxl.utils import get_column_letter

print("Opening aplication")

status = "Disciplinas Cursadas"
_finisehPeriods = 0

splash_screen = Tk()
splash_screen.geometry("+400+250")
splash_screen.overrideredirect(True) #Desabilita o título da janela
splash_screen.wm_attributes("-transparentcolor", 'grey')

img = ImageTk.PhotoImage(Image.open("data/UFRJ.png"))
label = Label(image=img, bg="grey")
label.grid()


def mainWindow():
    splash_screen.destroy()
    menu = Tk()
    menu.title("Minerva Course Analytics")
    menu.geometry("600x650+400+50")
    menu.resizable(False,False)
    menu.iconbitmap("data/UFRJ.ico")

    nb = ttk.Notebook(menu)
    nb.place(x=0, y=0, width=600, height=650)

    aba1 = Frame(nb)
    nb.add(aba1, text="Grade Curricular")
    aba2 = Frame(nb)
    nb.add(aba2, text="Disciplinas Cursadas")
    # aba3 = Frame(nb)
    # nb.add(aba3, text="Disciplinas em Curso")
    aba4 = Frame(nb)
    nb.add(aba4, text="Disciplinas Pendentes")
    aba5 = Frame(nb)
    nb.add(aba5, text="Periodização")

    pendingDisciplinesTv = TableView(aba5, False)

    currentYear = int(datetime.now().strftime('%Y'))
    initialYear = 2017
    periods = []
    for i in range(currentYear-initialYear):
        oddPeriod = str(initialYear) + ".1"
        evenPeriod = str(initialYear) + ".2"
        periods.append(oddPeriod)
        periods.append(evenPeriod)
        initialYear += 1

    selectPeriodLabel = Label(aba5, text="Selecione seu período de entrada na faculdade", borderwidth=2, relief="groove")
    selectPeriodLabel.pack( pady=5, padx=5)

    def updatePeriod(finisehPeriods):
        initialPeriod = selectPeriodSpinBox.get()
        currentMonth = int(datetime.now().strftime('%m'))
        if currentMonth < 7:
            currentPeriod = str(currentYear) + ".1"
        else:
            currentPeriod = str(currentYear) + ".2"

        if (initialPeriod.split(".")[1] == currentPeriod.split(".")[1]):
            finisehPeriods = 2*(int(currentPeriod.split(".")[0]) - int(initialPeriod.split(".")[0]))
        else:
            if (initialPeriod.split(".")[1] == "1"):
                finisehPeriods = 2*(int(currentPeriod.split(".")[0]) - int(initialPeriod.split(".")[0])) + 1
            else:
                finisehPeriods = 2*(int(currentPeriod.split(".")[0]) - int(initialPeriod.split(".")[0])) - 1

        selectPeriodLabel["text"] = "Seu período previsto para o presente momento é " + str(finisehPeriods + 1) +"°"

        generateCourseStatistics(finisehPeriods)

    def generateCourseStatistics(finisehPeriods):
        plannedDisciplines = []
        takenDisciplines = []

        for i in takenTv.get_children():
            takenDisciplines.append(takenTv.item(i)["values"])

        for i in curriculumTv.get_children():
            if (int(curriculumTv.item(i)["values"][4]) <= finisehPeriods):
                plannedDisciplines.append(curriculumTv.item(i)["values"])

        pendingDisciplinesList = [item for item in plannedDisciplines if item not in takenDisciplines]
        pendingDisciplinesNumber = len(pendingDisciplinesList)

        if (len(takenTv.get_children()) == 0):
            infoPeriodLabel["text"] = "Para obter informações sobre sua periodização ideal,\n preencha a tabela de disciplinas cursadas na aba Grade Curricular"
        else:
            if (len(pendingDisciplinesList) > 0):
                infoPeriodLabel["text"] =  "Voce está atrasado em " + str(pendingDisciplinesNumber) + " matérias" 
            else:
                infoPeriodLabel["text"] =  "Voce está de acordo com sua periodização ideal"
        
        pendingDisciplinesTv.clear()
        pendingDisciplinesTv.setTableView()
        pendingDisciplinesTv.pack( pady=5, padx=5)

        for i in pendingDisciplinesList:
            pendingDisciplinesTv.insert("", "end", values=i)


    selectPeriodSpinBox = Spinbox(aba5, values=periods, width=30, command= lambda:updatePeriod(_finisehPeriods))
    selectPeriodSpinBox.pack( pady=5, padx=5)

    selectPeriodLabel = Label(aba5, text="", font=25)
    selectPeriodLabel.pack( pady=5, padx=5)

    infoPeriodLabel = Label(aba5, text="", font=25)
    infoPeriodLabel.pack( pady=5, padx=5)

    f = open("data/grade.txt", encoding="utf8")
    selectedDisciplines = []
    grade = f.readlines()

    gradeLabel = Label(aba1, text="Grade Curricular: Engenharia de Controle e Automação", bd=2, font=25, borderwidth=2, relief="flat")
    gradeLabel.pack(pady=10)
    
    def value_changed():
        status = mySpin.get()
        selectLabel["text"] = ("Selecione as " + status)

    mySpin = Spinbox(aba1, values=("Disciplinas Cursadas", "Disciplinas Pendentes"), width=50, relief="groove", command=value_changed)
    mySpin.pack( padx=5)

    selectLabel = Label(aba1, text= ("Selecione as " + status), bd=2, font=25, borderwidth=2, relief="flat")
    selectLabel.pack()

    def selecionarDisciplinas():
        status = mySpin.get()

        selectedDisciplines = []
        notSelectedDisciplines = []
        currentTv = 0
        currentLabel = 0

        if status == "Disciplinas Cursadas" or status == "Disciplinas Pendentes" :
            for row in takenTv.get_children():
                takenTv.delete(row)
            for row in pendingTv.get_children():
                pendingTv.delete(row)
            if status == "Disciplinas Cursadas":
                currentTv = takenTv
                currentLabel = takenNumberLabel
                nb.select(aba2)
            else:
                currentTv = pendingTv
                currentLabel = PendingNumberLabel
                nb.select(aba4)
        # elif status == "Disciplinas em Curso":
        #     currentTv = inCourseTv
        #     currentLabel = inCourseNumberLabel
        #     for row in inCourseTv.get_children():
        #         inCourseTv.delete(row)
        #     nb.select(aba3)

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
        ch = 0
        cred = 0
        for i in tv.get_children():
            ch += int(tv.item(i)["values"][3])
            cred += float(tv.item(i)["values"][2])

        label["text"] = "Você possui " + str(len(tv.get_children())) + " " + status
        label["text"] += "\n\n A carga horária totaliza "+str(ch) +" horas"
        label["text"] += "\n\n Total de créditos: " + str(cred)


    # Aba 2    -----------------------------------------------------------------------------------------------------------------
     

    saveButton = Button(aba1, text ="Salvar Disciplinas Selecionadas", command = selecionarDisciplinas)
    saveButton.pack(pady=5)
    

    curriculumTv = TableView(aba1, True)
    curriculumTv.setTableView()
    curriculumTv["height"] = 20
    curriculumTv.pack()


    # Aba 3 -----------------------------------------------------------------------------------------------------------------

    takenLabel = Label(aba2, text="Disciplinas Cursadas", bd=2, font=25, borderwidth=2, relief="flat")
    takenLabel.pack(pady=10)

    takenTv = TableView(aba2, False)
    takenTv.setTableView()
    takenTv.pack()

    takenNumberLabel = Label(aba2, text="Você possui " + str(len(takenTv.get_children())) + " Disciplinas em cursadas", bd=2, font=25, borderwidth=2, relief="flat")
    takenNumberLabel.pack(pady=10)
   # Aba 5 -----------------------------------------------------------------------------------------------------------------

    pendingLabel = Label(aba4, text="Disciplinas Pendentes", bd=2, font=25, borderwidth=2, relief="flat")
    pendingLabel.pack(pady=10)

    pendingTv = TableView(aba4, False)
    pendingTv.setTableView()
    pendingTv.pack()


    PendingNumberLabel = Label(aba4, text="Você possui " + str(len(pendingTv.get_children())) + " Disciplinas Pendentes", bd=2, font=25, borderwidth=2, relief="flat")
    PendingNumberLabel.pack(pady=10)


    for materia in grade:
        values = materia.split(",")
        curriculumTv.insert("", "end", values=values)

    def generateGraphics():
        taken = len(takenTv.get_children())
        pending = len(curriculumTv.get_children()) - taken
        pyplot.axis("equal")
        pyplot.pie((taken, pending), labels=("Concluídas", "Pendentes"), autopct='%1.1f%%')
        pyplot.legend(("Concluídas", "Pendentes"), loc=3)
        pyplot.title("Percentual de conclusão de curso")
        pyplot.show()

    GraphicButton = Button(aba5, text="Gerar estatística de conclusão do curso", bd=2, font=25, borderwidth=2, relief="groove", command=generateGraphics)
    GraphicButton.pack( pady=5, padx=5)



splash_screen.after(3000, mainWindow)

mainloop()
print("Closing aplication")