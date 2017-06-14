from tkinter import * # Importa el módulo
import turtle
import math
import random
import time
 
v0 = Tk() # Tk() Es la ventana principal
v0.title("Examen")

v1=Toplevel(v0) # Crea una ventana hija
var1 = IntVar()
var4 = IntVar()
def dibuja():
    n= var1
    t= turtle.Pen()
    n = input()
    n=int(n)
    radio = 100
    b=(2*radio*math.sin(math.pi/n))
    a = ((n-2)*180)/n
    c = (180 - a)  
    for x in range(0,n):
        t.forward(b)
        t.left(c)


def calculos () :
    resultado=0
    l=int(e1)
    b=int(e2)
    h=int(e3)
    d=e4.get()
    if l <=2:
        print ("lados deben ser valores marores a tres ")
    elif l==3:
        resultado = (b*h)/2
    elif l==4:
        resultado = (b*h)
    elif l==5:
        resultado = ((l*d)* a)/2
def perimetro():
    resultado=0
    l = var1
    d = var4
    if l <=2:
        print ("lados deben ser valores marores a tres ")
    elif l==3:
        resultado = l*d
    elif l==4:
        resultado = l*d
    elif l==5:
        resultado = l*d
    print (resultado)
def mostrar(ventana):
    ventana.deiconify() # Muestra una ventana
    Label(v1, text="Lados").grid(row=0)
    
    Label(v1, text="Base").grid(row=1)
    Label(v1, text="altura").grid(row=2)
    Label(v1, text="Tamaño lado").grid(row=3)
    Label(v1, text="Apotema").grid(row=4)
    e1 = Entry(v1)
    var1 = IntVar(e1)
    e2 = Entry(v1)
    e3 = Entry(v1)
    e4 = Entry(v1)
    var4 = IntVar(e4)
    e5 = Entry(v1)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    Button(v1, text='Perimetro', command = perimetro).grid(row=5,
    column=0, sticky=W, pady=4)
    Button(v1, text='Calcular Area',
    command=calculos).grid(row=5, column=1, sticky=W,
    pady=4)
    Button(v1, text='Graficar',
    command=dibuja).grid(row=5, column=2, sticky=W,
    pady=4)
    
def ocultar(ventana):
    

    class Ball:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_line(0, 10, 10, 0, width=1, fill='green')
            self.canvas.move(self.id, 245, 300)
 
        def draw(self):
            self.canvas.move(self.id, -1, 1)
 
    tk = Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    ball = Ball(canvas, 'red')
    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    
def ejecutar(f): v0.after(200,f) # Una forma alternativa de ejecutar una función
 
v0.config(bg="black") # Le da color al fondo
v0.geometry("640x480") # Cambia el tamaño de la ventana
 
b1=Button(v0,text="Perimetro,area,Grafico",command=lambda: ejecutar(mostrar(v1))) # Primer botón
b1.grid(row=1,column=1) # El botón es cargado
b2=Button(v0,text="Animacion",command=lambda: ejecutar(ocultar(v1))) # Segundo botón
b2.grid(row=1,column=2) # El botón es cargado


 
v1.withdraw() # Oculta la ventana v1
v0.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.

