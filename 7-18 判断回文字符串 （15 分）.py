a=input()
b=a[::-1]
flag=True
for i in range(len(a)):
    if a[i]!=b[i]:
        flag=False
        break
print(a+'\n'+('Yes' if flag else 'No'))
