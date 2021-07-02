from tkinter import *
from calculator import calculator, calculate, clear_all, backspace
from funcs import *
import numba
from numba import jit


def main():
    root = Tk()
    root.title('Calculator')
    root.iconbitmap('icon/calc.ico')

    # frame
    frm = Frame(root)
    frm.pack(side="top", expand=True, fill="both")
    calculator(frm, root)

    men = Menu(root)
    oth_calcs = Menu(men, tearoff=0)  # Creating menu

    # adding items
    oth_calcs.add_command(label='Normal', command=lambda: calculator(frm, root))
    oth_calcs.add_command(label='Circle', command=lambda: circle(frm, root))
    oth_calcs.add_command(label='Cube', command=lambda: cube(frm, root))
    oth_calcs.add_command(label='Cuboid', command=lambda: cuboid(frm, root))
    oth_calcs.add_command(label='Cylinder', command=lambda: cylinder(frm, root))
    oth_calcs.add_command(label='Cone', command=lambda: cone(frm, root))
    oth_calcs.add_command(label='Sphere', command=lambda: sphere(frm, root))
    oth_calcs.add_command(label="Hemisphere", command=lambda: hemisphere(frm, root))

    men.add_cascade(label='Calculators', menu=oth_calcs)  # Putting up the menu

    # Help Menu
    hp = Menu(men, tearoff=0)
    men.add_command(label='Help', command=lambda: hlp(frm, root))

    # About Menu
    about = Menu(men, tearoff=0)
    men.add_command(label='About', command=lambda: about_me(frm, root))

    root.config(menu=men)
    root.mainloop()

main()