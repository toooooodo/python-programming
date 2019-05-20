def prime(p):
    if p<=1:
        return False
    else:
        for i in range(2,int(p**0.5+1)):
            if p%i==0:
                return False
        return True

def PrimeSum(m,n):
    return sum([i for i in range(m,n+1) if prime(i)])
m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))