def anagram(slowo1,slowo2):
    if len(slowo1) != len(slowo2):
        return False
    for literka in slowo1:
        if literka in slowo2 == False:
            return False
    return True

x = input("Podaj pierwsze slowo do sprawdzenia czy para to anagram: ")
y = input("Podaj drugie slowo do sprawdzenia czy para to anagram: ")
if anagram(x,y) == True:
    print("Slowa są anagramem")
else:
    print("Slowa nie są anagramem")