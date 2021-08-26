from tkinter import *
from random import randint

root = Tk()

resultado = ""


def nuevo_juego():
    en_1.delete(0, "end")
    en2.delete(0, "end")
    en_1.insert(0, randint(0, 10))
    en2.insert(0, randint(0, 10))
    if seleccion.get() == 1:
        lbmenos["text"] = "+"
        resultado = int(en_1.get()) + int(en2.get())
    if seleccion.get() == 2:
        lbmenos["text"] = "-"
        resultado = int(en_1.get()) - int(en2.get())
    if seleccion.get() == 3:
        lbmenos["text"] = "*"
        resultado = int(en_1.get()) * int(en2.get())
    if seleccion.get() == 4:
        lbmenos["text"] = "/"
        resultado = int(en_1.get()) / int(en2.get())


def result():
    if seleccion.get() == 1:
        resultado = int(en_1.get()) + int(en2.get())
        if resultado == int(en_res.get()):
            print("si")
        else:
            print("no")
    if seleccion.get() == 2:
        resultado = int(en_1.get()) - int(en2.get())
        if resultado == int(en_res.get()):
            print("si")
        else:
            print("no")
    if seleccion.get() == 3:
        resultado = int(en_1.get()) * int(en2.get())
        if resultado == int(en_res.get()):
            print("si")
        else:
            print("no")
    if seleccion.get() == 4:
        resultado = int(en_1.get()) / int(en2.get())
        if resultado == float(en_res.get()):
            print("si")
        else:
            print("no")


en_1 = Entry(root)
en_1.grid(row=1)
lbmenos = Label(root, text="?")
lbmenos.grid(row=1, column=1)
en2 = Entry(root)
en2.grid(row=1, column=2)
bt_nuevon = Button(root, text="Nuevo Numero", command=nuevo_juego)
bt_nuevon.grid(row=1, column=3)
seleccion = IntVar()
rb_sum = Radiobutton(root, text="sumar", value=1, variable=seleccion)
rb_sum.grid(row=2)
rb_res = Radiobutton(root, text="restar", value=2, variable=seleccion)
rb_res.grid(row=3)
rb_mul = Radiobutton(root, text="multiplicar", value=3, variable=seleccion)
rb_mul.grid(row=4)
rb_div = Radiobutton(root, text="divir", value=4, variable=seleccion)
rb_div.grid(row=5)

en_res = Entry(root)
en_res.grid(row=3, column=2)
bt_res = Button(root, text="Resultado", command=result)
bt_res.grid(row=4, column=2)

lbjuegos = Label(root, text="Juegos:")
lbjuegos.grid(row=6, column=2)
lb2 = Label(root, text="")
lb2.grid(row=6, column=3)
lbbuenos = Label(root, text="Buenos:")
lbbuenos.grid(row=7, column=2)
lb1 = Label(root, text="")
lb1.grid(row=7, column=3)
lbmalos = Label(root, text="Malos:")
lbmalos.grid(row=8, column=2)
lb1 = Label(root, text="")
lb1.grid(row=8, column=3)


root.mainloop()
