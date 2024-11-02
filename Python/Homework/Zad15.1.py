def WiezaHanoi(n,a,b,c):
    if n == 0:
        return ""
    L = WiezaHanoi(n-1,a,c,b)
    P = WiezaHanoi(n-1,b,a,c)
    return L + a + c + P
print(WiezaHanoi(3,"A","B","C"))
