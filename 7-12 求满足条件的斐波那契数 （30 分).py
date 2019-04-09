n=int(input())
a=0;b=1
while True:
    if b>n:
        print(b)
        break
    else:
        c=a+b
        a=b
        b=c
