a = input("Podaj znak do wypisania: ")
n = int(input("Podaj liczbę znaków do wypisania: "))
l = len(a)
while l != 1:
    a = input("Podaj ponownie znak do wypisania: ")
while n < 0:
    n = int(input("Podaj ponownie liczbę znaków do wypisania: "))
def writeLine (x,y):
    if y == 0:
        return 0
    if y == 1:
        return x
    return x*y
print(writeLine(a,n))



































































