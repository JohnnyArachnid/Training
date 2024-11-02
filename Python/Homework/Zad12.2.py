tablica = []
lewyIndex = 0
dlugosc = int(input("Podaj dlugosc swojej tablicy do posortowania: "))
for index in range(dlugosc):
    print("Podaj nr.",index," swojej tablicy: ")
    n = str(input(""))
    while len(n) != 1:
        print("Podaj nr.",index," swojej tablicy jeszcze raz: ")
        n = str(input(""))
    tablica.append(n)
for index in range(len(tablica)):
    a = tablica[index].upper()
    tablica[index] = a
prawyIndex = len(tablica)-1

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
def zamianaNaAscii(tablica):
    for i in range(len(tablica)):
        a = ord(tablica[i])
        tablica[i] = a
def zamianaNaLitery(tablica):
    for i in range(len(tablica)):
        a = chr(tablica[i])
        tablica[i] = a

zamianaNaAscii(tablica)
quickSort(tablica,lewyIndex,prawyIndex)
zamianaNaLitery(tablica)
print(tablica)

