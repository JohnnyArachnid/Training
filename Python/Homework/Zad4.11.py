n = int(input("Podaj liczbe do wyliczenia silni: "))
def funkcja (a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return funkcja(a-1) * a
print(funkcja(n))



































































