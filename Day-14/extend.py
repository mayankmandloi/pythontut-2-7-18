studentList=["Student1","Student2","Student 3",1234]
studentuple1=("Student1","Student2","Student 3",1234)
thisset = {"Student1","Student2","Student 3",1234}
student1={"name":"Niranjan","number":123456789,"height":5.6}
print(studentList)
studentList.extend(studentuple1)
print(studentList)
studentList.extend(thisset)
print(studentList)
studentList.extend(student1.values())
print(studentList)
