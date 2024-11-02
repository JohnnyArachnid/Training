import datetime
data_urodzenia = int(input("Podaj swój rok urodzenia: "))
dzisiaj = datetime.date.today()
rok = dzisiaj.year
wiek = rok - data_urodzenia
print("Masz: "+str(wiek)+" lat \n")
#Wyswietlenie typu zmiennej dzisiaj type(dzisiaj)