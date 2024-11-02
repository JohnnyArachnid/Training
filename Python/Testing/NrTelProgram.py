nr_tel = []
tekst = ""
dane = input("Podaj nr tel: ")
for i in dane:
    nr_tel.append(int(i))
for i in nr_tel:
    if i == 1:
        tekst += "Jeden "
    elif i == 2:
        tekst += "Dwa "
    elif i == 3:
        tekst += "Trzy "
    elif i == 4:
        tekst += "Cztery "
    elif i == 5:
        tekst += "Piec "
    elif i == 6:
        tekst += "Szesc "
    elif i == 7:
        tekst += "Siedem "
    elif i == 8:
        tekst += "Osiem "
    elif i == 9:
        tekst += "Dziewiec "
print(tekst)
