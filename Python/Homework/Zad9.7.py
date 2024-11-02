def anagram(x,y):
    tab1 = []
    tab2 = []
    x.upper()
    y.upper()
    for q in x:
        tab1.append(q)
    for w in y:
        tab2.append(w)
    if len(x) != len(y):
        return False
    else:
        tab1.sort()
        tab2.sort()
        for index in range(len(tab1)):
            if tab1[index] != tab2[index]:
                return False
    return True

a = str(input("Podaj pierwszy wyraz: "))
b = str(input("Podaj drugi wyraz: "))
print(anagram(a,b))

