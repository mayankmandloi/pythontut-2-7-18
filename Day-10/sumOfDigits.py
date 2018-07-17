num1=int(input("Enter any number"))
sum=0
while num1>0:
    sum=sum*10
    sum=sum+num1%10
    num1=num1//10
print("Answer is ",sum)