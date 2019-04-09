res=[int(i) for i in input() if '0'<=i<='9']
dig=0
for i in res:
    dig=dig*10+i
print(dig)
