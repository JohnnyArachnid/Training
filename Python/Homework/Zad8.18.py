def ZamianaNaDecymalny(napis,system):
    dec = 0
    for i in range(len(napis)):
        if ord(napis[i]) >= 65:
            liczba = ord(napis[i]) -55
        else:
            liczba = int(napis[i])
        power = len(napis) - 1 - i
        dec = dec + liczba * (system ** power)
    return dec
wartosc = input("Podaj liczbę: ")
system = int(input("Podaj system liczbowy dla wartości: "))
print(ZamianaNaDecymalny(wartosc,system))
