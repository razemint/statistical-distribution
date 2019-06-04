from tkinter import *
import os;

#buttomSimpPress = Soluciona el problema

def buttonSimpPress():
  simpCommand = '\"\"inicio.py"\"'
  os.system(simpCommand)

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

#button_simp = Boton para resolver

button_simp=Button(simpFrame, text="Resolver", command=buttonSimpPress)
button_simp.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 15))
button_simp.grid(row=1, column=0, pady=10)

#----------------Simpson 1/3------------------

border.mainloop()