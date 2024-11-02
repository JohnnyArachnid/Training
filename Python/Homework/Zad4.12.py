n = int(input("Podaj n-ty wyraz ciągu fibonachiego do obliczenia: "))
def funkcja (a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return funkcja(a-1) + funkcja(a-2)
print(funkcja(n))



































































