count = int(input("Enter any number"));
first=0;
second=1;
current=0;
while count>=0:
    print(first,end=" ");
    current=second+first;
    first=second
    second=current
    count=count-1
