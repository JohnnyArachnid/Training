def deszyfrowanieCezara(tekst,k):
    duze = ""
    for i in tekst:
        a = i.upper()
        duze += a
    wynik = ""
    if k > 0:
        x = k % 26
        for i in range(len(duze)):
            if ord(duze[i])-x < 65:
                b = chr(ord(duze[i])-x+26)
                wynik+=b
            else:
                c = chr(ord(duze[i])-x)
                wynik+=c
    else:
        x = k % -26
        for i in range(len(duze)):
            if ord(duze[i])-x > 90:
                b = chr(ord(duze[i])-x-26)
                wynik+=b
            else:
                c = chr(ord(duze[i])-x)
                wynik+=c
    return wynik

tekst = str(input("Podaj tekst do zaszyfrowania: "))
k = int(input("Podaj klucz do szyfru: "))
print(deszyfrowanieCezara(tekst,k))
