import tkinter as t
from functools import partial
window=t.Tk(className="calculator")
window.geometry("1000x600")

label=t.Label(text="MY CALCULATOR",font="Helvetica 25 bold",bg="black",relief="sunken",bd=10,fg="white")
label.pack(fill="x")

var=t.StringVar()

def onclick(x):
    length=len(var.get())
    if x=="C":
        screen.delete(0,length)
    elif x!="=":
        screen.insert(length,x)
    else:
        try:
            var.set(str(eval(var.get().replace("^","**"))))
        except (SyntaxError,ZeroDivisionError):
            var.set("Error")

screen=t.Entry(width=26,bg="white",textvariable=var,bd=20,relief="ridge",font="Helvetica 20 bold")
screen.pack()
frame=t.Frame()
frame.pack()

buttonlist="123.C456+-789*/(0)^="
count=0
packet=[]
for i in range(1,5):
    for j in range(5):
        click=partial(onclick,buttonlist[count])
        if buttonlist[count].isdigit():
            packet.append(t.Button(frame,bg="green",text=buttonlist[count],command=click,width=5,height=2,relief="groove",bd=10,font="Helvetica 15 bold"))
        elif buttonlist[count]=="C":
            packet.append(t.Button(frame,bg="red", text=buttonlist[count], command=click, width=5, height=2, relief="groove",bd=10, font="Helvetica 15 bold"))
        else:
            packet.append(t.Button(frame,bg="skyblue", text=buttonlist[count], command=click, width=5, height=2, relief="groove",bd=10, font="Helvetica 15 bold"))
        packet[-1].grid(row=i,column=j)
        count+=1
window.mainloop()

#testing the working of remote repository VSCode extension
