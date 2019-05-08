import functools

def func(x,y):
    if type(x)==type(y):
        if x<y:
            return -1
        elif x==y:
            return 0
        else:
            return 1
    else:
        if type(x)==type('x'):
            return 1
        else:
            return -1
exec('d1='+input().strip())
exec('d2='+input().strip())
for i in d1:
    if i in d2:
        d2[i]+=d1[i]
    else:
        d2[i]=d1[i]
lst=sorted(d2,key=functools.cmp_to_key(func))
print('{',end='')
for i in range(len(lst)):
    if type(lst[i])==type(1):
        print(lst[i],end='')
    else:
        print('"'+lst[i]+'"',end='')
    print(':%d'%(d2[lst[i]]),end='')
    if i!=len(lst)-1:
        print(',',end='')
print('}')