def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-2)+fibo(n-1)
x = int(input("Podaj liczbe fibo do obliczenia: "))
print(fibo(x))