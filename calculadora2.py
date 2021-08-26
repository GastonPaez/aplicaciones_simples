from tkinter import *

root = Tk()
root.geometry("400x200")
frame_sep = Frame(root, height=30, width=20)
frame_sep.grid(row=1)

label_title = Label(root, text="Operaciones")
label_title.grid(row=2, column=2)

label_val1 = Label(root, text="Valor 1")
label_val1.grid(row=3, column=0)
label_val2 = Label(root, text="Valor 2")
label_val2.grid(row=4, column=0)
label_resultado = Label(root, text="Resultado")
label_resultado.grid(row=5, column=0)

entry1 = Entry(root)
entry1.grid(row=3, column=1)
entry2 = Entry(root)
entry2.grid(row=4, column=1)
entryres = Entry(root)
entryres.grid(row=5, column=1)


def calcular():
    if seleccion.get() == 1:
        valor1 = int(entry1.get())
        valor2 = int(entry2.get())
        entryres.delete(0, "end")
        entryres.insert(0, (valor1 + valor2))

    if seleccion.get() == 2:
        valor1 = int(entry1.get())
        valor2 = int(entry2.get())
        entryres.delete(0, "end")
        entryres.insert(0, (valor1 - valor2))

    if seleccion.get() == 3:
        valor1 = int(entry1.get())
        valor2 = int(entry2.get())
        entryres.delete(0, "end")
        entryres.insert(0, (valor1 * valor2))

    if seleccion.get() == 4:
        valor1 = int(entry1.get())
        valor2 = int(entry2.get())
        entryres.delete(0, "end")
        entryres.insert(0, (valor1 / valor2))


seleccion = IntVar()
radsum = Radiobutton(root, text="Sumar", variable=seleccion, value=1)
radsum.grid(row=3, column=2)
radres = Radiobutton(root, text="Restar", value=2, variable=seleccion)
radres.grid(row=4, column=2)
radmul = Radiobutton(root, text="Multiplicar", value=3, variable=seleccion)
radmul.grid(row=5, column=2)
raddiv = Radiobutton(root, text="Dividir", value=4, variable=seleccion)
raddiv.grid(row=6, column=2)

boton_calc = Button(root, text="Calcular", command=calcular)
boton_calc.grid(row=7)

root.mainloop()
