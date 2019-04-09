l1=input().split()
l2=input().split()
res=[]
for i in range(1,len(l1)):
    if l2[1:].count(l1[i])==0 and l1[i] not in res:
        res.append(l1[i])
for i in range(1,len(l2)):
    if l1[1:].count(l2[i])==0 and l2[i] not in res:
        res.append(l2[i])
print(' '.join(res))
