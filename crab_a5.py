from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

#variables

box_text_simp_int_inf_num = DoubleVar()
box_text_simp_int_sup_num = DoubleVar()
box_text_simp_init_num = IntVar()
box_text_simp_func_num = StringVar()

#buttomSimpPress = Soluciona el problema

def buttonSimpPress():

    a = box_text_simp_int_inf_num.get()
    b = box_text_simp_int_sup_num.get()
    n = box_text_simp_init_num.get()
    f = box_text_simp_func_num.get()

    console = "******************\n" + "Intervalo Inferior: " + str(a) + "\n" + "Intervalo Superior: " + str(b) + "\n" + "Numero de Iteraciones: " + str(n) + "\n" + "Funcion: " + str(f) + "\n******************"

    h = (b - a) / n

    suma = 0.0

    for i in range(1, n):
        x = a + i * h

        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        else:
            suma = suma + 4 * fx(x, f)

    suma = suma + fx(a, f) + fx(b, f)
    rest = suma * (h / 3)

    return (rest)

    print(console, rest)

def fx(x, f):
    return eval(f)

#border = El borde de la pantalla, orillas y todo

border = Tk()
border.title("Distribucion de probabilidad")
border.resizable(0, 0)
border.geometry("800x650")
border.iconbitmap("sources/bordericon_a.ico")
border.config(bg="#3F3F3F")

#mainFrame = La ventana principal

mainFrame = Frame(border)
mainFrame.config(bg="#4c4c4c")
mainFrame.config(width="790", height="645")
mainFrame.pack()

#mainFrameImg = PhotoImage(file = "sources/mainframeimg.png")

#mainLabel = Titulo FES

mainLabel = Label(mainFrame, text="Facultad de Estudios Superiores\nAragón")
mainLabel.place(x=212, y=250)
mainLabel.config(fg="#FFFFFF", bg="#3F3F3F", font=("Verdana", 20))
mainLabel.pack()

#crabFrame = Para los cuadros de texto

crabFrame = Frame(mainFrame)
crabFrame.config(bg="#4c4c4c")
crabFrame.pack()

#simpFrame = Para los cuadros de texto

simpFrame = Frame(crabFrame)
simpFrame.config(bg="#4c4c4c")
simpFrame.pack()

#----------------Simpson 1/3------------------

#box_text_simp_label = "Metodo Simpson 1/3"

box_text_simp_label = Label(simpFrame, text="Metodo Simpson 1/3")
box_text_simp_label.grid(row=0, column=0)
box_text_simp_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 18))

#box_text_simp_int_inf = Caja uno

box_text_simp_int_inf = Entry(simpFrame, textvariable = box_text_simp_int_inf_num)
box_text_simp_int_inf.grid(row=1, column=1)

box_text_simp_int_inf_label = Label(simpFrame, text="Intervalo Inferior:")
box_text_simp_int_inf_label.grid(row=1, column=0, pady=10)
box_text_simp_int_inf_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#box_text_simp_int_sup = Caja dos

box_text_simp_int_sup = Entry(simpFrame, textvariable = box_text_simp_int_sup_num)
box_text_simp_int_sup.grid(row=2, column=1)

box_text_simp_int_sup_label = Label(simpFrame, text="Intervalo Superior:")
box_text_simp_int_sup_label.grid(row=2, column=0, pady=10)
box_text_simp_int_sup_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#box_text_simp_init = Caja tres

box_text_simp_init = Entry(simpFrame, textvariable = box_text_simp_init_num)
box_text_simp_init.grid(row=3, column=1)

box_text_simp_init_label = Label(simpFrame, text="Iteraciones:")
box_text_simp_init_label.grid(row=3, column=0, pady=10)
box_text_simp_init_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#box_text_simp_func = Caja cuatro

box_text_simp_func = Entry(simpFrame, textvariable = box_text_simp_func_num)
box_text_simp_func.grid(row=4, column=1)

box_text_simp_func_label = Label(simpFrame, text="Funcion:")
box_text_simp_func_label.grid(row=4, column=0, pady=10)
box_text_simp_func_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#button_simp = Boton para resolver

button_simp=Button(simpFrame, text="Resolver", command=buttonSimpPress)
button_simp.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 15))
button_simp.grid(row=5, column=0, pady=10)

#box_text_simp_ans = Caja seis

box_text_simp_ans_label = Label(simpFrame, text="Resultado de la integral:")
box_text_simp_ans_label.grid(row=6, column=0, pady=10)
box_text_simp_ans_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

box_text_simp_ans = Entry(simpFrame, text="")
box_text_simp_ans.grid(row=6, column=1)

#----------------Simpson 1/3------------------

border.mainloop()