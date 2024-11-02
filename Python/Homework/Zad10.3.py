def sortowanieBabelkoweAnagram(x):
    for j in range(len(x)-1):
        for i in range(len(x)-1):
            y = ord(x[i])
            z = ord(x[i+1])
            if y > 97:
                y = ord(x[i]) - 32
            if z > 97:
                z = ord(x[i+1]) - 32
            if y > z:
                x[i] = chr(y)
                x[i+1] = chr(z)
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    return x
def anagram(x,y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True

a = str(input("Podaj pierwszy wyraz: "))
b = str(input("Podaj drugi wyraz: "))
taba = []
for i in a:
    taba.append(i)
tabb = []
for i in b:
    tabb.append(i)
print(anagram(sortowanieBabelkoweAnagram(taba), sortowanieBabelkoweAnagram(tabb)))