print("Enter a 4 digit number")
abcd= int(input())
d=abcd%10
abcd=abcd//10
c=abcd%10
abcd=abcd//10
b=abcd%10
abcd=abcd//10
a=abcd%10
print(a+b+c+d)