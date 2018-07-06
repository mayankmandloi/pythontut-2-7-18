"""
Logical operators are used to combine conditional statements:

Operator     Description                                                Example
1)and     Returns True if both statements are true(*)                   x < 5 and x < 10
2)or      Returns True if one of the statements is true(+)              x < 5 or x < 4
3)not     Reverse the result,                                          not(x < 5 and x < 10)
"""
x =  int(input())
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))
print(not(x<5 or x<10))
