print("Podaj swój pesel:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
k=int(input())
print("Wpisany przez ciebie pesel to: {}{}{}{}{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g,h,i,j,k))
a=(a*1)%10
b=(b*3)%10
c=(c*7)%10
d=(d*9)%10
e=(e*1)%10
f=(f*3)%10
g=(g*7)%10
h=(h*9)%10
i=(i*1)%10
j=(j*3)%10
s=a+b+c+d+e+f+g+h+i+j
x=10-s
if(x==k):
    print("Pesel jest poprawny")
else:
    print("Niepoprawny pesel")
