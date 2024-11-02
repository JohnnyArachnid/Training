x = int(input("Podaj liczbę całkowitą: "))
def funkcja(a):
    flaga = True
    for i in range(2, a):
        if a % i == 0:
            flaga = False
    return flaga
print(funkcja(x))
