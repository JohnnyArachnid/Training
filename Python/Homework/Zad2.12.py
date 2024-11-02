a = input("Podaj liczbę naturalną: ")
suma = ""
for i in a:
    if int(i) % 2 == 1:
        suma+=i
print(suma)