def palindrom(slowo):
    slowo_duze = slowo.upper()
    for i in range(len(slowo_duze)):
        if slowo_duze[i] != slowo_duze[len(slowo_duze)-i-1]:
            return False
    return True

def wypisz(bool):
    if bool == False:
        print("Podane slowo nie jest palindromem")
    else:
        print("Podane slowo jest palindromem")

slowo = input("Podaj slowo do sprawdzenia czy jest palindromem: ")
wypisz(palindrom(slowo))

