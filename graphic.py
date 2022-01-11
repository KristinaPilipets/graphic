from tkinter import*
from math import *
import matplotlib.pyplot as plt
import numpy as np

def test():
    global a,b,c
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        sutsav.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return flag,D,t

def graafik():
    flag,D,t=test()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    sutsav.configure(text=f"D={D}\n{t}\n{text}") 

def big(event):
    aken.geometry(str(aken.winfo_width()+14)+"x"+str(aken.winfo_height()+20))

def small(event):
    aken.geometry(str(aken.winfo_width()-14)+"x"+str(aken.winfo_height()-20))

aken=Tk()
aken.title("Квадратные уровнения")
aken.geometry("700x350")

lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue",justify=CENTER)
lbl.pack()
sutsav=Label(aken,text="Ответ",width=60,font="Calibri 26",fg="green",bg="yellow")
sutsav.pack(side=BOTTOM)

arg=Button(aken,text="Увеличить",font="Calibri 26",fg="black",bg="green",relief=GROOVE)
arg.pack(side=BOTTOM)
arg.bind("<Button-1>",big)

ar=Button(aken,text="Уменшить",font="Calibri 26",fg="black",bg="green",relief=GROOVE)
ar.pack(side=BOTTOM)
ar.bind("<Button-1>",small)

a=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
a.pack(side=LEFT)
x1=Label(aken,text="x**2+",font="Calibri 26",fg="green")
x1.pack(side=LEFT)
b=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
b.pack(side=LEFT)
x2=Label(aken,text="x+",font="Calibri 26",fg="green")
x2.pack(side=LEFT)
c=Entry(aken,width=3,font="Arial 20",fg="green",bg="lightblue")
c.pack(side=LEFT)
o=Label(aken,text="=0",font="Calibri 26",fg="green")
o.pack(side=LEFT)
 
vastus=Button(aken,text="Решить",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=test)#RAISED, SUNKEN
vastus.pack(side=RIGHT)

grafik=Button(aken,text="График",font="Calibri 26",fg="black",bg="green",relief=GROOVE,command=graafik)#RAISED, SUNKEN
grafik.pack(side=RIGHT)


aken.mainloop()