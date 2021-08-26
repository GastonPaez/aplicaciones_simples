from tkinter import *

root = Tk()

root.title("Contador mas menos")

frame_ventana = Frame(root, bg="DodgerBlue4", padx=30, pady=20)
frame_ventana.pack()

lb_contador = Label(frame_ventana, text="Contador", padx=4, bg="CadetBlue3")
lb_contador.grid(row=0, column=0)
lb_pantalla = Label(frame_ventana, width=10, bg="CadetBlue1", text="0")
lb_pantalla.grid(column=1, row=0)


def contUp():
    valor = int(lb_pantalla["text"])
    valor_up = valor + 1
    lb_pantalla["text"] = valor_up


def countDown():
    valor = int(lb_pantalla["text"])
    valor_up = valor - 1
    lb_pantalla["text"] = valor_up


def reset_val():
    lb_pantalla["text"] = 0


bt_countup = Button(frame_ventana, text="CountUp", padx=4, command=contUp)
bt_countup.grid(column=2, row=0)
bt_countdown = Button(frame_ventana, text="CountDown", padx=4, command=countDown)
bt_countdown.grid(column=3, row=0)
bt_reset = Button(frame_ventana, text="Reset", command=reset_val)
bt_reset.grid(column=4, row=0)


root.mainloop()
