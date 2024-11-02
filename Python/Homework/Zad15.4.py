def bezSpacji(tekst):
    wynik = ""
    for i in range(len(tekst)):
        wynik+=tekst[i].replace(" ","")
    return wynik
def duzeLitery(tekst):
    wynik=""
    for i in range(len(tekst)):
        a = tekst[i].upper()
        wynik+=a
    return wynik
def przesuniecieWierszy(tablica,klucz):
    tablicaPom = []
    for i in range(len(tablica)):
        tablicaPom.append("")
    for i in range(len(tablica)):
        if klucz > len(tablica):
            klucz = klucz % len(tablica)
            if klucz+i >= len(tablica):
                tablicaPom[i+klucz-len(tablica)] = tablica[i]
            else:
                tablicaPom[i + klucz] = tablica[i]
        else:
            if klucz+i >= len(tablica):
                tablicaPom[i+klucz-len(tablica)] = tablica[i]
            else:
                tablicaPom[i + klucz] = tablica[i]
    return tablicaPom

def doTablicy(tekst):
    tablica = []
    for i in range(len(tekst)):
        tablica.append(tekst[i])
    return tablica
def Szyfr(macierz,klucz):
    tablica = []
    for i in range(klucz):
        tablica.append([])
    for j in range(klucz):
        for i in range(klucz):
            tablica[j].append("-")
    indexMacierz=0
    for j in range(klucz):
        for i in range(klucz):
            if indexMacierz < len(macierz):
                tablica[j][i] = macierz[indexMacierz]
                indexMacierz+=1
    return tablica

tekstJawny = str(input("Podaj tekst do zaszyfrowania: "))
klucz1 = int(input("Podaj pierwszą cyfrę klucza: "))
klucz2 = int(input("Podaj drugą cyfrę klucza: "))
tekstJawny = bezSpacji(tekstJawny)
tekstJawny = duzeLitery(tekstJawny)
tablica = doTablicy(tekstJawny)
tekstJawnyPrzesuniety = przesuniecieWierszy(tablica,klucz2)
wynik = Szyfr(tekstJawnyPrzesuniety, klucz1)
print(wynik)