def liczbadoskonala(x):
    tab = []
    suma = 0
    for i in range(1,x):
        if x % i == 0:
            tab.append(i)
            suma+=i
        else:
            continue
    if x != suma:
        return False
    return True

a = int(input("Podaj liczbę: "))
print(liczbadoskonala(a))

