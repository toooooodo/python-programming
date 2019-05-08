n=int(input())
dic=dict()
ls=list(map(int,input().split()))
for i in ls:
    dic[i]=dic.get(i,0)+1
#sorted(dic)
for i in sorted(dic):
    print('%d:%d'%(i,dic[i]))
#print(dic)

    