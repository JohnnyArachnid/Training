n = input("Podaj liczbę nautalną : ")
licznik1 = 0
licznik2 = 0
for i in n:
    if int(i) % 2 == 0:
        licznik1+=1
    else:
        licznik2+=1
if licznik1 > licznik2:
    print("W podanej liczbie jest więcej cyfr parzystych")
elif licznik1 == licznik2:
    print("W podanej liczbie jest tyle samo cyfr parzystych co nieparzystych")
elif licznik1 < licznik2:
    print("W podanej liczbie jest więcej cyfr nieparzystych")


