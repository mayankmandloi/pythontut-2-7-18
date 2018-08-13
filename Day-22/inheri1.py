class t1():
    name = "Mayank"
    def __init__(self):

        self.number=9425319399
        print("I am t1")

class t2(t1):
    def __init__(self):
        super().__init__()
        print("I am t2")

class t3(t2):
    def __init__(self):
        super().__init__()
        print("I am t3")


t = t3()
print(t.name)
print(t.number)