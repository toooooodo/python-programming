n=int(input().strip())
if n==0:
    print("average = 0.0")
    print("count = 0")
else:
    
    lst=list(map(int,input().strip().split()))
    count=0
    for i in lst:
        if i >= 60:
            count+=1
    print("average = %.1f"%(sum(lst)/len(lst)))
    print("count = %d"%count)
        

