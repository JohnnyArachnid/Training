x = input("Wpisz pierwszy wyraz: ")
y = input("Wpisz wyraz, który chcesz sprawdzić czy jest anagramem poprzedniego: ")
def CzyAnagram(x,y):
    if len(x) != len(y):
        return False
    tabx = []
    pomocniczax = []
    taby = []
    pomocniczay = []
    for i in x:
        if ord(i) > 90:
            tabx.append(ord(i)-32)
        else:
            tabx.append(ord(i))
    for j in y:
        if ord(j) > 90:
            taby.append(ord(j)-32)
        else:
            taby.append(ord(j))
    while tabx:
        min = tabx[0]
        for k in tabx: 
            if k < min:
                min = k
        pomocniczax.append(min)
        tabx.remove(min)
    while taby:
        min = taby[0]
        for l in taby: 
            if l < min:
                min = l
        pomocniczay.append(min)
        taby.remove(min)
    return pomocniczax == pomocniczay
print(CzyAnagram(x,y))