from tkinter import *

root = Tk()

root.title("Factorial")

lb_numero = Label(root, text="n")
lb_numero.grid(row=0, column=0)
entry_pantalla = Entry(
    root,
    width=5,
)
entry_pantalla.grid(column=1, row=0)
lb_factorial = Label(root, text="Factorial (n)")
lb_factorial.grid(row=0, column=2)

lb_resultado = Label(root, width=5)
lb_resultado.grid(row=0, column=3)


def factorizar():
    valor = int(entry_pantalla.get())
    contador = 1
    for x in range(valor):
        contador = contador * valor
        valor = valor - 1
    lb_resultado["text"] = contador


bt_siguiente = Button(root, text="Siguiente", command=factorizar)
bt_siguiente.grid(column=4, row=0)

root.mainloop()
