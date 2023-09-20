# ----- Tkinter ----- #

from tkinter import *
from tkinter.ttk import *
from random import randint

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("720x480")
label = Label(master, text="Enter your name:")
label.pack(pady=10)

input = Entry(master, width=30)
input.focus_set()
input.pack(pady=10)

btn = Button(master, text ="Uppercase it !", command = lambda: upperit(input.get()))
btn.pack(pady = 10)

# canvas = Canvas(master, width = 500, height = 500)      
# canvas.pack()      
# img = PhotoImage(file="/home/lukimperinetti/Téléchargements/lotr.gif")      
# canvas.create_image(20,20, anchor=NW, image=img) 

# drawing :
canvas = Canvas(width = 4000, height = 3000, bg = "white")
canvas.pack(pady = 20)

canvas.create_oval(450, 5, 550, 100, fill = "lightgreen", width=3)
canvas.create_line(500, 120, 700, 200, fill = "blue", width=3)
canvas.create_line(300, 200, 500, 120, fill = "red", width=3)
canvas.create_line(500, 100, 500, 300, fill = "green", width=3)
canvas.create_line(300, 380, 500, 300, fill = "purple", width=3)
canvas.create_line(500, 300, 700, 380, fill = "orange", width=3)


def upperit(n):
    print(n.upper())

def dessiner(item=None):
    canvas.delete(item)
    a=randint(1,90)
    b=randint(1,50)
    c=50
    item=canvas.create_rectangle(a, b, a+c, b+c, fill='blue', outline='')
    canvas.after(1000, dessiner, item)

dessiner()

# mainloop, runs infinitely
mainloop()
