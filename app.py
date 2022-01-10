from tkinter import *
from PIL import ImageTk,Image

splash_screen = Tk()
splash_screen.geometry("+500+250")
splash_screen.overrideredirect(True) #Desabilita o título da janela
splash_screen.wm_attributes("-transparentcolor", 'grey')

img = ImageTk.PhotoImage(Image.open("camera.ico"))
label = Label(image=img, bg="grey")

label.pack()

def mainWindow():
    splash_screen.destroy()
    menu = Tk()
    menu.title("Trabalho LP")
    menu.geometry("500x500+450+250")
    menu.minsize(200,200)
    menu.iconbitmap("camera.ico")

splash_screen.after(2000, mainWindow)

mainloop()