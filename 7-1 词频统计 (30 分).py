import sys
s=sys.stdin.read()
strs=s[:s.find('#')]

for k in set([i for i in strs if i.isalnum()==False and i!='_']):
    strs=strs.replace(k,' ')
strs=strs.rstrip(' ').lower().split()
counts=dict()
for i in strs:
    k=i[:15]
    if k not in counts:
        counts[k]=1
    else:
        counts[k]+=1

ans=sorted(counts.items(),key=lambda x:(-x[1], x[0]))
print(len(counts))

for i in range(0,int(0.1*len(counts))):
    print(str(ans[i][1])+":"+ans[i][0])