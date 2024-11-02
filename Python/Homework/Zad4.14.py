a = int(input("Podaj liczbę do spotęgowania: "))
b = int(input("Podaj wykładnik potęgi: "))
while a < 0:
    a = int(input("Podaj liczbę do spotęgowania: "))
def power1 (x,y):
    tab = []
    for i in range(1,y+1):
        x = x ** i
        tab.append(x)
    tab.reverse()
    return tab[0]
print(power1(a,b))



































































