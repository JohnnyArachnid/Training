def NWD(x,y):
    if y > 0:
        return NWD(y, x%y)
    return x

a = int(input("Podaj wartość liczby pierwszej: "))
b = int(input("Podaj wartość liczby drugiej: "))
print(NWD(a,b))


