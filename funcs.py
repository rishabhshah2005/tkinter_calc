from tkinter import *
import math

PIE = 22 / 7


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def decim(imp):
    imp = str(imp)
    le = len(imp)
    a = imp.split('.')
    len_d = len(a[1])
    mi = len_d - 4
    b = le - mi
    imp = imp[0:b]
    if imp.endswith('.0'):
        imp = imp.replace('.0', '')
    return imp


def get_hype(r, h):
    hype = math.hypot(h, r)
    return hype


# Formulas For cube

def cube(root, win):
    clear_frame(root)
    win.geometry('300x300')
    frame = Frame(root)
    frame.grid(row=3, column=0, columnspan=2)
    a = StringVar()
    a.set('')
    lbl = Label(root, text='Length of side = ').grid(row=0, column=0, pady=20, padx=20, sticky="nsew")
    inp = Entry(root, width=25, textvariable=a, borderwidth=5).grid(row=0, column=1, pady=20, sticky="nsew")

    def clc():
        clear_frame(frame)
        try:
            side = float(a.get())
            len_of_all = 6 * side
            tsa = 6 * side ** 2
            csa = 4 * side ** 2
            vol = side ** 3
            tsa = decim(tsa)
            csa = decim(csa)
            vol = decim(vol)
            len_of_all = decim(len_of_all)

            l_len = Label(frame, text=f"Length of all sides = {len_of_all}").grid(row=3, column=0, columnspan=2)
            tsa_l = Label(frame, text=f"TSA = {tsa}").grid(row=4, column=0, columnspan=2)
            csa_l = Label(frame, text=f"CSA = {csa}").grid(row=5, column=0, columnspan=2)
            vol_l = Label(frame, text=f"Volume = {vol}").grid(row=6, column=0, columnspan=2)

        except ValueError:
            clear_frame(frame)
            label = Label(frame, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    btn = Button(root, padx=10, pady=10, command=clc, text='Calculate').grid(row=2, column=0, columnspan=2, pady=10)


# Formulas for cuboid

def cuboid(root, win):
    clear_frame(root)
    win.geometry("300x300")
    # ENTRY BOX LABELS
    Label(root, text="Length = ").grid(row=0, column=0, padx=15, pady=10)
    Label(root, text="Breath = ").grid(row=1, column=0, padx=15, pady=10)
    Label(root, text="Height = ").grid(row=2, column=0, padx=15, pady=10)

    # ENTRY BOXES
    l = StringVar()
    l.set('')
    inp_l = Entry(root, width=25, textvariable=l, borderwidth=5).grid(row=0, column=1)
    b = StringVar()
    b.set('')
    inp_b = Entry(root, width=25, textvariable=b, borderwidth=5).grid(row=1, column=1)
    h = StringVar()
    h.set('')
    inp_h = Entry(root, width=25, textvariable=h, borderwidth=5).grid(row=2, column=1)
    fram = Frame(root)
    fram.grid(row=4, column=0, columnspan=2)

    # Calculating

    def calc():
        try:
            clear_frame(fram)
            len = float(l.get())
            bre = float(b.get())
            hgt = float(h.get())
            l_of_all_edges = 4 * (len + bre + hgt)
            tsa = 2 * (len * bre + bre * hgt + hgt * len)
            csa = 2 * hgt * (len + bre)
            vol = len * bre * hgt
            tsa = decim(tsa)
            csa = decim(csa)
            vol = decim(vol)
            l_of_all_edges = decim(l_of_all_edges)
            # Labels
            l_of_al = Label(fram, text=f"Length of all edges = {l_of_all_edges}")
            tsa_l = Label(fram, text=f"TSA = {tsa}")
            csa_l = Label(fram, text=f"CSA = {csa}")
            vol_l = Label(fram, text=f"Volume = {vol}")
            # Putting Labels up
            l_of_al.pack()
            tsa_l.pack()
            csa_l.pack()
            vol_l.pack()

        except ValueError:
            clear_frame(fram)
            label = Label(fram, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    btn = Button(root, text="Calculate", padx=10, pady=8, command=calc).grid(row=3, column=0, columnspan=2, padx=25,
                                                                             pady=15)


# CYLINDER


def cylinder(root, win):
    clear_frame(root)
    win.geometry("300x300")
    frm = Frame(root)
    frm.grid(row=3, column=0, columnspan=2, pady=15)
    # LABELS
    radius = Label(root, text="Radius = ").grid(row=0, column=0, pady=10, padx=15)
    height = Label(root, text="Height = ").grid(row=1, column=0, pady=10, padx=15)
    # Entry Boxes
    rd = StringVar()
    rd.set('')
    rad = Entry(root, width=25, textvariable=rd, borderwidth=5).grid(row=0, column=1)
    ht = StringVar()
    ht.set('')
    hgt = Entry(root, width=25, textvariable=ht, borderwidth=5).grid(row=1, column=1)

    # Calc func
    def calc():
        try:
            r = float(rd.get())
            h = float(ht.get())
            clear_frame(frm)
            tsa = eval(f"2*{PIE}*{r}*({r}+{h})")
            csa = eval(f"2*{PIE}*{r}*{h}")
            vol = eval(f"{PIE}*{r}**2*{h}")
            tsa = decim(tsa)
            csa = decim(csa)
            vol = decim(vol)
            vol_l = Label(frm, text=f"Volume = {vol}").pack()
            tsa_l = Label(frm, text=f"TSA = {tsa}").pack()
            csa_l = Label(frm, text=f'CSA = {csa}').pack()

        except ValueError:
            clear_frame(frm)
            label = Label(frm, text="ERROR", font=('helvetica', 20, 'bold')).pack()

        # BUTTON

    btn = Button(root, text="Calculate", padx=15, pady=15, command=calc).grid(row=2, column=0, columnspan=2, pady=15)


# CONE


def cone(root, win):
    clear_frame(root)
    win.geometry('300x300')
    frm = Frame(root)
    frm.grid(row=3, column=0, columnspan=2)
    r = StringVar()
    r.set('')
    rad = Entry(root, width=25, borderwidth=5, textvariable=r).grid(row=0, column=1)
    h = StringVar()
    h.set('')
    hgt = Entry(root, width=25, borderwidth=5, textvariable=h).grid(row=1, column=1)
    # Labels
    rad_l = Label(root, text="Radius = ").grid(row=0, column=0, padx=15, pady=10)
    hgt_l = Label(root, text="Height = ").grid(row=1, column=0, padx=15, pady=10)

    # Calculating
    def calc():
        clear_frame(frm)
        try:
            rd = float(r.get())
            ht = float(h.get())
            til = decim(get_hype(rd, ht))
            tsa = eval(f'{PIE}*{rd}*({rd}+{til})')
            csa = eval(f"{PIE}*{rd}*{til}")
            vol = eval(f"1/3 * {PIE}* {rd}**2 * {ht}")
            tsa = decim(tsa)
            csa = decim(csa)
            vol = decim(vol)
            til_l = Label(frm, text=f"Hypotenuse = {til}").pack()
            tsa_l = Label(frm, text=f"TSA = {tsa}").pack()
            csa_l = Label(frm, text=f"CSA = {csa}").pack()
            vol_l = Label(frm, text=f"Volume = {vol}").pack()

        except ValueError:
            clear_frame(frm)
            label = Label(frm, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    btn = Button(root, text="Calculate", padx=15, pady=15, command=calc).grid(row=2, column=0, columnspan=2, padx=20,
                                                                              pady=15)


# Sphere

def sphere(root, win):
    clear_frame(root)
    win.geometry('300x300')
    l_radius = Label(root, text="Radius = ", pady=15).grid(row=0, column=0, padx=15, pady=10)
    frm = Frame(root)
    frm.grid(row=3, column=0, columnspan=2, padx=15, pady=20)
    r = StringVar()
    r.set('')
    rad = Entry(root, width=25, borderwidth=5, textvariable=r).grid(row=0, column=1, pady=10)

    # Calculating
    def calc():
        clear_frame(frm)
        try:
            rd = float(r.get())
            tsa = eval(f"4 * {PIE} * {rd}**2")
            vol = eval(f"4/3 * {PIE} * {rd}**3")
            tsa = decim(tsa)
            vol = decim(vol)
            # Labels
            tsa_l = Label(frm, text=f"TSA = {tsa}").pack()
            vol_l = Label(frm, text=f"Volume = {vol}").pack()

        except ValueError:
            clear_frame(frm)
            label = Label(frm, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    # BUTTON
    btn = Button(root, text="Calculate", padx=15, pady=15, command=calc).grid(row=1, column=0, columnspan=2, padx=15,
                                                                              pady=20)


# Hemisphere


def hemisphere(root, win):
    clear_frame(root)
    win.geometry('300x300')
    l_radius = Label(root, text="Radius = ", pady=15).grid(row=0, column=0, padx=15, pady=10)
    frm = Frame(root)
    frm.grid(row=3, column=0, columnspan=2, padx=15, pady=20)
    r = StringVar()
    r.set('')
    rad = Entry(root, width=25, borderwidth=5, textvariable=r).grid(row=0, column=1, pady=10)

    # Calculating
    def calc():
        clear_frame(frm)
        try:
            rd = float(r.get())
            tsa = eval(f"3 * {PIE} * {rd}**2")
            csa = eval(f"2 * {PIE} * {rd}**2")
            vol = eval(f"2/3 * {PIE} * {rd}**3")
            tsa = decim(tsa)
            vol = decim(vol)
            csa = decim(csa)
            # Labels
            tsa_l = Label(frm, text=f"TSA = {tsa}").pack()
            csa_l = Label(frm, text=f"CSA = {csa}").pack()
            vol_l = Label(frm, text=f"Volume = {vol}").pack()


        except ValueError:
            clear_frame(frm)
            label = Label(frm, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    # BUTTON
    btn = Button(root, text="Calculate", padx=15, pady=15, command=calc).grid(row=1, column=0, columnspan=2, padx=15,
                                                                              pady=20)


# Circle


def circle(root, win):
    clear_frame(root)
    win.geometry('300x300')
    l_radius = Label(root, text="Radius = ", pady=15).grid(row=0, column=0, padx=15, pady=10)
    frm = Frame(root)
    frm.grid(row=3, column=0, columnspan=2, padx=15, pady=20)
    r = StringVar()
    r.set('')
    rad = Entry(root, width=25, borderwidth=5, textvariable=r).grid(row=0, column=1, pady=10)

    # Calculating
    def calc():
        clear_frame(frm)
        try:
            rd = float(r.get())
            circ = decim(eval(f"2 * {PIE} * {rd}"))
            ar = decim(eval(f"{PIE} * {rd} ** 2"))
            circum = Label(frm, text=f"Circumference = {circ}").pack()
            area = Label(frm, text=f"Area = {ar}").pack()

        except ValueError:
            clear_frame(frm)
            label = Label(frm, text="ERROR", font=('helvetica', 20, 'bold')).pack()

    # BUTTON
    btn = Button(root, text="Calculate", padx=15, pady=15, command=calc).grid(row=1, column=0, columnspan=2, padx=15,
                                                                              pady=20)


def about_me(root, win):
    clear_frame(root)
    win.geometry('500x300')
    label1 = Label(root, text='Made by', font=('helvetica', 40, 'bold')).pack()
    label2 = Label(root, text='Rishabh Shah', font=('helvetica', 40, 'bold')).pack()


def hlp(root, win):
    clear_frame(root)
    win.geometry('700x200')
    lab = Label(root,
                text='For using powers in calculations add "×" 2 times \n \n This program uses python\nAny python mathematical \nfunctions can be used in the Calculator',
                font=('helvetica', 20, 'bold')).pack()

# MADE BY RISHABH SHAH
