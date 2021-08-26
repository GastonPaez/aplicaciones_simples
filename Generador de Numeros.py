from tkinter import *
from random import randint

root = Tk()

label1 = Label(root, text="Numero 1")
label1.grid(row=0, column=0)
spin1 = Spinbox(root, from_=0, to=99)
spin1.grid(row=0, column=1)
label2 = Label(root, text="Numero 2")
label2.grid(row=1, column=0)
spin2 = Spinbox(root, from_=0, to=99)
spin2.grid(row=1, column=1)
label3 = Label(root, text="Numero Generado")
label3.grid(row=2, column=0)
entry3 = Entry(root)
entry3.grid(row=2, column=1)


def generar_numero():
    uno = int(spin1.get())
    dos = int(spin2.get())
    entry3.delete(0, "end")
    entry3.insert(0, str(randint(uno, dos)))


boton_generar = Button(root, text="Generar", command=generar_numero)
boton_generar.grid(row=3, column=1)

root.mainloop()
