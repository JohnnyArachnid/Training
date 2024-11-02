def liczbapierwsza(a):
    if a == 1:
        return False
    for liczba in range(2, a):
        if a % liczba == 0:
            return False
    return True
słownik = {}
n = int(input("Podaj długość słownika: "))
for i in range(1,n+1):
    słownik[i] = liczbapierwsza(i)
print(słownik)





































































