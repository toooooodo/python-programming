ls=list(input())
for i in range(len(ls)):
    if ls[i].isupper() == True:
        ls[i]=ls[i].lower()
    elif ls[i].islower() == True:
        ls[i]=ls[i].upper()
print(''.join(ls[:len(ls)-1]))
