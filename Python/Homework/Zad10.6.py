def najwiekszaliczba(tablica):
    najwieksza = tablica[0]
    for i in range(len(tablica)):
        if tablica[i] > najwieksza:
            najwieksza = tablica[i]
    return najwieksza

def sortowaniekubelkowe(tablice):
    tablicapomocnicza = []
    c = najwiekszaliczba(tablice)
    for l in range(c+1):
        tablicapomocnicza.append(0)
    for k in range(len(tablice)):
        tablicapomocnicza[tablice[k]] = tablicapomocnicza[tablice[k]] + 1
    index = 0
    for j in range(c+1):
        if tablicapomocnicza[j] > 0:
            for numer in range(tablicapomocnicza[j]):
                tablice[index] = j
                index+=1
    return tablice

a = int(input("Podaj ilość elementów dla twojej tablicy: "))
tab = []
for index in range(a):
    print("Podaj wartość nr.", index, "dla twojej tablicy: ")
    b = int(input())
    tab.append(b)
print(sortowaniekubelkowe(tab))