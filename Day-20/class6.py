class test():
    def __init__(self,name,number):
        self.__name=name
        self.__number=number

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    def getNumber(self):
        return self.__number

    def setName(self,number):
        self.__number=number


person1=test("Mayank",12345678)
print(person1.getName(),"&",person1.getNumber())