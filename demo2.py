#add widgets to create a user interface application program

from tkinter import *
window = Tk()
window.geometry("500x500+10+20")

window.title("Bading")

#adding a label
lbl = Label(window, text = "Ur name?", fg = "Red")
lbl.place(x=80, y=60)

#adding a button widget
btn = Button(window,text = "Submit", bg = "Gray")
btn.place(x=80, y=120)

#Text Field
txtfld = Entry(window, text = "entry", bd = 5)
txtfld.place(x=80, y=90)

def sel():
    selection = "You selected option " + str(var.get())
    label.config(text = selection)

var = IntVar()
r1 = Radiobutton(window, text="Male", variable=var, value = 1, command = sel)
r1.pack(anchor = W)
r1 = Radiobutton(window, text="Female", variable=var, value = 2, command = sel)
r1.pack(anchor = W)

label = Label(window)
label.pack()
window.mainloop()
