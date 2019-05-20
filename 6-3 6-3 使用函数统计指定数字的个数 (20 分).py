def CountDigit(number,digit):
    return sum([i==str(digit) for i in str(number)])

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)