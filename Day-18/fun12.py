def fun1():
    def fun2():
        print("I am fun2")
    print("I am fun1")
    return  fun2

abcd = fun1()
abcd()
abcd()
abcd()
abcd()
print(abcd)