import math
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
d = (b**2)-4*a*c
e = math.sqrt(d)
if d > 0:
    print(round((-b-e)/(2*a), 2))
    print(round((-b+e)/(2*a), 2))
elif d == 0:
    print(round((-b)/(2*a), 2))
else:
    print("Nie ma miejsc zerowych")

