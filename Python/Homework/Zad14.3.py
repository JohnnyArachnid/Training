def deszyfrowanieVinegere(tekst,klucz):
    wynik = ""
    tekst1 = ""
    klucz1 = ""
    tablica = []
    while len(klucz) < len(tekst):
        klucz+=klucz
    for i in range(len(tekst)):
        a = tekst[i].upper()
        b = klucz[i].upper()
        tekst1+=a
        klucz1+=b
    for j in range(26):
        tablica.append([])
    for j in range(26):
        alfabet = 65 + j
        for i in range(26):
            if alfabet > 90:
                alfabet = 65
                tablica[j].append(chr(alfabet))
                alfabet += 1
            else:
                tablica[j].append(chr(alfabet))
                alfabet+=1
    index = 0
    for i in range(len(tekst1)):
        kolumna = ord(klucz1[i]) - 65
        for j in range(26):
            if tablica[kolumna][j] == tekst1[i]:
                wynik+=chr(j+65)
    return wynik

tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = str(input("Podaj klucz do zaszyfrowania tekstu: "))
print(deszyfrowanieVinegere(tekst,klucz))
