def r2d2():
    print("I am r2d2")
    t2()
    print("r2d2 says good-bye")

def t1():
    print("I am t1")
    print("bye from t1")
    print("test")

def t2():
    print("I am t2")
    t1()
    print("Bye From t2")


r2d2()