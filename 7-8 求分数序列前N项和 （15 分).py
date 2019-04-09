n=int(input().strip())
a=2;b=1;_sum=0
for i in range(n):
    _sum+=a/b
    c=a+b
    b=a
    a=c
print("%.2f"%_sum)
