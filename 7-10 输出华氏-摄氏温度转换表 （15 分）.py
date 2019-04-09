lower,upper=input().split()
lower=int(lower)
upper=int(upper)
if lower>upper or lower>100:
    print("Invalid.")
else:
    print("fahr celsius")
    for i in range(lower,upper+1,2):
        print("%d%6.1f"%(i,5*(i-32)/9))
