def NWD(x,y):
    if y > 0:
        return NWD(y, x%y)
    return x
def NWW(z,c):
    return int((z*c)/NWD(z,c))

a = int(input("Podaj wartość liczby pierwszej: "))
b = int(input("Podaj wartość liczby drugiej: "))
print(NWW(a,b))


