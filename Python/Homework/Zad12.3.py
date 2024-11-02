tablica = []
lewyIndex = 0
dlugosc = int(input("Podaj dlugosc swojej tablicy do posortowania: "))
for index in range(dlugosc):
    print("Podaj nr.",index," swojej tablicy: ")
    n = int(input(""))
    tablica.append(n)
prawyIndex = len(tablica)-1
a = int(input("Podaj index pierwszego pivota: "))
tmp = tablica[a]
tablica[a] = tablica[len(tablica)-1]
tablica[len(tablica)-1] = tmp

def wyznaczPivot(tablica,lewyIndex,prawyIndex):
    granica = lewyIndex
    pivotIndex = prawyIndex
    for i in range(lewyIndex,prawyIndex):
        if tablica[i] < tablica[pivotIndex]:
            tmp = tablica[i]
            tablica[i] = tablica[granica]
            tablica[granica] = tmp
            granica+=1

    zmianaPivot = tablica[granica]
    tablica[granica] = tablica[pivotIndex]
    tablica[pivotIndex] = zmianaPivot
    return granica

def quickSort(tablica,lewyIndex,prawyIndex):
    if lewyIndex < prawyIndex:
        pivotIndex = wyznaczPivot(tablica, lewyIndex, prawyIndex)
        quickSort(tablica,lewyIndex,pivotIndex - 1)
        quickSort(tablica,pivotIndex + 1,prawyIndex)

quickSort(tablica,lewyIndex,prawyIndex)
print(tablica)