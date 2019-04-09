a,b=input().split()
a,b=int(a),int(b)
count=0
sum=0
for i in range(a,b+1):
    sum+=i
    count+=1
    if count%5!=0 or i ==b:
        print("%5d"%i, end="")
    else:
        print("%5d"%i)
print("\nSum = %d"%sum)
