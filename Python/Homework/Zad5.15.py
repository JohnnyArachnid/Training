tab = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = len(tab)
y = len(tab[0])
for a in range(x):
    for b in range(y):
        tab[a][x-1-a] = x*2**a
print(tab)

































































