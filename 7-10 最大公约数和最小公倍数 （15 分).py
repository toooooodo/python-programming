def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

m,n=map(int,input().strip().split())
_gcd=gcd(m,n)
print(_gcd,int(_gcd*(m/_gcd)*(n/_gcd)))
