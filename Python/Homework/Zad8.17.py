def zamiananabinarny(x):
    liczba = ""
    while x>0:
        liczba+=str(x%2)
        x = int(x/2)
    return liczba[::-1]
wartosc = int(input("Podaj liczbę w systemie dziesiętnym: "))
print("Twoja liczba po zamianie na binarny wynosi:", zamiananabinarny(wartosc))
