n=int(input())
a=1
b=1
if n<3:
    print("1")
else:
    c=0
    for i in range (2,n):
        c=a+b
        a=b
        b=c 
    print(c)