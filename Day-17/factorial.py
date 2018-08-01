def fact(a):
    ans = 1
    while a > 0:
        ans = ans * a
        a = a - 1
    return ans



inp=int(input("Enter a number"))
print("=",fact(inp))
