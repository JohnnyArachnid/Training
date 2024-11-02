a = input("Podaj wyraz do sprawdzenia: ")
def funkcja(x):
    l = len(x)
    for index in range(0, l):
        if x[index] == x[l - 1 - index]:
            return True
    return False
print(funkcja(a))

# a = input("Podaj wyraz do sprawdzenia: ")
# def funkcja(x):
#     l = len(x)
#     n = 0
#     for index in x:
#         if index != x[l - 1 - n]:
#             n+=1
#             return False
#     return True
# print(funkcja(a))