tab = [[11,22,33],[44,55,66],[77,88,99]]
x = len(tab)
y = len(tab[0])
tab1 = []
s = 0
for a in range(x):
    for b in range(y):
        s+=tab[b][a]
    tab1.append(s)
    s = 0
print(tab1)
































































