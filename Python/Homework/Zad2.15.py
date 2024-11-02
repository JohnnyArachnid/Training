n = str(input("Podaj liczbę naturalną: "))
dlugosc = len(n)
suma = 0
wynik ="0"
for i in n:
    a = n[dlugosc - 1]
    suma += int(a) ** 2
    wynik+=str(suma)
    dlugosc = dlugosc - 1
    suma = 0
print(n,"drukujemy",wynik.replace("0", ""))
