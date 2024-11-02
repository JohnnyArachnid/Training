def palindrom(a):
    for i in range(len(a)):
        if a[i] != a[len(a) - 1 - i]:
            return print("Wyraz nie ",a," jest palindromem")
    return print("Wyraz ",a," jest palindromem")
słownik = {
    "ann":"a",
    "ka":"jak",
    "antanna":"rywa"
}
s = ""
for key,item in słownik.items():
    s = key+item
    palindrom(s)
    s = ""

