class test():
    def __init__(self,name,number):
        self.__name=name
        self.__number=number

person1=test("Mayank",12345678)
print(person1.__name,"&",person1.__number)