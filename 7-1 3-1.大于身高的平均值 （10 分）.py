ls=list(map(int,input().split()))
res=list(map(str,[i for i in ls if i > sum(ls)/len(ls)]))
print(' '.join(res),end=' ')
#print(''.join(res))
