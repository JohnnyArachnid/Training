tablica = [[4,5,6,4], [3,3, 2,7],[1, 1, 1, 1]]
lewyindex = 0
prawyindex = len(tablica[0]) - 1
pomocniczatablica = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def merge(tablica, lewyindex, pivot, prawyindex, pomocniczatablica,dlugosctablicy):
    for x in range(dlugosctablicy):
        for i in range(lewyindex, prawyindex+1):
            pomocniczatablica[x][i] = tablica[x][i]

        indexlewejstrony = lewyindex
        indexprawejstrony = pivot + 1
        index = lewyindex

        while indexlewejstrony <= pivot and indexprawejstrony <= prawyindex:
            if pomocniczatablica[x][indexlewejstrony] <= pomocniczatablica[x][indexprawejstrony]:
                tablica[x][index] = pomocniczatablica[x][indexlewejstrony]
                indexlewejstrony+=1
            else:
                tablica[x][index] = pomocniczatablica[x][indexprawejstrony]
                indexprawejstrony+=1
            index+=1

        while indexlewejstrony <= pivot:
            tablica[x][index] = tablica[x][index]
            tablica[x][index] = pomocniczatablica[x][indexlewejstrony]
            index+=1
            indexlewejstrony+=1

def mergeSort(tablica, lewyindex, prawyindex, pomocniczatablica):
    if lewyindex != prawyindex:
        dlugosctablicy = len(tablica)
        pivot = int((prawyindex+lewyindex)/2)
        mergeSort(tablica,lewyindex,pivot,pomocniczatablica)
        mergeSort(tablica,pivot+1,prawyindex,pomocniczatablica)
        merge(tablica,lewyindex,pivot,prawyindex,pomocniczatablica,dlugosctablicy)

def zamiana(tablica):
    rr = len(tablica)
    for n in range(rr):
        print(tablica[n][::])


mergeSort(tablica, lewyindex, prawyindex, pomocniczatablica)
zamiana(tablica)





