pesel = input("pesel")
newPesel = []
i = 0
for letter in pesel:
    newPesel.append(int(letter))
    i = i + 1
j = 0
for el in newPesel:
    if(0 == j or j == 4 or 8 == j or j == 10):
        newPesel[j] = el * 1

    elif(1 == j or j == 5 or 9 == j):
        newPesel[j] = (el * 3) % 10

    elif(2 == j or j == 6):
        newPesel[j] = (el * 7) % 10

    else:
        newPesel[j] = (el * 9) % 10
    j = j + 1
check = 0
for el in newPesel:
    check = check + el
check = check - newPesel[10]
if(check >= 10):
    check = check % 10
check = 10 - check
if(check == 10):
    check = check % 10
print("y") if check == newPesel[10] else print("n")



