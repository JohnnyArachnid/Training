def anagram(x,y):
    tab = ["A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N","Ń","O","Ó","P","R","S","Ś","T","U","w","Y","Z","Ź","Ż"]
    x.upper()
    y.upper()
    licznik1 = 0
    licznik2 = 0
    if len(x) != len(y):
        return False
    else:
        for index1 in range(len(tab)):
            for index2 in range(len(x)):
                if x[index2] == tab[index1]:
                    licznik1+=1
                if y[index2] == tab[index1]:
                    licznik2+=1
            if licznik1 != licznik2:
                return False
            else:
                licznik1 = 0
                licznik2 = 0
    return True

a = str(input("Podaj pierwszy wyraz: "))
b = str(input("Podaj drugi wyraz: "))
print(anagram(a,b))

