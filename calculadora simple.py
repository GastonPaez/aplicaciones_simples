from tkinter import *

root = Tk()

root.title("Calculadora simple")


lb_primern = Label(root, text="Primer Numero")
lb_primern.grid(row=1, column=0)
en_pn = Entry(root)
en_pn.grid(row=1, column=1)

lb_segundon = Label(root, text="Segundo Numero")
lb_segundon.grid(column=0, row=2)
en_sn = Entry(root)
en_sn.grid(row=2, column=1)


lb_res = Label(root, text="Resultado")
lb_res.grid(column=0, row=3)
lbr_res = Label(root, bg="gainsboro", width=16)
lbr_res.grid(row=3, column=1)


def sumar():
    valor1 = int(en_pn.get())
    valor2 = int(en_sn.get())
    resultado = valor1 + valor2
    lbr_res["text"] = resultado


def restar():
    valor1 = int(en_pn.get())
    valor2 = int(en_sn.get())
    resultado = valor1 - valor2
    lbr_res["text"] = resultado


def multiplicar():
    valor1 = int(en_pn.get())
    valor2 = int(en_sn.get())
    resultado = valor1 * valor2
    lbr_res["text"] = resultado


def dividir():
    valor1 = int(en_pn.get())
    valor2 = int(en_sn.get())
    resultado = valor1 / valor2
    lbr_res["text"] = resultado


def el_resto_division():
    valor1 = int(en_pn.get())
    valor2 = int(en_sn.get())
    resultado = valor1 % valor2
    lbr_res["text"] = resultado


def borrar():
    lbr_res["text"] = ""


bt_mas = Button(root, text="+", width=15, command=sumar)
bt_mas.grid(row=4, column=0)
bt_menos = Button(root, text="-", width=15, command=restar)
bt_menos.grid(row=4, column=1)
bt_multiplicar = Button(root, text="x", width=15, command=multiplicar)
bt_multiplicar.grid(row=5, column=0)
bt_dividir = Button(root, text="÷", width=15, command=dividir)
bt_dividir.grid(row=5, column=1)
bt_porciento = Button(root, text="%", width=15, command=el_resto_division)
bt_porciento.grid(row=6, column=0)
bt_clear = Button(root, text="CLEAR", width=15, command=borrar)
bt_clear.grid(row=6, column=1)


root.mainloop()
