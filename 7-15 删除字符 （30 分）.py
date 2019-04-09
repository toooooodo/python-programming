ls=list(input())
ch=input()
re=''
for i in ls:
  if i == ch or i.upper()==ch or i.lower()==ch:
    continue
  else:
    re+=i
print('result: '+re)
