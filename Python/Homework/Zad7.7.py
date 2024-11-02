słownik = {
    "Wartość11": "Morela",
    "Wartość2": "Delete",
    "Wartość3": "Pomidor",
}
słownik1 = słownik.copy()
for key,value in słownik.items():
    value = value.upper()
    if value == "DELETE":
        słownik1.pop(key)
print(słownik1)

