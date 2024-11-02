z1 = input("Podaj ile cali ma twoja dyskietka:")
z1 = float(z1)
z2 = input("Podaj długość dyskietki:")
z2 = float(z2)
z3 = input("Podaj szerokość dyskietki")
z3 = float(z3)
if z1 == 8:
    print ("twoja dyskietka ma pojemność 800 KB")
elif z1 == 5.25:
    print("twoja dyskietka ma pojemność 110 KB")
elif z1 == 3:
    print("twoja dyskietka ma pojemność 320 KB")
elif z1 == 3.5:
    print("twoja dyskietka ma pojemność 2880 KB")
    pass
z4 = z2 * z3
print ("Pole na którym możesz nakleić naklejkę to: {}".format(z4))