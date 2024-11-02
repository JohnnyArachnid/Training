a = input("Podaj wyraz do sprawdzenia czy jest Palindromem: ")
tab = []
for i in a:
    tab.append(i)
tab1 = tab[::-1]
lent = len(tab)
for i in range(lent):
    if tab[i] != tab1[i]:
        print("Podany wyraz nie jest Palindromem")
        break
    else:
        print("Podany wyraz jest Palindromem")
        break










