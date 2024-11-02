n = int(input("Podaj liczbę całkowitą większą od 1: "))
A = [0]
for i in range (0,n):
    d = int(input("Podaj kolejną liczbę: "))
    A.append(d)
L = 1
P = n
while L != P:
    pivot = int((L+P)/2)
    if A[pivot] % 2 !=0:
        L = pivot + 1
    else:
        P = pivot
print(A[L])
