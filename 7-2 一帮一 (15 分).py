n=int(input().strip())
lst=[]
for i in range(n):
    s=input().strip().split()
    lst.append(list(s)+[True])
for i in range(n//2):
    for j in range(n):
        if lst[j][2]==True:
            lst[j][2]=False
            idx1=j
            break
    for j in range(n-1,-1,-1):
        if lst[j][2]==True and lst[j][0]!=lst[idx1][0]:
            lst[j][2]=False
            print(lst[idx1][1],lst[j][1])
            break