def iloscliterwslowie(a,b):
    s = 0
    for index in a:
        if i == index:
            s+=1
        else:
            continue
    return s

x = str(input("Podaj wyraz do zliczenia: "))
y = x.replace(" ","")
słownik = {}
for i in y:
    słownik[i] = iloscliterwslowie(y,i)
print(słownik)

