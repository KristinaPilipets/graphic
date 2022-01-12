from tkinter import*
from math import *
import matplotlib.pyplot as plt
import numpy as np

def test():
    global a,b,c
    flag=""
    D=0
    t=0
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
t=0
def big(event):
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width()+200)+"x"+str(aken.winfo_height()+150))
        arg.configure(text="уменьшить",font="Calibri 26",fg="black",bg="green",relief=GROOVE)
        t=1
    else:
        arg.configure(text="Увеличить",font="Calibri 26",fg="black",bg="green",relief=GROOVE)
        aken.geometry(str(aken.winfo_width()-100)+"x"+str(aken.winfo_height()-200))
        t=0

def whale():
    y=[]
    x=list(range(0,9+1))
    for i in x:
        y_=2/27*i**2-3
        y.append(y_)
    plt.plot(x,y)

    x=np.linspace(-10,0,100)
    y=0.04*x**2-3
    plt.plot(x,y)
    x=np.linspace(-9,-3,100)
    y=2/9*(x+6)**2+1
    plt.plot(x,y)
    x=np.linspace(-3,9,100)
    y=-1/12*(x-3)**2+6
    plt.plot(x,y)
    x = np.linspace(5,8.6,80)
    y = 1/9*(x-5)**2+2
    plt.plot(x,y)
    x = np.linspace(5,7.8,100)
    y = 1/8*(x-7)**2+1.5
    plt.plot(x,y)
    x = np.linspace(-13,-9,100)
    y = -0.75*(x+11)**2+6
    plt.plot(x,y)
    x = np.linspace(-15,-13,100)
    y = -0.5*(x+13)**2+3
    plt.plot(x,y)
    x = [-15,-14,-13,-12,-11,-10]
    y = [1,1,1,1,1,1]
    plt.plot(x,y)

    x10=np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    plt.plot(x10,y10)
    plt.title("Ruutvõrrand Whale")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()
    
def glasses():

    x = np.linspace(-9,-1,100)
    y = -1/16*(x+5)**2+2
    plt.plot(x,y)
    x = np.linspace(1,9,100)
    y = -1/16*(x-5)**2+2
    plt.plot(x,y)
    x = np.linspace(-9,-1,100)
    y = 1/4*(x+5)**2-3
    plt.plot(x,y)
    x = np.linspace(1,9,100)
    y = 1/4*(x-5)**2-3
    plt.plot(x,y)
    x = np.linspace(-9,-6,100)
    y = -1*(x+7)**2+5
    plt.plot(x,y)
    x = np.linspace(6,9,100)
    y = -1*(x-7)**2+5
    plt.plot(x,y)
    x = np.linspace(-1,1,100)
    y = -0.5*x**2+1.5
    plt.plot(x,y)

    plt.title("Ruutvõrrand Glasses")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

def umbrella():

    x = np.linspace(-12,12,100)
    y = -1/18*x**2+12
    plt.plot(x,y,color="r")
    x = np.linspace(-4,4,100)
    y = -1/8*x**2+6
    plt.plot(x,y,color="b")
    x = np.linspace(-12,-4,100)
    y = -1/8*(x+8)**2+6
    plt.plot(x,y,color="g")
    x = np.linspace(4,12,100)
    y = -1/8*(x-8)**2+6
    plt.plot(x,y,color="c")
    x = np.linspace(-4,-0.3,100)
    y = 2*(x+3)**2-9
    plt.plot(x,y,color="m")
    x = np.linspace(-4.5,0.2,100)
    y = 1.5*(x+3)**2-10
    plt.plot(x,y,color="k")

    plt.title("Ruutvõrrand Umbrella")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

def buterfly():

    x = np.linspace(-9,-1,100)
    y = -1/8*(x+9)**2+8
    plt.plot(x,y)
    x = np.linspace(1,9,100)
    y = -1/8*(x-9)**2+8
    plt.plot(x,y)
    x = np.linspace(-9,-8,100)
    y = 7*(x+8)**2+1
    plt.plot(x,y)
    x = np.linspace(8,9,100)
    y = 7*(x-8)**2+1
    plt.plot(x,y)
    x = np.linspace(-8,-1,100)
    y = 1/49*(x+1)**2
    plt.plot(x,y)
    x = np.linspace(1,8,100)
    y = 1/49*(x-1)**2
    plt.plot(x,y)

    x = np.linspace(-8,-1,100)
    y = -4/49*(x+1)**2
    plt.plot(x,y)
    x = np.linspace(1,8,100)
    y = -4/49*(x-1)**2
    plt.plot(x,y)
    x = np.linspace(-8,-2,100)
    y = 1/3*(x+5)**2-7
    plt.plot(x,y)
    x = np.linspace(2,8,100)
    y = 1/3*(x-5)**2-7
    plt.plot(x,y)
    x = np.linspace(-2,-1,100)
    y = -2*(x+1)**2-2
    plt.plot(x,y)
    x = np.linspace(1,2,100)
    y = -2*(x-1)**2-2
    plt.plot(x,y)
    x = np.linspace(-1,1,100)
    y = -4*x**2+2
    plt.plot(x,y)
    x = np.linspace(-1,1,100)
    y = 4*x**2-6
    plt.plot(x,y)
    x = np.linspace(-2,0,100)
    y = -1.5*x+2
    plt.plot(x,y)
    x = np.linspace(0,2,100)
    y = 1.5*x+2
    plt.plot(x,y)

    plt.title("Ruutvõrrand Buterfly")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

def frog():

    x = np.linspace(-7,7,100)
    y = -3/49*x**2+8
    plt.plot(x,y)
    x = np.linspace(-7,7,100)
    y = 4/49*x**2+1
    plt.plot(x,y)
    x = np.linspace(-6.8,-2,100)
    y = -0.75*(x+4)**2+11
    plt.plot(x,y)
    x = np.linspace(2,6.8,100)
    y = -0.75*(x-4)**2+11
    plt.plot(x,y)
    x = np.linspace(-5.8,-2.8,100)
    y = -1*(x+4)**2+9
    plt.plot(x,y)
    x = np.linspace(2.8,5.8,100)
    y = -1*(x-4)**2+9
    plt.plot(x,y)
    x = np.linspace(-4,4,100)
    y = 4/9*x**2-5
    plt.plot(x,y)
    x = np.linspace(-5.2,5.2,100)
    y = 4/9*x**2-9
    plt.plot(x,y)

    x = np.linspace(-7,-2.8,100)
    y = -1/16*(x+3)**2-6
    plt.plot(x,y)
    x = np.linspace(2.8,7,100)
    y = -1/16*(x-3)**2-6
    plt.plot(x,y)
    x = np.linspace(-7,0,100)
    y = 1/9*(x+4)**2-11
    plt.plot(x,y)
    x = np.linspace(0,7,100)
    y = 1/9*(x-4)**2-11
    plt.plot(x,y)
    x = np.linspace(-7,-4.5,100)
    y = -1*(x+5)**2
    plt.plot(x,y)
    x = np.linspace(4.5,7,100)
    y = -1*(x-5)**2
    plt.plot(x,y)
    x = np.linspace(-3,3,100)
    y = 2/9*x**2+2
    plt.plot(x,y)


    plt.title("Ruutvõrrand frog")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

aken=Tk()
aken.title("Квадратные уровнения")
aken.geometry("650x200")
f1=Frame(aken,width=650,height=260)
f2=Frame(aken,width=650,height=260)
f1.pack(side=TOP)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue",justify=CENTER)
lbl.pack()
sutsav=Label(f1,text="Ответ",width=60,font="Calibri 20",fg="green",bg="yellow")
sutsav.pack(side=BOTTOM)

arg=Button(f2,text="Увеличить",font="Calibri 26",fg="black",bg="green",relief=GROOVE)
arg.pack(side=TOP)
arg.bind("<Button-1>",big)


a=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
a.pack(side=LEFT)
x1=Label(f1,text="x**2+",font="Calibri 26",fg="green")
x1.pack(side=LEFT)
b=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
b.pack(side=LEFT)
x2=Label(f1,text="x+",font="Calibri 26",fg="green")
x2.pack(side=LEFT)
c=Entry(f1,width=3,font="Arial 20",fg="green",bg="lightblue")
c.pack(side=LEFT)
o=Label(f1,text="=0",font="Calibri 26",fg="green")
o.pack(side=LEFT)
 
vastus=Button(f1,text="Решить",font="Calibri 26",fg="black",bg="green",relief=GROOVE,command=test)#RAISED, SUNKEN
vastus.pack(side=RIGHT)

grafik=Button(f1,text="График",font="Calibri 26",fg="black",bg="green",relief=GROOVE,command=graafik)#RAISED, SUNKEN
grafik.pack(side=RIGHT)

r1=Radiobutton(f2,text="Кит",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=whale)
r1.pack(side=LEFT)
r2=Radiobutton(f2,text="Очки",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=glasses)
r2.pack(side=LEFT)
r3=Radiobutton(f2,text="Зонтик",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=umbrella)
r3.pack(side=LEFT)
r4=Radiobutton(f2,text="Бабочка",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=buterfly)
r4.pack(side=LEFT)
r5=Radiobutton(f2,text="Лягушка",font="Calibri 26",fg="black",bg="green",relief=GROOVE, command=frog)
r5.pack(side=LEFT)

aken.mainloop()