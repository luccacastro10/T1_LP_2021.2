from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

splash_screen = Tk()
splash_screen.geometry("+500+250")
splash_screen.overrideredirect(True) #Desabilita o título da janela
splash_screen.wm_attributes("-transparentcolor", 'grey')

img = ImageTk.PhotoImage(Image.open("camera.ico"))
label = Label(image=img, bg="grey")
label.grid()


def mainWindow():
    splash_screen.destroy()
    menu = Tk()
    menu.title("Trabalho LP")
    menu.geometry("500x500+450+250")
    menu.minsize(200,200)
    menu.iconbitmap("camera.ico")

    nb = ttk.Notebook(menu)
    nb.place(x=0, y=0, width=500, height=500)

    aba1 = Frame(nb)
    nb.add(aba1, text="Aba 1")
    aba2 = Frame(nb)
    nb.add(aba2, text="Aba 2")
    aba3 = Frame(nb)
    nb.add(aba3, text="Aba 3")


splash_screen.after(2000, mainWindow)
mainloop()