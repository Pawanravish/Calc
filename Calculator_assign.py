from tkinter import *

def OnClick(value):
    e.insert(END, value)

def Clear():
    e.delete(0, END)

def Evaluate():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

window = Tk()
window.geometry("300x400")
window.title("Basic Calculator")

e = Entry(window, font=("Arial", 18), justify="right")
e.place(x=0, y=0, height=50, width=300)

# Number Buttons
btn1 = Button(window, text="1", command=lambda: OnClick("1"), height=2, width=5)
btn1.place(x=20, y=70)

btn2 = Button(window, text="2", command=lambda: OnClick("2"), height=2, width=5)
btn2.place(x=90, y=70)

btn3 = Button(window, text="3", command=lambda: OnClick("3"), height=2, width=5)
btn3.place(x=160, y=70)

btn4 = Button(window, text="4", command=lambda: OnClick("4"), height=2, width=5)
btn4.place(x=20, y=130)

btn5 = Button(window, text="5", command=lambda: OnClick("5"), height=2, width=5)
btn5.place(x=90, y=130)

btn6 = Button(window, text="6", command=lambda: OnClick("6"), height=2, width=5)
btn6.place(x=160, y=130)

btn7 = Button(window, text="7", command=lambda: OnClick("7"), height=2, width=5)
btn7.place(x=20, y=190)

btn8 = Button(window, text="8", command=lambda: OnClick("8"), height=2, width=5)
btn8.place(x=90, y=190)

btn9 = Button(window, text="9", command=lambda: OnClick("9"), height=2, width=5)
btn9.place(x=160, y=190)

btn0 = Button(window, text="0", command=lambda: OnClick("0"), height=2, width=5)
btn0.place(x=90, y=250)

# Operators
btn_mul = Button(window, text="*", command=lambda: OnClick("*"), height=2, width=5)
btn_mul.place(x=20, y=250)

btn_add = Button(window, text="+", command=lambda: OnClick("+"), height=2, width=5)
btn_add.place(x=160, y=250)

btn_sub = Button(window, text="-", command=lambda: OnClick("-"), height=2, width=5)
btn_sub.place(x=20, y=310)

btn_div = Button(window, text="/", command=lambda: OnClick("/"), height=2, width=5)
btn_div.place(x=90, y=310)

btn_clear = Button(window, text="Clear", command=Clear, height=2, width=5)
btn_clear.place(x=160, y=310)

# Equal Button
btn_eq = Button(window, text="=", command=Evaluate, height=2, width=16)
btn_eq.place(x=20, y=370)

window.mainloop()
