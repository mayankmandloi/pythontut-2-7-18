class Student:
    city="Indore"

s1= Student()
s2=Student()

print(s1.city)
print(s2.city)
print(Student.city)

s1.city="Bhopal"

print(s1.city)
print(s2.city)
print(Student.city)