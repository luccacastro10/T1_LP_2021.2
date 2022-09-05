from textwrap import fill
import tkinter as tk
from tkinter import Canvas
from tkinter import *
from turtle import width
from PIL import ImageTk,Image

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


app = tk.Tk()
app.title("Canvas")
app.geometry("1000x750+400+250")
app.bind('<Motion>', motion)

canvas = Canvas(app)
image = Image.open("data/grade-eca.jpg")
photo = ImageTk.PhotoImage(image.resize((1000, 750), Image.Resampling.LANCZOS))
canvas.create_image(0,0, image=photo, anchor='nw')

canvas.pack(fill='both', expand=1)

w=75
h=60

flux = open("data/fluxograma.txt")
bboxes = flux.readlines()

for bbox in bboxes:
   cod = bbox.split(",")[0]
   x = int(bbox.split(", ")[1])
   y = int(bbox.split(", ")[2])

   canvas.create_rectangle(x, y, x+w, y+h, outline='green', width=6 )

app.mainloop()