def NWD(x,y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

a = int(input("Podaj wartość liczby pierwszej: "))
b = int(input("Podaj wartość liczby drugiej: "))
print(NWD(a,b))
