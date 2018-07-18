"""
*
***
*****

##*
#***
*****
"""

x=0

a=int(input("Enter number of rows"))
while x<a:
    z=0
    while z<(a-1)-x:
        print(" ",end="")
        z=z+1
    y = 0
    while y<=x*2:
        print("*",end="")
        y=y+1
    print("")
    x=x+1