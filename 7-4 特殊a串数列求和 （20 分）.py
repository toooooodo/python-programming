a,b=input().split()
b=int(b)
sum = sum(int(a*i) for i in range(1,b+1))
print("s =",sum)
