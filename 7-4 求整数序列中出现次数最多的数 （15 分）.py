ls=list(map(int,input().strip().split()))
num=count=0
for i in ls[1:]:
    if ls.count(i)>count:
        count=ls.count(i)
        num=i
print('%d %d'%(num,count))
