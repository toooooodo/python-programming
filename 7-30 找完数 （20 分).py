import math
m,n=map(int,input().split())
flag = False
for i in range(m,n+1):
    lst=[]
    for j in range(1,int(math.sqrt(i))+1):
        if i%j==0 and j==1:
            lst.append(j)
        elif i%j==0 and j!=1:
            lst.append(j)
            lst.append(i//j)
    lst.sort()
    if sum(lst)==i:
        print(i,'=',' + '.join(list(map(str,lst))))
        flag=True
if not flag:
    print('None')
