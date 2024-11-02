def NWD(x,y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

def NWW(z,c):
    return int((z*c)/NWD(z,c))

a = int(input("Podaj wartość liczby pierwszej: "))
b = int(input("Podaj wartość liczby drugiej: "))
print(NWW(a,b))


