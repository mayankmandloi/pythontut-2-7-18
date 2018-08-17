class T1:
    def showMe(self):
        print("I am showMe from class T1")
class T2(T1):
    def test(self):
        print("I am test from class T2")
    def showMe(self):
        print("I am showMe from class T2")



t= T2()
t.showMe()
