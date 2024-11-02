tab = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = len(tab)
y = len(tab[0])
n = 1
for a in range(x):
    for b in range(y):
        tab[a][a] = n**2
    n+=1
print(tab)

































































