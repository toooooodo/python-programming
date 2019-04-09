ch=input()
s=input()
index=-1
for i in range(len(s)):
    if s[i]==ch:
        index=i
print('Not Found' if index==-1 else 'index = %d'%(index))
