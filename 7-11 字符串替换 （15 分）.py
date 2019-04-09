ls=list(input())
for i in range(len(ls)):
    if 'A'<=ls[i]<='Z':
        #ls[i]=str(int('A')+int('Z')-int(ls[i]))
        ls[i]=chr(ord('A')+(ord('Z')-ord(ls[i])))
print(''.join(ls))
