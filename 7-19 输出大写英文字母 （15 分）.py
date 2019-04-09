s=input()
res=''
for i in s:
    if i.isupper()==True and i not in res:
        res+=i
print(res if len(res)!=0 else 'Not Found')
