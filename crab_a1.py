from tkinter import *

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

mainFrameImg = PhotoImage(file = "sources/mainframeimg.png")

#mainLabel = Titulo FES

mainLabel = Label (mainFrame, text="Facultad de Estudios Superiores\nAragon", justify="center")
mainLabel.place(x=212, y=30)
mainLabel.place(bordermode="inside")
mainLabel.config(fg="#FFFFFF")
mainLabel.config(bg="#4c4c4c")
mainLabel.config(font=("Verdana", 18))


border.mainloop()