file=open('letter.txt','rt')
letter=number=others=0
for line in file.readlines():
    for i in line:
        if ord('A')<=ord(i)<=ord('Z') or ord('a')<=ord(i)<=ord('z'):
            letter+=1
        elif ord('0')<=ord(i)<=ord('9'):
            number+=1
        else:
            others+=1
print(letter,number,others)
file.close()