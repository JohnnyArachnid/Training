file1 = open("./anagram.txt","r")
file2 = open("./zad9.txt","w")

tab = []
tab1 = []
z = ""

for x in file1.readlines():
    line = x.replace("\n","")
    t = line.split(" ")
    tab.append(t)
# print(tab)
pomocnicza = 0
for i in tab:
    pomocnicza = 0
    # print(i)
    for j in i:
        # print(j)
        if len(j) != len(i[0]):
            pomocnicza = 1
    if pomocnicza == 0:
        tab1.append(i)
# print(len(tab1))

p = 0

for j in tab1:
    for i in j:
        z = z+i+" "
    if tab1[p]!=tab1[len(tab1)-1]:
        z = z+"\n"
    p = p+1
print(z)

file2.write(z)

file1.close()
file2.close()