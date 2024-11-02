def szyfrowaniePrzestawne(tekst):
    duze = ""
    wynik = ""
    for i in tekst:
        a = i.upper()
        duze+=a
    for i in range(0, len(duze)-1, 2):
        wynik+=duze[i+1]
        wynik+=duze[i]
    if len(duze)%2 == 1:
        wynik+=duze[len(duze)-1]
    return wynik

tekst = str(input("Podaj tekst do zaszyfrowania: "))
print(szyfrowaniePrzestawne(tekst))