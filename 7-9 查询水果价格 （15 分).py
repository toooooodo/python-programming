print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit")
lst=[0,3.0,2.5,4.1,10.2]
inp=list(map(int,input().strip().split()))
for i in range(5):
    x=inp[i]
    if x==0:
        break
    elif 1<=x<=4:
        print("price = %.2f"%lst[x])
    else:
        print("price = 0.00")
        
