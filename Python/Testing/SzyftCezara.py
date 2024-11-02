def cezar_szyfrowanie(tekst,klucz):
    tekst_zaszyfrowany = ""
    klucz%=26
    for litera in range(len(tekst)):
        if ord(tekst[litera]) >= 65 and ord(tekst[litera]) <= 90:
            if ord(tekst[litera]) + klucz >= 90:
                nadmiarowosc = ord(tekst[litera]) + klucz - 90
                tekst_zaszyfrowany += chr(65+nadmiarowosc)
            else:
                tekst_zaszyfrowany += chr(ord(tekst[litera])+klucz)
        elif ord(tekst[litera]) >= 97 and ord(tekst[litera]) <= 122:
            if ord(tekst[litera]) + klucz >= 122:
                nadmiarowosc = ord(tekst[litera]) + klucz - 122
                tekst_zaszyfrowany += chr(97+nadmiarowosc)
            else:
                tekst_zaszyfrowany += chr(ord(tekst[litera])+klucz)
        else:
            continue
    return tekst_zaszyfrowany

def cezar_deszyfrowanie(tekst_zaszyfrowany,klucz):
    tekst_deszyfrowany = ""
    klucz %= 26
    for litera in range(len(tekst_zaszyfrowany)):
        if ord(tekst_zaszyfrowany[litera]) >= 65 and ord(tekst_zaszyfrowany[litera]) <= 90:
            if ord(tekst_zaszyfrowany[litera]) - klucz <= 65:
                nadmiarowosc = abs(ord(tekst_zaszyfrowany[litera]) - klucz - 65)
                tekst_deszyfrowany += chr(90 - nadmiarowosc)
            else:
                tekst_deszyfrowany += chr(ord(tekst_zaszyfrowany[litera]) - klucz)
        elif ord(tekst_zaszyfrowany[litera]) >= 97 and ord(tekst_zaszyfrowany[litera]) <= 122:
            if ord(tekst_zaszyfrowany[litera]) - klucz <= 97:
                nadmiarowosc = abs(ord(tekst_zaszyfrowany[litera]) - klucz - 97)
                tekst_deszyfrowany += chr(122 - nadmiarowosc)
            else:
                tekst_deszyfrowany += chr(ord(tekst_zaszyfrowany[litera]) - klucz)
        else:
            continue
    return tekst_deszyfrowany

tekst_przed_szyfrowaniem = input("Podaj slowo do zaszyfrowania: ")
klucz = int(input("Podaj klucz do zaszyfrowania: "))
print("Slowo przed zaszyforwaniem: ",tekst_przed_szyfrowaniem)
print("Tekst po szyfrowaniu: ",cezar_szyfrowanie(tekst_przed_szyfrowaniem,klucz))
print("Tekst po deszyfrowaniu: ",cezar_deszyfrowanie(cezar_szyfrowanie(tekst_przed_szyfrowaniem,klucz),klucz))
