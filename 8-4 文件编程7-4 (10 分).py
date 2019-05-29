file=open('water.txt','rt')

for line in file.readlines():
    if line!='\n':
        lst=line.strip().split()
#        print(total,int(lst[13])-int(lst[1]))
        print(lst[0],(int(lst[13])-int(lst[1]))*1.05)
file.close()