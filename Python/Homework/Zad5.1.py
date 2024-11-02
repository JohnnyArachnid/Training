tab1 = []
for i in range(5):
    a = int(input("Podaj liczbę całkowitą parzystą: "))
    while a % 2 != 0:
        a = int(input("Podaj liczbę całkowitą parzystą raz jeszcze: "))
    tab1.append(a)
tab2= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = len(tab2)
y = len(tab2[0])
for ix in range(x):
    for iy in range(y):
        tab2[ix][iy] = tab1[iy]
print(tab2)



































































