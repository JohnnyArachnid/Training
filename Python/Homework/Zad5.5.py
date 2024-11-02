tab1 = [[11,22,33],[44,55,66],[77,88,99]]
tab2 = []
lr = len(tab1)
lc = len(tab1[0])
s = 0
for x in range(lr):
    for y in range(lc):
        s+=tab1[x][y]
    tab2.append(s)
    s = 0
print(tab2, sep=" ")

































































