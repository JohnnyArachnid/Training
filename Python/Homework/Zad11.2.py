a = int(input("Podaj długość swojej tablicy: "))
tablica = []
for i in range(a):
    print("Podaj znak nr.",i+1,"swojej tablicy:")
    b = str(input())
    tablica.append(b)
pomocniczatablica = [0]*(len(tablica))
lewyindex = 0
prawyindex = len(tablica) - 1
def merge(tablica, lewyindex, pivot, prawyindex, pomocniczatablica):
    for i in range(lewyindex, prawyindex+1):
        pomocniczatablica[i] = tablica[i]

    indexlewejstrony = lewyindex
    indexprawejstrony = pivot + 1
    index = lewyindex

    while indexlewejstrony <= pivot and indexprawejstrony <= prawyindex:
        if pomocniczatablica[indexlewejstrony] >= pomocniczatablica[indexprawejstrony]:
            tablica[index] = pomocniczatablica[indexlewejstrony]
            indexlewejstrony+=1
        else:
            tablica[index] = pomocniczatablica[indexprawejstrony]
            indexprawejstrony+=1
        index+=1

    while indexlewejstrony <= pivot:
        tablica[index] = tablica[index]
        tablica[index] = pomocniczatablica[indexlewejstrony]
        index+=1
        indexlewejstrony+=1

def mergeSort(tablica, lewyindex, prawyindex, pomocniczatablica):
    if lewyindex != prawyindex:
        pivot = int((prawyindex+lewyindex)/2)
        mergeSort(tablica,lewyindex,pivot,pomocniczatablica)
        mergeSort(tablica,pivot+1,prawyindex,pomocniczatablica)
        merge(tablica,lewyindex,pivot,prawyindex,pomocniczatablica)
def zamiana(tablica):
    for i in range(len(tablica)):
        if ord(tablica[i]) >= 97:
            tablica[i] = ord(tablica[i]) - 32
        else:
            tablica[i] = ord(tablica[i])
    for i in range(len(tablica)):
        tablica[i] = chr(tablica[i])
    return tablica

zamiana(tablica)
mergeSort(tablica, lewyindex, prawyindex, pomocniczatablica)
print(tablica)