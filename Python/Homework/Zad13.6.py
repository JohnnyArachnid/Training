def szyfrowaniePlotkowe(tekst,k):
    duze = ""
    wynik = ""
    plotek = []
    for i in tekst:
        a = i.upper()
        duze+=a

    for i in range(k):
        plotek.append([])

    wDol = True
    wiersz = 0

    for i in range(k):
        for j in range(len(duze)):
            plotek[i].append("")

    for i in range(len(duze)):
        plotek[wiersz][i] = duze[i]
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

    for i in range(k):
        for j in range(len(duze)):
            wynik+=plotek[i][j]
    return wynik

tekst = str(input("Podaj tekst do zaszyfrowania: "))
k = int(input("Podaj wartość klucza do zaszyfrowania tekstu: "))
while k < 2 or k >= len(tekst):
    k = int(input("Podaj wartość klucza do zaszyfrowania tekstu: "))
print(szyfrowaniePlotkowe(tekst,k))
