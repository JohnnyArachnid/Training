def deszyfrowaniePlotkowe(tekst,k):
    duze = ""
    wynik = ""
    plotek = []
    for i in tekst:
        a = i.upper()
        duze+=a

    for i in range(k):
        plotek.append([])

    for i in range(k):
        for j in range(len(duze)):
            plotek[i].append("")

    wDol = True
    wiersz = 0

    for i in range(len(duze)):
        plotek[wiersz][i] = "X"
        if wDol == True and wiersz != k-1:
            wiersz = wiersz + 1
        elif wDol == True and wiersz == k-1:
            wiersz = wiersz - 1
            wDol = False
        elif wDol == False and wiersz != 0:
            wiersz = wiersz - 1
        elif wDol == False and wiersz == 0:
            wiersz = wiersz + 1
            wDol = True

    indexSzyfrogramu = 0

    for i in range(k):
        for j in range(len(duze)):
            if plotek[i][j] == "X":
                plotek[i][j] = duze[indexSzyfrogramu]
                indexSzyfrogramu+=1

    wDol = True
    wiersz = 0

    for i in range(len(duze)):
        wynik+=plotek[wiersz][i]
        if wDol == True and wiersz != k-1:
            wiersz = wiersz + 1
        elif wDol == True and wiersz == k-1:
            wiersz = wiersz - 1
            wDol = False
        elif wDol == False and wiersz != 0:
            wiersz = wiersz - 1
        elif wDol == False and wiersz == 0:
            wiersz = wiersz + 1
            wDol = True
    return wynik


tekst = str(input("Podaj tekst do deszyfrowania: "))
k = int(input("Podaj wartość klucza do zaszyfrowania tekstu: "))
while k < 2 or k >= len(tekst):
    k = int(input("Podaj wartość klucza do zaszyfrowania tekstu: "))
print(deszyfrowaniePlotkowe(tekst,k))
