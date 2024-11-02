a = input("Podaj wyraz do sprawdzenia: ")
def funkcja(x):
    b = len(x)
    s = 0
    for i in range(0, b):
        if x[i] == "a" or x[i] == "A":
            s+=1
    return s
print(funkcja(a))

