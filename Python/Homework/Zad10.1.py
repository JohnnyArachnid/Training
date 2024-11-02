def sortowanieBabelkowe(x):
    for j in range(len(x)-1):
        for i in range(len(x)-1):
            if x[i] < x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    return x

tab = []
a = int(input("Podaj dlugosc tablicy: "))
for index in range(a):
    b = int(input("Podaj element tablicy: "))
    tab.append(b)
print(sortowanieBabelkowe(tab))