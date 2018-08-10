class t1():
    def __init__(self,name,number):
        self.name=name
        self.number=number

class t2(t1):
    def __init__(self,age,name,number):
        super(t2, self).__init__(name,number)
        self.age=age


person = t2(23,"Mayank",12345678)
print(person.name,person.number,person.age)