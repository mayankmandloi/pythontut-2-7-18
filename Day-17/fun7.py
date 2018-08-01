def test(a):
    if a<=0:
        return 1
    else:
        return a+test(a-1)

print(test(10))

"""
10+9+8+7+6+5+4+3+2+1+1
"""