from tkinter import *

root = Tk()
i = 0


def poner_numeros(n):
    global i
    casillero_res.insert(i, n)
    i += 1


def poner_operador(operador):
    global i
    longitud = len(operador)
    casillero_res.insert(i, operador)
    i += longitud


def borrar_todo():
    casillero_res.delete(0, "end")


casillero_res = Entry(root, width=35)
casillero_res.grid(columnspan=6, row=0)
bt_backspace = Button(root, text="Backspace", width=11)
bt_clear = Button(root, text="Clear", width=11)
bt_clear_all = Button(root, text="Clear All", width=11, command=borrar_todo)
bt_backspace.grid(columnspan=2, row=1, column=0)
bt_clear.grid(column=2, columnspan=2, row=1)
bt_clear_all.grid(columnspan=2, column=4, row=1)

# Botones Memoria
bt_mc = Button(root, text="MC", width=5)
bt_mr = Button(root, text="MR", width=5)
bt_ms = Button(root, text="MS", width=5)
bt_mmas = Button(root, text="M+", width=5)
bt_mc.grid(row=2, column=0)
bt_mr.grid(row=3, column=0)
bt_ms.grid(row=4, column=0)
bt_mmas.grid(row=5, column=0)
# Botones Numerico
bt_7 = Button(root, text="7", width=5, command=lambda: (poner_numeros(7)))
bt_1 = Button(root, text="1", width=5, command=lambda: (poner_numeros(1)))
bt_0 = Button(root, text="0", width=5, command=lambda: (poner_numeros(0)))
bt_4 = Button(root, text="4", width=5, command=lambda: (poner_numeros(4)))
bt_7.grid(row=2, column=1)
bt_4.grid(row=3, column=1)
bt_1.grid(row=4, column=1)
bt_0.grid(row=5, column=1)
bt_8 = Button(root, text="8", width=5, command=lambda: (poner_numeros(8)))
bt_5 = Button(root, text="5", width=5, command=lambda: (poner_numeros(5)))
bt_2 = Button(root, text="2", width=5, command=lambda: (poner_numeros(2)))
bt_decimal = Button(root, text=".", width=5)
bt_8.grid(row=2, column=2)
bt_5.grid(row=3, column=2)
bt_2.grid(row=4, column=2)
bt_decimal.grid(row=5, column=2)
bt_9 = Button(root, text="9", width=5, command=lambda: (poner_numeros(9)))
bt_6 = Button(root, text="6", width=5, command=lambda: (poner_numeros(6)))
bt_3 = Button(root, text="3", width=5, command=lambda: (poner_numeros(3)))
bt_masmenos = Button(root, text="+-", width=5)
bt_9.grid(row=2, column=3)
bt_6.grid(row=3, column=3)
bt_3.grid(row=4, column=3)
bt_masmenos.grid(row=5, column=3)
# Botones Operadores
bt_dividido = Button(root, text="÷", width=5, command=lambda: (poner_operador("÷")))
bt_por = Button(root, text="x", width=5, command=lambda: (poner_operador("*")))
bt_menos = Button(root, text="-", width=5, command=lambda: (poner_operador("-")))
bt_mas = Button(root, text="+", width=5, command=lambda: (poner_operador("+")))
bt_dividido.grid(row=2, column=4)
bt_por.grid(row=3, column=4)
bt_menos.grid(row=4, column=4)
bt_mas.grid(row=5, column=4)
# Botones Funciones
bt_sqrt = Button(root, text="Sqrt", width=5)
bt_elevacion = Button(root, text="x^2", width=5)
bt_lsobreequis = Button(root, text="l/x", width=5)
bt_igual = Button(root, text="=", width=5)
bt_sqrt.grid(row=2, column=5)
bt_elevacion.grid(row=3, column=5)
bt_lsobreequis.grid(row=4, column=5)
bt_igual.grid(row=5, column=5)


root.mainloop()
