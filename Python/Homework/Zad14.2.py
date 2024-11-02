def szyfrVinegere(tekst,klucz):
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
    for i in range(len(tekst1)):
        literaKlucza = ord(klucz1[i])
        literaTekstu = ord(tekst1[i])
        szukanaKolumna = literaKlucza - 65
        szukanyWiersz = literaTekstu - 65
        wynik+=tablica[szukanaKolumna][szukanyWiersz]
    return wynik
tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = str(input("Podaj klucz do zaszyfrowania tekstu: "))
print(szyfrVinegere(tekst,klucz))
