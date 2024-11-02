a = int(input("Podaj liczbę do spotęgowania: "))
b = int(input("Podaj wykładnik potęgi: "))
while a < 0:
    a = int(input("Podaj liczbę do spotęgowania: "))
def power3 (x,y):
    if y < 1:
        return 1
    if y % 2 == 0:
        return int((x**(y/2))**2)
    else:
        return int((x**(y/2))**2)
print(power3(a,b))



































































