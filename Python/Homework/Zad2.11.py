a = str(input("Podaj liczbę naturalną: "))
suma = "0"
for i in range(1, int(a)):
    if int(a) % i == 0:
        if i == 1:
            continue
        else:
            i=str(i)
            suma+=str(i)
    i=int(i)
    i+=1
print(a,"=",suma.replace("0", ""),sep="")
