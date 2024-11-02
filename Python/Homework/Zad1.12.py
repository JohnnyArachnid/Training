print("Witam w prostym kalkulatorze\nJeżeli chcesz obliczyć pole fgur płaskich wybierz nr.1 jeżeli chcesz obliczyć objętość brył wynierz nr.2")
n = int(input("Podaj Wybrany Numer: "))
if n == 1:
    print("Witam w prostym kalkulatorze pól figur")
    print("Zapoznaj się z poniższych możliwościami programu po czym wybierz opcję do obliczenia pola twojej figury\n")
    print("1.Pole Kwadratu\n2.Pole Prostokąta\n3.Pole trójkąta\n4.Pole Trapezu\n5.Pole Równoległoboku")
    p = int(input("Zatem pole której figury chcesz obliczyć? "))
    if p == 1:
        a = int(input("Podaj bok kwadratu którego pole chcesz obliczyć: "))
        p1 = a ** 2
        print("Pole twojego kwadratu wynosi: ", p1)
    elif p == 2:
        a = int(input("Podaj pierwszy bok prostokąta którego pole chcesz obliczyć: "))
        b = int(input("Podaj drugi bok prostokąta którego pole chcesz obliczyć: "))
        p2 = a * b
        print("Pole twojego prostokąta wynosi: ", p2)
    elif p == 3:
        a = int(input("Podaj podstawę trójkąta którego pole chcesz obliczyć: "))
        h = int(input("Podaj wysokość trójkąta którego pole chcesz obliczyć: "))
        p3 = (a * h)/2
        print("Pole twojego trójkąta wynosi: ", p3)
    elif p == 4:
        a = int(input("Podaj pierwszą podstawę trapezu którego pole chcesz obliczyć: "))
        b = int(input("Podaj drugą podstawę trapezu którego pole chcesz obliczyć: "))
        h = int(input("Podaj wysokość trapezu którego pole chcesz obliczyć: "))
        p4 = ((a+b)*h)/2
        print("Pole twojego trapezu wynosi: ", p4)
    elif p == 5:
        a = int(input("Podaj podstawę równoległoboku którego pole chcesz obliczyć: "))
        h = int(input("Podaj wysokość równoległoboku którego pole chcesz obliczyć: "))
        p5 = a * h
        print("Pole twojego równoległoboku wynosi: ", p5)
    else:
        print("Proszę zainicjuj program ponownie i wybierz liczbę od 1 do 5: ")
elif n == 2:
    print("Witam w prostym kalkulatorze objętości brył")
    print("Zapoznaj się z poniższych możliwościami programu po czym wybierz opcję do obliczenia objętości twojej figury\n")
    print("1.Objętość Sześcianu\n2.Objętość Ostrosłupa\n3.Objętość Walca\n")
    o = int(input("Zatem objętośc której bryły chcesz obliczyć? "))
    if o == 1:
        a = int(input("Podaj bok sześcianu którego objętość chcesz obliczyć: "))
        o1 = a ** 3
        print("Objętość twojego sześcianu wynosi: ", o1)
    elif o == 2:
        a = int(input("Podaj pole podstawy ostrosłupa którego objętość chcesz obliczyć: "))
        h = int(input("Podaj wysokość ostrosłupa którego objętość chcesz obliczyć: "))
        o2 = 1/3*(a*h)
        print("Pole twojego równoległoboku wynosi: ", o2)
    elif o == 3:
        a = int(input("Podaj promień podstawy walca którego pole chcesz obliczyć: "))
        h = int(input("Podaj wysokość walca którego pole chcesz obliczyć: "))
        p = 3.14
        o3 = (p*h)*a**2
        print("Pole twojego równoległoboku wynosi: ", o3)
    else:
        print("Proszę zainicjuj program ponownie i wybierz liczbę od 1 do 3: ")
else:
    print("Wystąpił nieznany błąd zainicjuj ponownie program")