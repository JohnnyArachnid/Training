n = input("Podaj liczbę naturalną: ")
flaga = True
for i in range(2, int(n)):
    if int(n) % i == 0:
        flaga = False
        break
if flaga == True:
    print("Twoja liczba jest pierwsza")
else:
    print("Twoja liczba nie jest pierwsza")

