import math
def judge(k,n):
    lst=list(map(int,list(str(k))))
    if k==sum([i**n for i in lst]):
        return True
    else:
        return False

n=int(input())
for i in range(int(math.pow(10,n-1)),int(math.pow(10,n))):
    if judge(i,n):
        print(i)
