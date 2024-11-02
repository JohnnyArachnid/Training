def silnia(x):
    if x == 1:
        return 1
    return x*silnia(x-1)
a = int(input("Podaj wartość silni do obliczenia: "))
print(silnia(a))