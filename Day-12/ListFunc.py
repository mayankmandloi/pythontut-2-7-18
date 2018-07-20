"""
List Methods

Python has a set of built-in methods that you can use on lists.
Method 	Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""
nameList=["Mayyank","Web Bhumi","Varun","Niranjan","RaviRaj","Narendra"]
print(nameList)
nameList.append("Web Bhumi")
nameList.append("Web Bhumi")
print(nameList)
#nameList.append(input("Enter your name"))
print(nameList)
print(nameList.index("Web Bhumi"))
nameList1=nameList.copy()
nameList1.clear()
print(nameList)
print(nameList1)
nameList[0]="Mayank"
print(nameList)
nameList.insert(1,"Sir")
print(nameList)
nameList.pop(1)
print(nameList)
nameList.remove("Web Bhumi")
print(nameList)
#print(ele)
nameList2=(nameList.copy())
nameList2.sort()
#nameList.sort();
print(nameList)
print(nameList2)