x = int(input("Podaj podstawę potęgi: "))
n = int(input("Podaj wykładnik potęgi: "))
def funckja (a,b):
    tab = []
    for i in range(0,b+1):
        tab.append(a**i)
    tab.reverse()
    return tab[0]
print(funckja(x,n))


































































