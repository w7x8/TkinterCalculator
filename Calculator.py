import tkinter
from tkinter import *
from tkinter import messagebox

op = ""
value = ""
X = 0



def buttonclick1():
    global value
    value = value + "1"
    data.set(value)


def buttonclick2():
    global value
    value = value + "2"
    data.set(value)


def buttonclick3():
    global value
    value = value + "3"
    data.set(value)


def buttonclick4():
    global value
    value = value + "4"
    data.set(value)


def buttonclick5():
    global value
    value = value + "5"
    data.set(value)


def buttonclick6():
    global value
    value = value + "6"
    data.set(value)


def buttonclick7():
    global value
    value = value + "7"
    data.set(value)


def buttonclick8():
    global value
    value = value + "8"
    data.set(value)


def buttonclick9():
    global value
    value = value + "9"
    data.set(value)


def buttonclick0():
    global value
    value = value + "0"
    data.set(value)


def buttonclickplus():
    global X
    global op
    global value
    X = int(value)
    op = "+"
    value = value + "+"
    data.set(value)


def buttonclickmin():
    global X
    global op
    global value
    X = int(value)
    op = "-"
    value = value + "-"
    data.set(value)


def buttonclickmult():
    global X
    global op
    global value
    X = int(value)
    op = "*"
    value = value + "*"
    data.set(value)


def buttonclickdiv():
    global X
    global op
    global value
    X = int(value)
    op = "/"
    value = value + "/"
    data.set(value)


def buttonclickc():
    global X
    global op
    global value
    X = 0
    op = ""
    value = ""
    data.set(value)


def result():
    global X
    global op
    global value
    val2 = value
    if op == "+":
        B = int((val2.split("+")[1]))
        C = X + B
        data.set(C)
        value = str(C)

    elif op == "-":
        B = int((val2.split("-")[1]))
        C = X - B
        data.set(C)
        value = str(C)

    elif op == "*":
        B = int((val2.split("*")[1]))
        C = X * B
        data.set(C)
        value = str(C)

    elif op == "/":
        B = int((val2.split("/")[1]))
        if B == 0 :
            messagebox.showerror("Error","Divisible by 0 not allowed.")
            X = ""
            value = ""
            data.set(value)
        else:
            C = int(X / B)
            data.set(C)
            value = str(C)


root = tkinter.Tk()
root.geometry("250x400+300+300")

root.resizable(0, 0)

root.title("Calculator")

data = StringVar()
lbl = Label(
    root,
    text="LABEL",
    anchor=SE,
    font=("Helvetica", 20),
    textvariable=data,
    background="#ffffff",
    fg="#000000"
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text="1",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick1
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick2
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick3

)
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclickplus
)
btnplus.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text="4",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick4

)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick5

)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick6

)
btn6.pack(side=LEFT, expand=True, fill="both")

btnminus = Button(
    btnrow2,
    text="-",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclickmin
)
btnminus.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow3,
    text="7",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick7

)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick8

)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick9

)
btn9.pack(side=LEFT, expand=True, fill="both")

btnmult = Button(
    btnrow3,
    text="x",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclickmult

)
btnmult.pack(side=LEFT, expand=True, fill="both")

btnc = Button(
    btnrow4,
    text="C",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclickc
)
btnc.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclick0

)
btn0.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=result
)
btnequal.pack(side=LEFT, expand=True, fill="both")

btndiv = Button(
    btnrow4,
    text="÷",
    font=("Helvetica", 22),
    relief=GROOVE,
    border=0,
    command=buttonclickdiv

)
btndiv.pack(side=LEFT, expand=True, fill="both")


root.title("Calculator")
root.iconbitmap("calogo.ico")
root.mainloop()