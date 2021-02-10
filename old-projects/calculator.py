z=0
x=int(raw_input("\nType in your first number:"))
y=int(raw_input("\nType in your second number:"))
i=int(raw_input("\nWhat operation do you want to do? (enter 1=+, 2=-, 3=*, 4=/):"))
while z == 0:
    if i==1:
        a=x+y
        print (a)
        z=1
    if i==2:
        a=x-y
        print (a)
        z=1
    if i == 3:
        a=x*y
        print (a)
        z=1
    if i == 4:
        a=x/y
        print (a)
        z=1
    else:
        z=1
    
