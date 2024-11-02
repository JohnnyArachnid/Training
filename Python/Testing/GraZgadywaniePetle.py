flaga = True
print("Witaj w grze zgadywanie, Twoim zadaniem jest zgadniecie liczby od 0 do 9, masz 3 szanse, Powodzenia!")
liczba = 8
zycia = 3
while flaga:
    decyzja = int(input(("Podaj liczbę do zganięcia: ")))
    if zycia != 0:
        if decyzja != liczba:
            zycia-=1
            print("Nie trafiles sprobuje ponownie")
        else:
            print("Wygrales :0")
            flaga = False
    else:
        print("Przegrales :(")
        flaga = False

