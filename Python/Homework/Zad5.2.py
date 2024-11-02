tab = [[11,22,33],[44,55,66],[77,88,99]]
lr = len(tab)
lc = len(tab[0])
s = 0
for x in range(lr):
    for y in range(lc):
        if tab[x][y] % 2 == 0 or tab[x][y] % 2 == 1:
            s+= tab[x][y]
        else:
            break
print(s)


































































