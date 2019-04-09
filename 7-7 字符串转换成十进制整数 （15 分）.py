s=input()
h=''
for i in s:
    if i=='#':
        break
    elif h=='' and i=='-':
        h='-'
    elif '0'<=i<='9' or 'a'<=i<='f' or 'A'<=i<='F':
        h+=i
print(0 if h=='' or h=='-' else int(h,16))
