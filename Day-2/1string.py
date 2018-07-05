"""
String literals in python are surrounded by either single quotation marks,
or double quotation marks.
'hello' is the same as "hello".
Strings can be output to screen using the print function. For example: print("hello").
Like many other popular programming languages, strings in Python are arrays characters.
 However, Python does not have a character data type, a single character is simply a
 string with a length of 1. Square brackets can be
used to access elements of the string."""

text="Hello I am Mayank's \"mind\""
print(text)
print(text[1])

#Substring. Get the characters from position 2 to position 5:
b = "WebBhumi"
print(b[3:8])
print(b[1:])
print(b[:6])



#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a)
print(a.strip()) # returns "Hello, World!"

#The len() method returns the length of a string:
a = "ab ba "
print(len(a))

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#The upper() method returns the string in upper case
print(a.upper())


#The replace() method replaces a string with another string:
a = "Hello, Werld!"
print(a.replace("He", "Jf"))


#The split() method splits the string into substrings if it
# finds instances of the separator:
a = "Hello I am Mayank and I teach Python at Web Bhumi"
data=a.split(" ")
print(data[1]) # returns ['Hello', ' World!']
