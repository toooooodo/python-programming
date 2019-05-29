exampleFile=open("example.txt","rt")
resultFile=open("result.txt","wt")
for line in exampleFile.readlines():
    line=list(line)
    for i in range(len(line)):
        if line[i].isupper():
            line[i]=line[i].lower()
        elif line[i].islower():
            line[i]=line[i].upper()
    resultFile.write(''.join(line))
exampleFile.close()
resultFile.close()