from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import file as f

root = Tk()

frame01 = Frame(root, bg="#001e33", width=450, height=80, bd=3, relief=RIDGE)
frame01.grid(row=0, column=0, columnspan=2, sticky="ew")
frame01.rowconfigure(0, weight=1)
frame01.columnconfigure(0, weight=1)
frame01.columnconfigure(1, weight=1)
frame01.grid_propagate(0)

labelB = Label(
    frame01,
    text="Ucitajte fajl sa linijama gradskog prevoza",
    fg="white",
    bg="#001e33",
    font=("Lucida Console", "10", "bold"),
)
labelB.grid(row=0, column=0, sticky="e")
buttonB = Button(
    frame01,
    text="UCITAJ",
    bg="#006bb2",
    padx=10,
    fg="white",
    command=lambda: f.ucitajL(
        filedialog.askopenfilename(filetypes=(("text files", "*.txt"),)), root, button
    ),
)
buttonB.grid(row=0, column=1, sticky="w")


def potvrdi():
    label1.config(text=f"Prikaz informacija")
    text.delete("1.0", END)
    meniS.config(values=tuple(f.stanice))
    meniP_Poc.config(values=tuple(f.stanice))
    meniP_Kraj.config(values=tuple(f.stanice))
    l = []
    for i in f.linije:
        l.append(i[0])
    meniL.config(values=tuple(l))


button = Button(
    frame01, text="OBRADI", bg="#006bb2", fg="white", padx=10, command=potvrdi
)


frame1 = Frame(root, bg="#001e33", width=450, height=80, bd=3, relief=RIDGE)
frame1.grid(row=0, column=0, columnspan=2, sticky="ew")
frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.grid_propagate(0)

labelA = Label(
    frame1,
    text="Ucitajte fajl sa stajalistima",
    fg="white",
    bg="#001e33",
    font=("Lucida Console", "10", "bold"),
)
labelA.grid(row=0, column=0, sticky="e")
buttonA = Button(
    frame1,
    text="UCITAJ",
    bg="#006bb2",
    padx=10,
    fg="white",
    command=lambda: f.ucitajS(
        filedialog.askopenfilename(filetypes=(("text files", "*.txt"),)), root, buttonA1
    ),
)
buttonA.grid(row=0, column=1, sticky="w")
buttonA1 = Button(
    frame1,
    text="DALJE",
    bg="#006bb2",
    padx=10,
    fg="white",
    command=lambda: frame01.lift(),
)


frame2 = Frame(root, bg="#001e33", width=300, height=600, bd=3, relief=RIDGE)
frame2.grid(row=1, column=0, sticky="ns")
frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)
frame2.rowconfigure(2, weight=1)
frame2.rowconfigure(3, weight=1)
frame2.rowconfigure(4, weight=1)
frame2.rowconfigure(5, weight=1)
frame2.rowconfigure(6, weight=1)
frame2.columnconfigure(0, weight=1)
frame2.grid_propagate(0)

labelL = Label(
    frame2,
    text="Prikaz informacija o linijama\nIzaberite oznaku linije cije informacije\nzelite da prikazete.",
    fg="white",
    bg="#001e33",
)
labelL.grid(row=0, column=0, sticky="s")
vrL = StringVar()
vrL.set("Izaberi liniju")
meniL = ttk.Combobox(frame2, textvariable=vrL, values=())
meniL.grid(row=1, column=0)
bS = Button(
    frame2,
    text="PRIKAZI",
    bg="#006bb2",
    fg="white",
    padx=10,
    command=lambda: f.ispisL(text, vrL.get(), label1),
)
bS.grid(row=2, column=0, sticky="n")

labelS = Label(
    frame2,
    text="Prikaz informacija o stajalistima\nIzaberite oznaku stajalista cije informacije\nzelite da prikazete",
    fg="white",
    bg="#001e33",
)
labelS.grid(row=3, column=0, sticky="s")
vrS = StringVar()
vrS.set("Izaberi stajaliste")
meniS = ttk.Combobox(frame2, textvariable=vrS, values=())
meniS.grid(row=4, column=0)
bL = Button(
    frame2,
    text="PRIKAZI",
    bg="#006bb2",
    fg="white",
    padx=10,
    command=lambda: f.ispisS(text, vrS.get(), label1),
)
bL.grid(row=5, column=0, sticky="n")

bf1 = Button(
    frame2,
    text="VRATI SE",
    bg="#006bb2",
    fg="white",
    padx=10,
    command=lambda: frame4.lift(),
)
bf1.grid(row=6, column=0, sticky="sw")


frame4 = Frame(root, bg="#001e33", width=300, height=600, bd=3, relief=RIDGE)
frame4.grid(row=1, column=0, sticky="ns")
frame4.rowconfigure(0, weight=1)
frame4.rowconfigure(1, weight=1)
frame4.rowconfigure(2, weight=1)
frame4.rowconfigure(3, weight=1)
frame4.rowconfigure(4, weight=1)
frame4.columnconfigure(0, weight=1)
frame4.grid_propagate(0)
labelP = Label(
    frame4,
    text="Prikaz\nputanje",
    fg="white",
    bg="#001e33",
    font=("Lucida Console", "15", "bold"),
)
labelP.grid(row=0, column=0)
vrP_Poc = StringVar()
vrP_Poc.set("Izaberi pocetno stajaliste")
meniP_Poc = ttk.Combobox(frame4, textvariable=vrP_Poc, values=())
meniP_Poc.grid(row=1, column=0)
vrP_Kraj = StringVar()
vrP_Kraj.set("Izaberi krajnje stajaliste")
meniP_Kraj = ttk.Combobox(frame4, textvariable=vrP_Kraj, values=())
meniP_Kraj.grid(row=2, column=0)


bP = Button(
    frame4,
    text="PRIKAZI",
    bg="#006bb2",
    fg="white",
    padx=10,
    command=lambda: f.ispisPut(vrP_Poc.get(), vrP_Kraj.get(), label1, text),
)
bP.grid(row=3, column=0, sticky="n")

bf2 = Button(
    frame4,
    text="JOS OPCIJA...",
    bg="#006bb2",
    fg="white",
    padx=10,
    command=lambda: frame2.lift(),
)
bf2.grid(row=4, column=0, sticky="se")


frame3 = Frame(root, bg="#001e33", width=600, height=600, bd=3, relief=RIDGE)
frame3.grid(row=1, column=1)
label1 = Label(
    frame3,
    fg="white",
    relief=GROOVE,
    font=("Lucida Console", "20", "bold"),
    bg="#001e33",
)
label1.grid(row=0, column=0, columnspan=2, sticky="ew")
text = Text(
    frame3,
    height=28,
    width=60,
    relief=SUNKEN,
    bg="#006bb2",
    bd=4,
    font=("Lucida Console", "15", "bold"),
    fg="white",
)
text.grid(row=1, column=0)
scrollbar = Scrollbar(frame3, orient=VERTICAL, width=25, bg="#001e33")
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
scrollbar.grid(row=1, column=1, sticky="ns")


root.mainloop()
