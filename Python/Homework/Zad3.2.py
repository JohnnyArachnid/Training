import math
x = int(input("Podaj liczbę rzeczywistą: "))
tab = []
while x > 0:
    cyfra = x % 10
    cyfra = cyfra ** 2
    tab.append(cyfra)
    x = math.floor(x / 10)
print(tab[::-1])





