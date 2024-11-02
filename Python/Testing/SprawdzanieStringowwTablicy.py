lista1 = ["Czerwony", "Zielony", "Zółty"]
lista2 = ["Czerwony","Zółty"]
lista3 = []
if len(lista1) > len(lista2):
    dlugosc = len(lista1)
    nr = 1
else:
    dlugosc = len(lista2)
    nr = 2
if nr == 1:
    for i in range(len(lista1)):
        if lista1[i] in lista2 != True:
            continue
        else:
            lista3.append(lista1[i])
else:
    for i in range(len(lista2)):
        if lista2[i] in lista1 != True:
            continue
        else:
            lista3.append(lista2[i])
print(lista3)
