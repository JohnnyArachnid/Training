number = 0
while(number < 3 or number > 10000):
    number = int(input("Podaj liczbę elementów tablicy: "))

moves = 0
while(moves > number or moves < 2):
    moves = int(input("Podaj liczbę przesunięć tablicy: "))

table = []

for i in range(number):
    table.append(input("Podaj liczbę do tablicy: "))

for i in range(moves):
    table.append(table[0])
    table.remove(table[0])

print(table)









