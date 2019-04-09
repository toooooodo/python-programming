letter=blank=digit=other=0
s=''
while True:
    s=s+input()
    if len(s)!=10:
        s+="\n"
    else:
        break
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        letter+=1
    elif '0'<=i<='9':
        digit+=1
    elif i==' ' or i=='\n':
        blank+=1
    else:
        other+=1
print("letter = %d, blank = %d, digit = %d, other = %d"%(letter,blank,digit,other))
    
