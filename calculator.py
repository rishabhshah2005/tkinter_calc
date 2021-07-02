from tkinter import *
from funcs import clear_frame
import numba
from numba import jit


@jit(nopython=True)
def clear_all(inp_b):
    inp_b.delete(0, END)

@jit(nopython=True)
def backspace(inp_b):
    st = inp_b.get()
    inp_b.delete(len(st) - 1)

@jit(nopython=True)
def calculate(inp_b):
    num = inp_b.get()
    num = num.replace('×', '*')
    num = num.replace('÷', '/')
    try:
        n = str(eval(num))
        n = n.replace('.0', '')
        inp_b.delete(0, END)
        inp_b.insert(0, string=n)
    except ZeroDivisionError:
        clear_all(inp_b)
        inp_b.insert(0, string='CANT DIVIDE BY ZERO')
    except (SyntaxError, NameError):
        clear_all(inp_b)
        inp_b.insert(0, string='ERROR')

@jit(nopython=True)
def calculator(root, win):
    clear_frame(root)
    win.geometry('565x338')
    inp_b = Entry(root, width=37, justify=RIGHT, borderwidth=5, font=('none', 20))
    inp_b.grid(ipady=5, row=0, column=0, columnspan=5)

    # NUMBER BUTTONS
    button0 = Button(root, text="0", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '0')).grid(row=5, column=1)
    button1 = Button(root, text="1", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '1')).grid(row=2, column=0)
    button2 = Button(root, text="2", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '2')).grid(row=2, column=1)
    button3 = Button(root, text="3", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '3')).grid(row=2, column=2)
    button4 = Button(root, text="4", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '4')).grid(row=3, column=0)
    button5 = Button(root, text="5", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '5')).grid(row=3, column=1)
    button6 = Button(root, text="6", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '6')).grid(row=3, column=2)
    button7 = Button(root, text="7", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '7')).grid(row=4, column=0)
    button8 = Button(root, text="8", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '8')).grid(row=4, column=1)
    button9 = Button(root, text="9", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '9')).grid(row=4, column=2)
    dot_b = Button(root, text=".", padx=41.5, pady=13, font=('none', 15, 'bold'),
                   command=lambda: inp_b.insert(END, '.')).grid(row=5, column=0)

    # BRACKET BUTTONS
    right_brac = Button(root, text=")", padx=50, pady=13, font=('none', 15, 'bold'),
                        command=lambda: inp_b.insert(END, ')')).grid(row=5, column=4)
    left_brac = Button(root, text="(", padx=50, pady=13, font=('none', 15, 'bold'),
                       command=lambda: inp_b.insert(END, '(')).grid(row=4, column=4)

    # OPERATIONS BUTTONS
    add_sym = Button(root, text="+", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '+')).grid(row=2, column=3)
    multi_sym = Button(root, text="×", padx=40, pady=13, font=('none', 15, 'bold'),
                       command=lambda: inp_b.insert(END, '×')).grid(row=4, column=3)
    sub_sym = Button(root, text="-", padx=42, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '-')).grid(row=3, column=3)
    div_sym = Button(root, text="÷", padx=40, pady=13, font=('none', 15, 'bold'),
                     command=lambda: inp_b.insert(END, '÷')).grid(row=5, column=3)

    # CLEAR BUTTON
    clear_b = Button(root, text='CLR', padx=35, pady=13, font=('none', 15, 'bold'), command=lambda: clear_all(inp_b))
    clear_b.grid(row=2, column=4)

    # BACKSPACE BUTTON
    back_b = Button(root, text='←', padx=44, pady=13, font=('none', 15, 'bold'), command=lambda: backspace(inp_b))
    back_b.grid(row=3, column=4)

    # ENTER BUTTON
    enter_b = Button(root, text="=", font=('none', 15, 'bold'), command=lambda: calculate(inp_b), padx=40, pady=13)
    enter_b.grid(row=5, column=2)
