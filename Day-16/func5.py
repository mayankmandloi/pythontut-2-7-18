def showMe():
    print("Hello I am Show me Function")

def showMeToo():
    showMe()
    print("I am show me too")

def funFunction():
    showMeToo()
    print("I am fun function")

funFunction()

print("Hello")