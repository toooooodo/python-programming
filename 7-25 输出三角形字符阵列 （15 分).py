n=int(input())
add=0
for i in range(n):
    for j in range(n-i):
        print(chr(ord('A')+add),'',end='')
        add+=1
    print()
