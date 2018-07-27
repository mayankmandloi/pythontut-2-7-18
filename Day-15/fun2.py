def swap(inp1,inp2):
    print(inp1,inp2) #12 45
    temp=inp1
    inp1=inp2
    inp2=temp
    print(inp1,inp2) # 45 12


a=12
b=45
print(a,b)#12 45
swap(a,b)
print(a,b) #45 12