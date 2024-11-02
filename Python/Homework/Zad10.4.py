def sortowaniePrzezWybor(x):
    for i in range(len(x)-1):
        startowyIndex = i
        for j in range(i+1,len(x)):
            if x[j] > x[startowyIndex]:
                startowyIndex = j
            temp = x[i]
            x[i] = x[startowyIndex]
            x[startowyIndex] = temp
    return x

taba = []
a = input("Podaj liczbe do posortowania: ")
for liczba in a:
    taba.append(int(liczba))

print(sortowaniePrzezWybor(taba))
