def pierwsza(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
tab = [[11,22,33],[44,55,66],[101,88,99]]
x = len(tab)
y = len(tab[0])
maksi = tab[0][0]
for a in range(x):
    for b in range(y):
        if pierwsza(tab[a][b]) == True:
            print("Liczba ", tab[a][b], " jest pierwsza")































































