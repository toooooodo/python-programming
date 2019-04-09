s=input()
res=''
for i in s:
    if 'a'<=i<='z' and i not in res and i.upper() not in res:
        res+=i
    elif 'A'<=i<='Z' and i not in res and i.lower() not in res:
        res+=i
    if len(res)==10:
        break
print(res if len(res)==10 else 'not found')
        
