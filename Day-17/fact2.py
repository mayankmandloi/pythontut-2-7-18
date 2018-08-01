def fact(inp):
    if inp>0:
        return  inp*fact(inp-1)
    else:
        return 1

a=int(input("Enter a number"))
print("factorial is",fact(a))