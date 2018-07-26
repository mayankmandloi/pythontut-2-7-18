"""
A dictionary is a collection which is unordered, changeable and indexed.
 In Python dictionaries are written with curly brackets, and they have keys and values.

"""
# {"key1" : "value1" ,"key2" : "value2"}
student1={"name":"Niranjan","number":123456789,"height":5.6}
#print(student1)
#print("Hello I am ",student1["name"]," and my number is ",student1["number"])

student2=dict(name="Niranjan",number="123456789",height=5.6)
#print(student2)
#print(student2["name"])
student2["name"]="Narendra"
#print(student2)

for item in student2:
    print(item,"is",student2[item],end=" ")
print()

for a,b in student1.items():
    print(a,"is",b,end=" ")
del student1["name"]
print(student1)