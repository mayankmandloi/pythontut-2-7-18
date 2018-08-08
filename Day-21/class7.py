class Student():
    count=0
    def __init__(self):
        type (self).count +=1

s1= Student()
s2=Student()
s3=Student()
s4=Student()

print(s1.count)
print(s2.count)
print(s3.count)
print(s4.count)
s5=Student()
print(s1.count)