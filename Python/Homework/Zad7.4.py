słownik1 = {
    "Wartość1": "Morela",
    "Wartość2": "Gruszka",
    "Wartość3": "Pomidor",
}
słownik2 = {
    "Wartość1": "Jabłko",
    "Wartość2": "Gruszka",
    "Wartość33": "Winogron",
}
tab = []
for klucze1 in słownik1:
    for klucze2 in słownik2:
        if klucze1 == klucze2:
            tab.append(klucze1)
print(tab)


































































