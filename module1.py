from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    if klik==100:
        klik=0
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()+10)+"x"+str(aken.winfo_height()+10))
def klikker_minus(event):
    global klik
    if klik==-100:
        klik=0
    klik-=1
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()-10)+"x"+str(aken.winfo_height()-10))
def txt_to_lbl(event):
    text_to_lbl=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl,show="*")
    txt.delete(0,END)
    #aken.destroy()
def klika(event):
    global klik
    aken.destroy()
def kliko(event):
    global klik
    klik=0
    lbl.configure(text=klik)

aken=Tk()
aken.title("kp")
aken.geometry("400x600")

nupp=Button(aken,text="Я кнопка\nНажми меня!",font="Arial 20",fg="lightblue",bg="black",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
nup=Button(aken,text="\nВыйти",font="Arial 20",fg="green",bg="black",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nup.bind("<Button-1>",klika)
nuppi=Button(aken,text="\nОбнулировать",font="Arial 20",fg="green",bg="black",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nuppi.bind("<Button-1>",kliko)

lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="black")
txt=Entry(aken,width=20,font="Arial 20",fg="green",bg="black",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#Enter

nuppi.pack()
lbl.pack()
nupp.pack()#side=LEFT,TOP,RIGHT
nup.pack()
txt.pack()
aken.mainloop()
