def poPrawej(macierz, indexWierszaLitera1, indexKolumnyLitera1, indexKolumnyLitera2):
    if indexKolumnyLitera1 + 1 == 5:
        indexKolumnyLitera1 = -1
    if indexKolumnyLitera2 + 1 == 5:
        indexKolumnyLitera2 = -1
    szyfrowanaLitera1 = macierz[indexWierszaLitera1][indexKolumnyLitera1 + 1]
    szyfrowanaLitera2 = macierz[indexWierszaLitera1][indexKolumnyLitera2 + 1]

    return szyfrowanaLitera1+szyfrowanaLitera2

def wDol(macierz, indexKolumnyLitera1, indexWierszaLitera1, indexWierszaLitera2):
    if indexWierszaLitera1 + 1 == 5:
        indexWierszaLitera1 = -1
    if indexWierszaLitera2 + 1 == 5:
        indexWierszaLitera2 = -1
    szyfrowanaLitera1 = macierz[indexKolumnyLitera1][indexWierszaLitera1 + 1]
    szyfrowanaLitera2 = macierz[indexKolumnyLitera1][indexWierszaLitera2 + 1]

    return szyfrowanaLitera1 + szyfrowanaLitera2

def Rozne(macierz, indexKolumnyLitera1, indexKolumnyLitera2, indexWierszaLitera1, indexWierszaLitera2):
    szyfrowanaLitera1 = macierz[indexWierszaLitera2][indexKolumnyLitera1]
    szyfrowanaLitera2 = macierz[indexWierszaLitera1][indexKolumnyLitera2]
    return szyfrowanaLitera1 + szyfrowanaLitera2

def znajdźWiersz(macierz,litera):
    for j in range(5):
        for i in range(5):
            if macierz[j][i] == litera:
                return j
    return "JD"

def znajdźKolumne(macierz,litera):
    for j in range(5):
        for i in range(5):
            if macierz[j][i] == litera:
                return i
    return "JD"

def szyfrowaniePara(macierz,litera1,litera2):
    indexWierszaLitera1 = znajdźWiersz(macierz,litera1)
    indexWierszaLitera2 = znajdźWiersz(macierz,litera2)
    indexKolumnyLitera1 = znajdźKolumne(macierz,litera1)
    indexKolumnyLitera2 = znajdźKolumne(macierz,litera2)
    if indexWierszaLitera1 == indexWierszaLitera2:
        return poPrawej(macierz, indexWierszaLitera1, indexKolumnyLitera1, indexKolumnyLitera2)
    if indexKolumnyLitera1 == indexKolumnyLitera2:
        return wDol(macierz, indexKolumnyLitera1, indexWierszaLitera1, indexWierszaLitera2)
    if indexWierszaLitera1 != indexWierszaLitera2 and indexKolumnyLitera1 != indexKolumnyLitera2:
        return Rozne(macierz, indexKolumnyLitera1, indexKolumnyLitera2, indexWierszaLitera1, indexWierszaLitera2)
    return "JD"

def sprMacierzLitera(macierz,litera):
    for j in range(5):
        for i in range(5):
            if macierz[j][i] == litera:
                return True
    return False

def pobranieLiteraMacierz(macierz):
    for i in range(65, 91):
        litera = chr(i)
        if sprMacierzLitera(macierz,litera) == False and litera != "J":
            return litera
    return "JD"

def pobierzBezDuplikatow(text):
    wynik = ""
    for index in range(len(text)):
        if wynik.find(text[index]) == -1:
            wynik+=text[index]
    return wynik

def szyfrowaniePlayFair(tekst,klucz):
    wynik = ""
    tekst1 = ""
    klucz1 = ""

    for i in range(len(tekst)):
        a = tekst[i].upper()
        tekst1 += a

    for i in range(len(klucz)):
        b = klucz[i].upper()
        klucz1 += b

    tablica = [[],[],[],[],[]]
    for j in range(5):
        for i in range(5):
            tablica[j].append("")

    nowyklucz = pobierzBezDuplikatow(klucz1)

    indexklucza = 0
    for j in range(5):
        for i in range(5):
            if indexklucza < len(nowyklucz):
                tablica[j][i] = nowyklucz[indexklucza]
                indexklucza+=1
            else:
                tablica[j][i] = pobranieLiteraMacierz(tablica)

    for i in range(0, len(tekst1) - 1, 2):
        wynik+=szyfrowaniePara(tablica, tekst1[i],tekst1[i+1])

    if len(tekst1) % 2 == 1:
        wynik += tekst1[len(tekst1) - 1]
    return wynik

tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = str(input("Podaj klucz do zaszyfrowania: "))
print(szyfrowaniePlayFair(tekst,klucz))