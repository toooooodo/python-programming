ls=list(map(int,input().strip().split(',')))
n=int(input().strip())
dic=dict()
for i in range(len(ls)):
    dic[ls[i]]=i
for i in range(len(ls)):
    if n-ls[i] in dic:
        print(i,dic[n-ls[i]])
        break
else:
    print('no answer')