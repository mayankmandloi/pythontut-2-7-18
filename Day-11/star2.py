a=int(input("ENter number of rows"))
x=0
while x<a:
    z=0
    while z<x:
        print(" ",end="")
        z=z+1
    y=0
    while y<2*(a-x)-1:
        print("*",end="")
        y=y+1
    print("")
    x=x+1