"""imiona = ["Daniel", "Jakub", "Tadeusz", "Kinga", "Kamila", "Maria"]
print(imiona)
print(imiona[2])
print(imiona[-1])
print(imiona[2:])
print(imiona[:2])
#Tak jak stringi"""
print("Podaj 5 liczb aby uzyskac z nich najwieksza: ")
tab_liczb = []
for i in range(5):
    tab_liczb.append(int(input(f"Podaj liczbe nr.{i}: ")))
maks = 0
for i in range(len(tab_liczb)):
    if tab_liczb[i] > maks:
        maks = tab_liczb[i]
print(maks)

