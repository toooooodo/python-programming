n=int(input().strip())
a=[]
max_s=[]
min_s=[]
for _ in range(n):
    a.append(list(map(int,input().strip().split())))
for i in range(n):
    maxa=max(a[i][j] for j in range(n))
    mina=min(a[k][i] for k in range(n))
    max_s+=[(i,j) for j in range(n) if a[i][j]==maxa]
    min_s+=[(k,i) for k in range(n) if a[k][i]==mina]
print(len(list(set(max_s)&set(min_s))))