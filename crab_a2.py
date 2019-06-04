from tkinter import *

#border = El borde de la pantalla, orillas y todo

border = Tk()
border.title("Distribucion de probabilidad")
border.resizable(0, 0)
border.geometry("800x650")
border.iconbitmap("sources/bordericon_a.ico")
border.config(bg="#3F3F3F")

#variables

box_text_x_num = StringVar()
box_text_y_num = StringVar()

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

#box_text_x = Caja uno

box_text_x = Entry(crabFrame, textvariable = box_text_x_num)
box_text_x.grid(row=0, column=1)

box_text_x_label = Label(crabFrame, text="crab that goes in X:")
box_text_x_label.grid(row=0, column=0, pady=10)
box_text_x_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#box_text_y = Caja dos

box_text_y = Entry(crabFrame, textvariable = box_text_y_num)
box_text_y.grid(row=1, column=1)

box_text_y_label = Label(crabFrame, text="crab that goes in Y:")
box_text_y_label.grid(row=1, column=0, pady=10)
box_text_y_label.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 10))

#def get_x = Para guardar X

def box_text_x_get():
    box_text_x_num.get()

#def get_y = Para guardar Y

def box_text_y_get():
    box_text_y_num.get()

#button_end = Boton para resolver

button_end=Button(mainFrame, text="Resolver", command=(box_text_x_get, box_text_y_get))
button_end.config(fg="#FFFFFF", bg="#4c4c4c", font=("Verdana", 15))

border.mainloop()