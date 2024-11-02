def liczbadoskonala(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    if suma == n:
        return True
    return False

x = int(input("Podaj liczbe do sprawdzenia czy doskonala: "))
if liczbadoskonala(x) == True:
    print("Liczba jest doskonala")
else:
    print("Liczba nie jest doskonala")