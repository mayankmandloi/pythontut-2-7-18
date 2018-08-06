class MyClass():
    x=10

p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)
p1.y=23
p1.x=12
print(p1.x)
print(p2.x)
print(p1.y)
#print(p2.y)