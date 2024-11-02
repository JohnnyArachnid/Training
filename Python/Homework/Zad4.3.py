a = int(input("Podaj pierwszą liczbę do sprawdzenia: "))
b = int(input("Podaj pierwszą liczbę do sprawdzenia: "))
c = int(input("Podaj pierwszą liczbę do sprawdzenia: "))
def funkcja(x,y,z):
    return (x >= 13 and x <= 19) or (y >= 13 and y <= 19) or (z >= 13 and z <= 19)
print(funkcja(a,b,c))