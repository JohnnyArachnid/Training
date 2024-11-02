number = 0
while(number < 3 or number > 10000):
    number = int(input("Podaj liczbę elementów tablicy: ")) #number -> długość tablicy

moves = 0
while(moves > number or moves < 2):
    moves = int(input("Podaj liczbę przesunięć tablicy: "))

table = []

for i in range(number):
    table.append(input("Podaj liczbę do tablicy: "))

for i in range(moves):
    table.insert(0, table[number - 1])
    table.pop()
print(table)









