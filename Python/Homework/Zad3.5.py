a = ["a", "ą", "b", "c", "ć", "d", "e", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
A = ["A", "Ą", "B", "C", "Ć", "D", "E", "F", "G", "H", "I", "J", "K", "L", "Ł", "M", "N", "Ń", "O", "Ó", "P", "R", "S", "Ś", "T", "U", "W", "Y", "Z", "Ź", "Ż"]
d = 0
print("Witam w wyświetlaczu alfabetu\nPodaj nr.1 jeżeli chcesz wyświetlić literki małe\nPodaj nr.2 jeżeli chcesz wyświetlić duże literki\nPodaj nr.3 jak chcesz wyświetlić oba")
x = int(input("Podaj numer: "))
if x == 1:
    n = int(input("Podaj liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while n <= 0:
        n = int(input("Podaj liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while d < n:
        if d < 31:
            print(a[d])
            d+=1
        else:
            break
if x == 2:
    n = int(input("Podaj liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while n <= 0:
        n = int(input("Podaj liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while d < n:
        if d < 31:
            print(A[d])
            d+=1
        else:
            break
if x == 3:
    n = int(input("Podaj liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while n <= 0:
         n = input(int("Podaj ponownie liczbę liter alfabetu jaką chcesz wyświetlić: "))
    while d < n:
        if d < 31:
            print(a[d],A[d], sep=" ")
            d += 1
        else:
            break








