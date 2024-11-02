 słownik1 = {
    "Wartość11": "Morela",
    "Wartość2": "Gruszka",
    "Wartość3": "Pomidor",
}
słownik2 = {
    "Wartość1": "Jabłko",
    "Wartość2": "Gruszka",
    "Wartość3": "Winogron",
    "Wartość4": "Ogórek",
}
słownik3 = {}
for klucz1,wartość1 in słownik1.items():
    for klucz2,wartość2 in słownik2.items():
        if klucz1 == klucz2:
            słownik3[klucz1] = wartość1
        else:
            słownik3[klucz1] = wartość1
            słownik3[klucz2] = wartość2
print(słownik3)