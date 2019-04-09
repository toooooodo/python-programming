n=int(input())
if n<1:
    print("Invalid.")
else:
    a=0
    b=1
    for i in range(n):
        if i!=0 and i%5==0:
            print()
        print("%11d"%b,end='')
        c=a+b
        a=b
        b=c
        
