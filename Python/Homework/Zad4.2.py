a = int(input("Podaj liczbę: "))
def funkcja(x):
    if int(x) % 3 == 0 and int(x) % 5 == 0:
        return True
    return False
print(funkcja(a))

# a = int(input("Podaj liczbę: "))
# def funkcja(x):
#     return int(x) % 3 == 0 and int(x) % 5 == 0
# print(funkcja(a))
