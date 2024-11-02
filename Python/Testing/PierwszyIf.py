jednostka = input("W jakiej jednostce chcesz podać wage LBS, KG: ")
waga = int(input("Podaj swoja wage: "))
if jednostka.upper() == "LBS":
    waga = float(waga) * 0.45
    print(f"Wazysz: {waga} KG")
elif jednostka.upper() == "KG":
    waga = float(waga) / 0.45
    print(f"Wazysz: {waga} LBS")
else:
    print("Bledne dane na wejsciu")