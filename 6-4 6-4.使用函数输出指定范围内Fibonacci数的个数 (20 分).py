def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)

def PrintFN(m,n):
    lst=[]
    i=0
    while fib(i)<m:
        i+=1
    while fib(i)<=n:
        lst.append(fib(i))
        i+=1
    return lst

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))