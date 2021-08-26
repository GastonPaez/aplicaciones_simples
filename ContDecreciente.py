from tkinter import *

root = Tk()

root.title("ContDecreciente")

lb_cont = Label(root, text="Contador:")
lb_cont.grid(row=0, column=0)
lb_pantalla = Label(root, width=15, text="88")
lb_pantalla.grid(column=1, row=0)


def decreciente():
    valor = int(lb_pantalla["text"])
    restar_valor = valor - 1
    lb_pantalla["text"] = restar_valor


bt_menos = Button(root, text="-", command=decreciente)
bt_menos.grid(column=2, row=0)

root.mainloop()
