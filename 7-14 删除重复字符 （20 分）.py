#st=set(input())
#ls=list(st)
#ls.sort()
#print(''.join(ls))

s=input()
ls=[]
for i in s:
  if i not in ls:
    ls.append(i)
ls.sort()
print(''.join(ls))
