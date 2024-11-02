a = int(input("Podaj liczbę do spotęgowania: "))
while a < 0:
    a = int(input("Podaj liczbę do spotęgowania: "))
def power3 (x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return power3(x-1) + power3(x - 2)
print(power3(a))



































































