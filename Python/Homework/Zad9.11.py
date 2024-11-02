a = int(input("Podaj stopień wielomianu: "))
d = int(input("Podaj wartość do wstawienia do wielomianu: "))
b = 0
tab = []
while a > b:
    c = int(input("Podaj kolejne współczynniki wielomianu począwszy od najwyższej potęgi: "))
    tab.append(c)
    b+=1
suma = 0
for index in range(len(tab)):
    suma+=tab[index] * (d ** (a - index))
print(suma)


