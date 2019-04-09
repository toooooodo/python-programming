import math

def judge(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
for i in range(2,n):
    if judge(i) and judge(n-i):
        print("%d = %d + %d"%(n,i,n-i))
        break
