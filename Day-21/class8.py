class Student():
    count =0
    def __init__(self):
        type (self).count+=1
    def __del__(self):
        type (self).count-=1
        print("Hahaha")

print(Student.count)
s1=Student()
print(s1.count)
s2=Student()
print(s1.count)