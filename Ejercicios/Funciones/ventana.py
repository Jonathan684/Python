import tkinter as tk
vent = tk.Tk()

def inicio():
    global vent
    vent.title("Python")
    #AnchoxAlto
    vent.geometry('380x300')
    vent.configure(background='dark sea green')
    etiqueta1 = tk.Label(vent,text= "Palabras con 're' y finalizan con 'o':",bg='snow2',fg ='black').place(x=10,y=10)

def ver_txt(text):
    salida = tk.Entry(vent,justify=tk.CENTER)
    salida.place(x=220, y=10)
    salida.insert(0,text)
def mostrar():
    vent.mainloop()