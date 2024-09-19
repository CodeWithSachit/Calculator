
from tkinter import *


def click(event):
    global svalue
    text = event.widget.cget("text")   # this will give us the  text of the button..
    

    if text == "=":
        if svalue.get().isdigit():
            value = int (svalue.get())

        else: 
            value = eval(screen.get())
        
        svalue.set(value)
        screen.update()

    elif text == "C":
        svalue.set("")
        screen.update()

    else:
        svalue.set(svalue.get() + text)
        screen.update()


root = Tk()
root.geometry("400x400")
root.title("MY Calculator")
root.wm_iconbitmap("calculator.ico")

svalue = StringVar()
svalue.set("")
screen = Entry(root, textvariable= svalue ,font= "lucida 30 bold ")
screen.pack(fill= X,ipadx= 8,pady=10,padx=10)

f = Frame(root, bg="grey")

b = Button(f , text = "9",font = "lucida 15 bold ",padx=4,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "8",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "7",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "+",font = "lucida 15 bold ",padx=4,pady=5)
b.pack(side=LEFT,padx=4,pady=4)
b.bind('<Button -1>',click)

f.pack()


f = Frame(root, bg="grey")

b = Button(f , text = "6",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "5",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "4",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "-",font = "lucida 14 bold ",padx=4.5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

f.pack()


f = Frame(root, bg="grey")

b = Button(f , text = "3",font = "lucida 15 bold ",padx=4,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "2",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "1",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "*",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button -1>',click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f , text = "/",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=RIGHT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "0",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=RIGHT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "C",font = "lucida 15 bold ",padx=5,pady=5)
b.pack(side=RIGHT,padx=5,pady=5)
b.bind('<Button -1>',click)

b = Button(f , text = "=",font = "lucida 15 bold ",padx=4,pady=5)
b.pack(side=RIGHT,padx=4,pady=4)
b.bind('<Button -1>',click)

f.pack()



root.mainloop()