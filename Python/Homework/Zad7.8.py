def srednia(a):
    s = 0
    for index in range(len(a)):
        s+=index
    return s

słownik = {
    "Wartość1": 1,
    "Wartość2": 2,
    "Wartość3": 3,
    "Wartość4": 4,
    "Wartość5": 5,
}
słownik1 = słownik.copy()
s = srednia(słownik1)
for key,value in słownik.items():
    if value < s:
        słownik1.pop(key)
        s = srednia(słownik1)
    else:
        continue
print(słownik1)
