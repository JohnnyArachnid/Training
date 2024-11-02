tablica = [[4,5,6,4], [3,3, 2,7],[1, 1, 1, 1]]
pomocniczatablica = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
pomocniczatablica1 = [0,0,0,0,0,0,0,0,0,0,0,0]
pomocniczatablica2 = [0,0,0,0,0,0,0,0,0,0,0,0]
lewyindex = 0
prawyindex = len(pomocniczatablica1) - 1
def jd(tablica,tablicapomocnicza):
    x = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[0])):
            tablicapomocnicza[x] = tablica[i][j]
            x+=1

def merge(tablica, lewyindex, pivot, prawyindex, pomocniczatablica):
        for i in range(lewyindex, prawyindex+1):
            pomocniczatablica[i] = tablica[i]

        indexlewejstrony = lewyindex
        indexprawejstrony = pivot + 1
        index = lewyindex

        while indexlewejstrony <= pivot and indexprawejstrony <= prawyindex:
            if pomocniczatablica[indexlewejstrony] <= pomocniczatablica[indexprawejstrony]:
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

def zamiana(tablica, pomocniczatablica1):
    x = 0
    rr = len(pomocniczatablica1)
    rc = len(pomocniczatablica1[0])
    for n in range(rr):
        for i in range(rc):
            pomocniczatablica1[n][i] = tablica[x]
            x+=1
    for y in range(rr):
        print(pomocniczatablica1[y][::])

jd(tablica,pomocniczatablica1)
mergeSort(pomocniczatablica1, lewyindex, prawyindex, pomocniczatablica2)
zamiana(pomocniczatablica1,pomocniczatablica)





