print("Enter three numbers")
x=int(input())
y=int(input())
z=int(input())
if x>y:
    if x>z:
        print(str(x)+" is greatest")
    else:
        print(str(z)+" is greatest")
elif y>z:
        print(str(y)+" is greatest")
else:
    print(str(z)+" is greatest")
