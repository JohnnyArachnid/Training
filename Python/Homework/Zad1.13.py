print("Witam w harmonogramie zajęć")
print("Wybierz dzień tygodnia z poniższej listy aby stwierdzić czy jest coś do zrobienia\nWartość podaj za pomocą cyfry")
print("1. Poniedziałek\n2. Wtorek\n3. Środa\n4. Czwartek\n5. Piątek\n6. Sobota\n7. Niedziela")
d = int(input("Podaj numer dnia tygodnia: "))
if d == 1 or d == 2 or d == 3 or d == 4 or d == 5:
    print("DO PRACY RODACY ")
elif d == 6 or d == 7:
    print("MASZ WOLNE GRATULACJE KORZYSTAJ Z WEEKENDU!")
else:
    print("Zainicjuj ponownie program wybierz dzień w postaci cyfry podanej powyżej")