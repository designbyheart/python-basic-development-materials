from tkinter import *
from random import shuffle
from tkinter import messagebox

stanice = {}
linije = []
vazne_stanice = []


def ucitajS(fajl_S, root, bA1):
    global stanice
    global vazne_stanice
    uspesno = 1
    with open(fajl_S, "r") as dat1:
        for red in dat1:
            if red[-1] != "\n":
                stanica = red.split(" ")
            else:
                stanica = red[:-1].split(" ")

            try:
                int(stanica[0])
            except:
                messagebox.showerror(
                    master=root,
                    title="showerror",
                    message="Pogresan fajl!\nUcitajte ponovo!",
                )
                stanice = {}
                vazne_stanice = []
                uspesno = 0
                break
            else:
                duz = len(stanica)
                if stanica[duz - 1] == "[!]":
                    vazne_stanice.append(stanica[0])
                    stanica.remove("[!]")
                stanice
                stanice[stanica[0]] = {}
                stanice[stanica[0]]["naziv"] = " ".join(stanica[1:])
    if uspesno:
        bA1.grid(row=0, column=2)
    dat1.close()


def ucitajL(fajl_L, root, b):
    with open(fajl_L, "r") as dat2:
        global linije
        global stanice
        uspesno = 1
        for red in dat2:
            if red[-1] != "\n":
                linija = red.split(" ")
            else:
                linija = red[:-1].split(" ")

            try:
                for i in linija[1:]:
                    int(i)
            except:
                messagebox.showerror(
                    master=root,
                    title="showerror",
                    message="Pogresan fajl!\nUcitajte ponovo!",
                )
                uspesno = 0
                break
            else:
                linije.append(linija)

                for i in linija[1:]:
                    if "linije" not in stanice[i].keys():
                        stanice[i]["linije"] = []
                        stanice[i]["linije"].append(linija[0])
                    else:
                        stanice[i]["linije"].append(linija[0])

                for i in range(1, len(linija)):
                    if i == 1:
                        if "susedi" not in stanice[linija[i]].keys():
                            stanice[linija[i]]["susedi"] = []
                            stanice[linija[i]]["susedi"].append(linija[i + 1])
                        else:
                            if linija[i + 1] not in stanice[linija[i]]["susedi"]:
                                stanice[linija[i]]["susedi"].append(linija[i + 1])
                    elif i == (len(linija) - 1):
                        if "susedi" not in stanice[linija[i]].keys():
                            stanice[linija[i]]["susedi"] = []
                            stanice[linija[i]]["susedi"].append(linija[i - 1])
                        else:
                            if linija[i - 1] not in stanice[linija[i]]["susedi"]:
                                stanice[linija[i]]["susedi"].append(linija[i - 1])
                    else:
                        if "susedi" not in stanice[linija[i]].keys():
                            stanice[linija[i]]["susedi"] = []
                            stanice[linija[i]]["susedi"].append(linija[i - 1])
                            stanice[linija[i]]["susedi"].append(linija[i + 1])
                        else:
                            if linija[i - 1] not in stanice[linija[i]]["susedi"]:
                                stanice[linija[i]]["susedi"].append(linija[i - 1])
                            if linija[i + 1] not in stanice[linija[i]]["susedi"]:
                                stanice[linija[i]]["susedi"].append(linija[i + 1])
    if uspesno:
        b.grid(row=0, column=2)
    dat2.close()


def ispisL(text, lin, lb):
    t = f"Linija_{lin}"
    lb.config(text=t)
    text.delete("1.0", END)
    lista = []
    duz = 0
    for i in linije:
        if i[0] == lin:
            lista = i[1:]
            duz = len(lista)
    text.insert(
        END, f"{lin} {stanice[lista[0]]['naziv']}->{stanice[lista[duz-1]]['naziv']}\n"
    )
    for i in lista:
        text.insert(END, f"{i} {stanice[i]['naziv']} ")
        if i in vazne_stanice:
            text.insert(END, "[!]")
        text.insert(END, "\n")


def ispisS(text, st, lb):
    t = f"Stajaliste_{st}"
    lb.config(text=t)
    text.delete("1.0", END)
    text.insert(END, f"{st} [")
    for i in range(0, len(stanice[st]["linije"])):
        if i == (len(stanice[st]["linije"]) - 1):
            text.insert(END, f"{stanice[st]['linije'][i]}] ")
            text.insert(END, "{! ")
        else:
            text.insert(END, f"{stanice[st]['linije'][i]} ")

    skup = tuple(set(stanice[st]["susedi"]) & set(vazne_stanice))
    if len(skup):
        for j in range(0, len(skup)):
            if j == (len(skup) - 1):
                text.insert(END, f"{skup[j]} ")
                text.insert(END, "!}\n")
            else:
                text.insert(END, f"{skup[j]} ")
    else:
        text.insert(END, "!}\n")


def ispisPut(poc, kraj, lb1, t):
    lb1.config(text=f"Putanja_{poc}_{kraj}")
    t.delete("1.0", END)
    Strategy1.putanja, Strategy1.busevi, Strategy1.konacno, Strategy1.nadjeno = (
        [],
        [],
        [],
        0,
    )
    (
        Strategy2.stan,
        Strategy2.lin,
        Strategy2.kolona,
        Strategy2.krajnje,
        Strategy2.nadjeno,
        Strategy2.k,
    ) = ([], [], [], [], 0, 0)

    Strategy2.trazi(poc, kraj)

    print(Strategy2.krajnje)
    print(stanice)

    if Strategy2.nadjeno:
        Strategy1.trazi(poc, kraj, [])
        i = 0
        j = 1
        pret = [""]

        while j < len(Strategy1.konacno) - 1:
            if j == len(Strategy1.konacno) - 2:
                t.insert(END, f"{pret[0]}->{Strategy1.konacno[j][0]}\n")
                for k in range(i, j + 2, 2):
                    t.insert(END, f"{Strategy1.konacno[k]} ")
                t.insert(END, "\n")
                break
            if set(Strategy1.konacno[j]) & set(Strategy1.konacno[j + 2]):
                Strategy1.konacno[j] = list(
                    set(Strategy1.konacno[j]) & set(Strategy1.konacno[j + 2])
                )
                Strategy1.konacno[j + 2] = list(
                    set(Strategy1.konacno[j]) & set(Strategy1.konacno[j + 2])
                )
                j += 2
            else:
                t.insert(END, f"{pret[0]}->{Strategy1.konacno[j][0]}\n")
                for k in range(i, j + 2, 2):
                    t.insert(END, f"{Strategy1.konacno[k]} ")
                t.insert(END, "\n")
                i = j + 1
                pret = Strategy1.konacno[j]
                j += 2

        t.insert(END, "\n\n\n")

        for i in range(0, len(Strategy2.krajnje) - 1):
            tren_l = Strategy2.krajnje[i][2]
            sled_l = Strategy2.krajnje[i + 1][2]
            t.insert(END, f"{tren_l}->{sled_l}\n")

            for l in linije:
                if l[0] == sled_l:
                    p = l[1:].index(Strategy2.krajnje[i][0]) + 1
                    k = l[1:].index(Strategy2.krajnje[i + 1][0]) + 1
                    if Strategy2.krajnje[i + 1][1] == "L":
                        while p >= k:
                            t.insert(END, f"{l[p]} ")
                            p -= 1

                    if Strategy2.krajnje[i + 1][1] == "D":
                        while p <= k:
                            t.insert(END, f"{l[p]} ")
                            p += 1
            t.insert(END, "\n")

    else:
        t.insert(END, "Putanja ne postoji!\n")


class Strategy1:
    putanja = []
    busevi = []
    konacno = []
    nadjeno = 0

    @classmethod
    def trazi(cls, i, j, niz):
        niz.append(i)

        if i == j:
            cls.nadjeno = 1
            cls.putanja = niz[:]
            for i in cls.putanja:
                cls.busevi.append(stanice[i]["linije"])
            cls.fin_putanja(cls.putanja[0])

        else:

            pom = stanice[i]["susedi"]
            if Strategy2.krajnje[1][1] == "L":
                pom.reverse()

            for st in pom:
                if cls.nadjeno == 0:
                    if st not in niz:
                        cls.trazi(st, j, niz[:])

    @classmethod
    def fin_putanja(cls, poc):
        cls.konacno.append(poc)

        for i in range(0, len(cls.busevi) - 1):

            j = i + 1
            presek1 = []

            presek = list(set(cls.busevi[i]) & set(cls.busevi[j]))

            for x in presek:
                for y in linije:
                    if y[0] == x:
                        if (
                            abs(
                                y[1:].index(cls.putanja[i])
                                - y[1:].index(cls.putanja[j])
                            )
                            == 1
                        ):
                            presek1.append(x)

            cls.konacno.append(presek1)
            cls.konacno.append(cls.putanja[j])


class Strategy2:

    stan = []
    lin = []
    kolona = []
    krajnje = []
    nadjeno = 0
    k = 0

    @classmethod
    def trazi(cls, i, j):
        poc = i
        kraj = j
        cls.stan.append(poc)
        cls.kolona = [(poc, 0, "", 0)]
        while len(cls.kolona) != 0:

            tr, s, l, br = cls.kolona.pop(0)
            if kraj in cls.stan:
                cls.krajnje.append(cls.k)
                break
            c = 0

            for j in linije:
                if j[0] not in cls.lin:
                    if tr in j[1:]:
                        c += 1
                        cls.lin.append(j[0])
                        for x in j[(j.index(tr) - 1) : 0 : -1]:
                            if x not in cls.stan:
                                if x == kraj:
                                    cls.k = tuple([x, "L", j[0], br + 1])
                                    cls.nadjeno = 1
                                cls.stan.append(x)
                                t = tuple([x, "L", j[0], br + 1])
                                cls.kolona.append(t)

                        for x in j[(j.index(tr) + 1) : len(j)]:
                            if x not in cls.stan:
                                if x == kraj:
                                    cls.k = tuple([x, "D", j[0], br + 1])
                                    cls.nadjeno = 1
                                cls.stan.append(x)
                                t = tuple([x, "D", j[0], br + 1])
                                cls.kolona.append(t)

            if c != 0:
                cls.krajnje.append((tr, s, l, br))

        if cls.nadjeno:

            br = cls.k[3]
            for n in cls.krajnje:
                if n[3] >= br:
                    if n[0] != cls.k[0]:
                        cls.krajnje.remove(n)

            br -= 1
            tr = cls.k
            pom = 0
            while br > 0:

                for n in cls.krajnje:
                    if n[3] == br:
                        for l in linije:
                            if tr[2] == l[0]:
                                if n[0] not in l[1:]:
                                    cls.krajnje.remove(n)
                                else:
                                    pom = n

                tr = pom
                br -= 1
