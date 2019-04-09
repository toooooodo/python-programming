import math

def judge(x):
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

m,n=input().strip().split()
m,n=int(m),int(n)
_sum=count=0
for i in range(m,n+1):
    if judge(i)==True:
        count+=1
        _sum+=i
print(count,_sum)
