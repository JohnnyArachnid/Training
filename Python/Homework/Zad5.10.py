tab = [[1,2,3],[4,5,6],[7,8,9]]
tab1 = [[0,0,0],[0,0,0],[0,0,0]]
x = len(tab)
y = len(tab[0])
for a in range(x):
    for b in range(y):
        tab1[b][x - 1 - a] = tab[a][b]
print(tab1)
































































