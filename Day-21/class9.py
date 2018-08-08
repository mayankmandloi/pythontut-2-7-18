class Student():
    def __init__(self,name):
        self.name=name

s1=Student("Santosh")
print(s1.name)
s2=s1
print(s2.name)
s2.name="Maryada"
print(s2.name)
print(s1.name)