from tkinter import *


def R1(a1, a2, a3, a4, c, z1, z2, z3, z4, n):
    DivisionByZeroCheck(a1, a4, c)
    if n == 0:
        return 1
    if n == 1:
        return aprox1ForR1(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n == 2:
        return aprox2ForR1(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n > 2:
        dv1 = R1(a1+1, a2+1, a3, a4, c+1, z1, z2, z3, z4, n-2)
        dv2 = R4(a1+1, a2+1, a3, a4, c+1, z1, z2, z3, z4, n-2)
        dv3 = R1(a1+1, a2, a3+1, a4, c+1, z1, z2, z3, z4, n-2)
        dv4 = R4(a1+1, a2, a3+1, a4, c+1, z1, z2, z3, z4, n-2)
        return 1 - B(a2, c, z1) / (D(a1, c, a4) + F1(a1, c, z1) / dv1 + F2(a4, c, z3) / dv2) - \
               B(a3, c, z2) / (D(a1, c, a4) + F1(a1, c, z2) / dv3 + F2(a4, c, z4) / dv4)


def R4(a1, a2, a3, a4, c, z1, z2, z3, z4, n):
    DivisionByZeroCheck(a1, a4, c)
    if n == 0:
        return 1
    if n == 1:
        return aprox1ForR4(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n == 2:
        return aprox2ForR4(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n > 2:
        dv14 = R1(a1, a2+1, a3, a4+1, c+1, z1, z2, z3, z4, n-2)
        dv24 = R4(a1, a2+1, a3, a4+1, c+1, z1, z2, z3, z4, n-2)
        dv34 = R1(a1, a2, a3+1, a4+1, c+1, z1, z2, z3, z4, n-2)
        dv44 = R4(a1, a2, a3+1, a4+1, c+1, z1, z2, z3, z4, n-2)
        return 1 - B(a2, c, z3) / (D(a1, c, a4) + F2(a2, c, z3) / dv14 + F1(a4, c, z3) / dv24) - \
               B(a3, c, z4) / (D(a1, c, a4) + F2(a1, c, z2) / dv34 + F1(a4, c, z4) / dv44)


def R2(a1, a2, a3, a4, c, z1, z2, z3, z4, n):
    DivisionByZeroCheck(a2, a3, c)
    if n == 0:
        return 1
    if n == 1:
        return aprox1ForR2(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n == 2:
        return aprox2ForR2(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n > 2:
        dv1 = R2(a1+1, a2+1, a3, a4, c+1, z1, z2, z3, z4, n-2)
        dv2 = R3(a1+1, a2+1, a3, a4, c+1, z1, z2, z3, z4, n-2)
        dv3 = R2(a1, a2+1, a3, a4+1, c+1, z1, z2, z3, z4, n-2)
        dv4 = R3(a1, a2+1, a3, a4+1, c+1, z1, z2, z3, z4, n-2)
        return 1 - B(a1, c, z1) / (D(a2, c, a3) + F1(a2, c, z1) / dv1 + F2(a3, c, z2) / dv2) - \
               B(a4, c, z3) / (D(a2, c, a3) + F1(a2, c, z3) / dv3 + F2(a3, c, z4) / dv4)


def R3(a1, a2, a3, a4, c, z1, z2, z3, z4, n):
    DivisionByZeroCheck(a2, a3, c)
    if n == 0:
        return 1
    if n == 1:
        return aprox1ForR3(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n == 2:
        return aprox2ForR3(a1, a2, a3, a4, c, z1, z2, z3, z4)
    if n > 2:
        dv14 = R2(a1+1, a2, a3+1, a4, c+1, z1, z2, z3, z4, n-2)
        dv24 = R3(a1+1, a2, a3+1, a4, c+1, z1, z2, z3, z4, n-2)
        dv34 = R2(a1, a2, a3+1, a4+1, c+1, z1, z2, z3, z4, n-2)
        dv44 = R3(a1, a2, a3+1, a4+1, c+1, z1, z2, z3, z4, n-2)
        return 1 - B(a1, c, z2) / (D(a2, c, a3) + F2(a2, c, z1) / dv14 + F1(a3, c, z2) / dv24) - \
               B(a4, c, z4) / (D(a2, c, a3) + F2(a2, c, z3) / dv34 + F1(a3, c, z4) / dv44)


def aprox1ForR1(a1, a2, a3, a4, c, z1, z2, z3, z4):
    part1 = B(a2, c, z1) / D(a1, c, a4)
    part2 = B(a3, c, z2) / D(a1, c, a4)
    return 1 - part1 - part2


def aprox1ForR2(a1, a2, a3, a4, c, z1, z2, z3, z4):
    part1 = B(a1, c, z1) / D(a2, c, a3)
    part2 = B(a4, c, z3) / D(a2, c, a3)
    return 1 - part1 - part2


def aprox1ForR3(a1, a2, a3, a4, c, z1, z2, z3, z4):
    part1 = B(a1, c, z2) / D(a2, c, a3)
    part2 = B(a4, c, z4) / D(a2, c, a3)
    return 1 - part1 - part2


def aprox1ForR4(a1, a2, a3, a4, c, z1, z2, z3, z4):
    part1 = B(a2, c, z3) / D(a1, c, a4)
    part2 = B(a3, c, z4) / D(a1, c, a4)
    return 1 - part1 - part2


def aprox2ForR1(a1, a2, a3, a4, c, z1, z2, z3, z4):
    return 1 - B(a2, c, z1) / (D(a1, c, a4) + F1(a1, c, z1) + F2(a4, c, z3)) - \
           B(a3, c, z2) / (D(a1, c, a4) + F1(a1, c, z2) + F2(a4, c, z4))


def aprox2ForR2(a1, a2, a3, a4, c, z1, z2, z3, z4):
    return 1 - B(a1, c, z1) / (D(a2, c, a3) + F1(a2, c, z1) + F2(a3, c, z2)) - \
           B(a4, c, z3) / (D(a2, c, a3) + F1(a2, c, z3) + F2(a3, c, z4))


def aprox2ForR3(a1, a2, a3, a4, c, z1, z2, z3, z4):
    return 1 - B(a1, c, z2) / (D(a2, c, a3) + F2(a2, c, z1) + F1(a3, c, z2)) - \
           B(a4, c, z4) / (D(a2, c, a3) + F2(a2, c, z1) + F1(a3, c, z4))


def aprox2ForR4(a1, a2, a3, a4, c, z1, z2, z3, z4):
    return 1 - B(a1, c, z2) / (D(a2, c, a3) + F2(a2, c, z1) + F1(a3, c, z2)) - \
           B(a4, c, z4) / (D(a2, c, a3) + F2(a2, c, z3) + F1(a3, c, z4))

def D(a1, c, a4):
    return (c - a1 - a4 - 1) / c


def B(a, c, z):
    return a * z / c


def F1(a, c, z):
    tmp1 = (a + 1) * (1 - z) / c
    return tmp1


def F2(a, c, z):
    tmp1 = a * (1 - z) / c
    return tmp1

def SelectedRk(a1, a2, a3, a4, c, z1, z2, z3, z4,n,combo):
    if combo == "R1":
        return R1(a1, a2, a3, a4, c, z1, z2, z3, z4,n)
    if combo == "R2":
        return R2(a1, a2, a3, a4, c, z1, z2, z3, z4,n)
    if combo == "R3":
        return R3(a1, a2, a3, a4, c, z1, z2, z3, z4,n)
    if combo == "R4":
        return R4(a1, a2, a3, a4, c, z1, z2, z3, z4,n)


def CloseWindow():
    return 1


def DivisionByZeroCheck(b1, b2, c):
    if c == 0 or D(b1, c, b2) == 0:
        window = Tk()
        window.title("Error")
        window.geometry('200x100')
        Label(window, text="Division By Zero").grid(column=0, row=0)
        Label(window, text="Please check your values").grid(column=0, row=1)
        Button(window, text="Ok", command=window.destroy).grid(column=0, row=2)
        window.mainloop()


def UnexpectedTypeError():
    window = Tk()
    window.title("Error")
    window.geometry('200x110')
    Label(window, text=f"Wrong type of value").grid(column=0, row=0)
    Label(window, text=f"Values must be real").grid(column=0, row=1)
    Label(window, text=f"Value of n must be natural").grid(column=0, row=2)
    Label(window, text="Please change your value").grid(column=0, row=3)
    Button(window, text="Ok", command=window.destroy).grid(column=0, row=4)
    window.mainloop()


def ReadFromFile(name):
    if name == '':
        name = "input"
    name+=".txt"
    f = open(name)
    text = f.read().split()
    f.close()
    return text

