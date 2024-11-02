a = int(input("Ile liczb chcesz sprawdzić: "))
for i in range(a):
    x = int(input("Podaj liczbe: "))
    flaga = True
    for j in range(2, x):
        if (x % j == 0):
            flaga = False
            break
    print(x, " nie jest pierwsza") if (flaga == False) else print(x, " jest pierwsza")










