from tkinter import *

root = Tk()
root.geometry("350x200")

tit_pelicula = Label(root, text="Escribe el titulo de una Pelicula")
tit_pelicula.grid(row=0, column=0)

frame_mid = Frame(root, width=25)
frame_mid.grid(rowspan=3, row=0, column=1)

view_pelicula = Label(root, text="Peliculas")
view_pelicula.grid(row=0, column=2)

ent_pelicula = Entry(root)
ent_pelicula.grid(row=2, column=0)

lista_box = Listbox(root)
lista_box.grid(row=1, rowspan=5, column=2)
lista_pelis = []


def agregar_pelicula():
    lista_pelis.append(ent_pelicula.get())
    print(lista_pelis)
    contador = 0
    lista_box.delete("0", "end")
    for x in lista_pelis:
        lista_box.insert(contador, x)
        contador += 1


bt_agregar = Button(root, text="Añadir", command=agregar_pelicula).grid(row=3, column=0)

root.mainloop()
