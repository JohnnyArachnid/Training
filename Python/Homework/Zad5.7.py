tab = [[11,22,33],[44,55,66],[101,88,99]]
x = len(tab)
y = len(tab[0])
maksi = tab[0][0]
for a in range(x):
    if tab[a][a] > maksi:
        maksi = tab[a][a]
    for b in range(y):
        if tab[a][x-1-a] > maksi:
            maksi = tab[a][x-1-a]
print(maksi)































































