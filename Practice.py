from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import Combobox
from function import *


def insertFromFile():
    name=inputData.get()
    data = ReadFromFile(name)
    a1.delete(0, 'end')
    a1.insert(INSERT, data[0])
    a2.delete(0, 'end')
    a2.insert(INSERT, data[1])
    a3.delete(0, 'end')
    a3.insert(INSERT, data[2])
    a4.delete(0, 'end')
    a4.insert(INSERT, data[3])
    c.delete(0, 'end')
    c.insert(INSERT, data[4])
    z1.delete(0, 'end')
    z1.insert(INSERT, data[5])
    z2.delete(0, 'end')
    z2.insert(INSERT, data[6])
    z3.delete(0, 'end')
    z3.insert(INSERT, data[7])
    z4.delete(0, 'end')
    z4.insert(INSERT, data[8])
    n.delete(0, 'end')
    n.insert(INSERT, data[9])


def save():
    cur_inp = txt.get("1.0", END)
    newfl=fileName.get()
    newfl=newfl+".txt"
    fl = open(newfl, "w")
    fl.write(cur_inp)
    fl.close()


def clicked():
    txt.delete('1.0', END)
    rk = combo.get()
    try:
        b1 = getdouble(a1.get())
        b2 = getdouble(a2.get())
        b3 = getdouble(a3.get())
        b4 = getdouble(a4.get())
        k = getdouble(c.get())
        y1 = getdouble(z1.get())
        y2 = getdouble(z2.get())
        y3 = getdouble(z3.get())
        y4 = getdouble(z4.get())
        m = int(n.get())
    except:
        UnexpectedTypeError()
    txt.insert(INSERT, f"Approximants for {rk}\n\n")
    txt.insert(INSERT, f"a1 = {b1} a2 = {b2} a3 = {b3} a4 = {b4}\nz1 = {y1} z2 = {y2} z3 = {y3} z4 = {y4}\nn = {m} c = {k}\n\n")
    for i in range(m+1):
        txt.insert(INSERT, str(i))
        txt.insert(INSERT, ' approximant = ')
        txt.insert(INSERT, SelectedRk(b1, b2, b3, b4, k, y1, y2, y3, y4, i, rk))
        txt.insert(INSERT, '\n')


if __name__ == '__main__':
    window = Tk()
    window.title("Сalculation of approximants")
    window.geometry('400x400')

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Data')
    tab_control.add(tab2, text='Result')

    Label(tab1, text="a1").grid(column=0, row=0)
    a1 = Entry(tab1, width=10)
    a1.grid(column=1, row=0)

    Label(tab1, text="a2").grid(column=2, row=0)
    a2 = Entry(tab1, width=10)
    a2.grid(column=3, row=0)

    Label(tab1, text="a3").grid(column=4, row=0)
    a3 = Entry(tab1, width=10)
    a3.grid(column=5, row=0)

    Label(tab1, text="a4").grid(column=6, row=0)
    a4 = Entry(tab1, width=10)
    a4.grid(column=7, row=0)

    Label(tab1, text="c").grid(column=0, row=1)
    c = Entry(tab1, width=10)
    c.grid(column=1, row=1)

    Label(tab1, text="z1").grid(column=2, row=1)
    z1 = Entry(tab1, width=10)
    z1.grid(column=3, row=1)

    Label(tab1, text="z2").grid(column=4, row=1)
    z2 = Entry(tab1, width=10)
    z2.grid(column=5, row=1)

    Label(tab1, text="z3").grid(column=6, row=1)
    z3 = Entry(tab1, width=10)
    z3.grid(column=7, row=1)

    Label(tab1, text="z4").grid(column=0, row=2)
    z4 = Entry(tab1, width=10)
    z4.grid(column=1, row=2)

    Label(tab1, text="n").grid(column=2, row=2)
    n = Entry(tab1, width=10)
    n.grid(column=3, row=2)
    combo = Combobox(tab1, width=8, state="readonly")
    combo['values'] = ("R1","R2","R3","R4")
    combo.current(0)
    combo.grid(column=1, row=4)

    btn = Button(tab1, text="Calculate", command=clicked)
    btn.grid(column=3, row=4)

    Label(tab1, text="File name: ").grid(column = 1, row = 3)
    inputData = Entry(tab1, width = 10)
    inputData.grid(column = 3, row = 3)

    btn = Button(tab1, text="Read data", command=insertFromFile)
    btn.grid(column=5, row=3)

    txt = scrolledtext.ScrolledText(tab2, width = 45, height = 20)
    txt.grid(column=1, row=1, columnspan=5)
    
    Label(tab2, text="File name: ").grid(column = 1, row = 0)
    fileName = Entry(tab2, width = 10)
    fileName.grid(column = 2, row = 0)
    btn = Button(tab2, text="Save to File", command=save)
    btn.grid(column=3, row=0)

    tab_control.pack(expand=1, fill='both')

    window.mainloop()
