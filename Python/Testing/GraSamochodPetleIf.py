flaga = True
czy_samochod_uruchomiony = False
help = '''start - uruchomienie pojazdu
stop - wylaczenie pojazdu
quit - wyjscie z pojazdu'''
while flaga:
    decyzja = input("").upper()
    if decyzja == "HELP":
        print(help)
    elif decyzja == "QUIT" and czy_samochod_uruchomiony == False:
        break
    elif decyzja == "QUIT" and czy_samochod_uruchomiony == True:
        print("Nie mozesz wyjsc z wlaczonego samochodu, musisz go na poczatku wylaczyc")
    elif decyzja == "STOP":
        czy_samochod_uruchomiony = False
        print("Samochod wylaczony")
    elif decyzja == "START":
        czy_samochod_uruchomiony = True
        print("Samochod uruchomiony")
    else:
        print("Nie rozumiem podanej instruckji :(")



