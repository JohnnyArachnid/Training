n = int(input("Podaj liczbę do wyliczenia silni: "))
def funckja (a):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
print(funckja(n))


































































