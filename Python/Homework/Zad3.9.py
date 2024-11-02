text = input("Podaj wyraz do sprawdzenia: ")
text = text.lower()
for i in range(97,123):
    suma = 0
    for j in text:
        if(chr(i) == j):
            suma = suma + 1
    if(suma != 0):
        print(chr(i),"-",suma,"razy")









