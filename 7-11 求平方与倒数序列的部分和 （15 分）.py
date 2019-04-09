m,n=input().split()
m,n=int(m),int(n)
sum=0
for i in range(m,n+1):
    sum+=i**2+1/i
print("sum = %.6f"%sum)
