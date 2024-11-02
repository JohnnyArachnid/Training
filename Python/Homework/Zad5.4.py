tab = [[11,22,33],[44,55,66],[77,88,99]]
lr = len(tab)
lc = len(tab[0])
Maksi = tab[0][0]
Minii = tab[0][0]
for x in range(lr):
    for y in range(lc):
        if tab[x][y] > Maksi:
            Maksi=tab[x][y]
        elif tab[x][y] < Minii:
            Minii = tab[x][y]
print(Maksi, Minii)