def sortowanko_babelkowe(tablica):
    for j in range(len(tablica)-1):
        for i in range(len(tablica)-1):
            if tablica[i+1] < tablica[i]:
                tablica[i],tablica[i+1] = tablica[i+1],tablica[i]
tablica = [9,8,7,6,5]
sortowanko_babelkowe(tablica)
print(tablica)
