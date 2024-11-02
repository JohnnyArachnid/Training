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