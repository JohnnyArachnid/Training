def silnia(x):
    silnia = 1
    for liczba in range(1,x+1):
        silnia*=liczba
    return silnia
a = int(input("Podaj wartość silni do obliczenia: "))
print(silnia(a))


