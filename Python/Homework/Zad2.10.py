a = int(input("Podaj liczbę naturalną: "))
i = 1
while i < a:
    if a % i == 0:
        print(i)
    i+=1
