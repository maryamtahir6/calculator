x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
print("enter +,*,/-")
a=str( input("enter operator"))

if a=='+':
    print(x+y)
elif a=="-":
    print(x-y)
elif a=="*":
    print(x*y)
elif a=="/":
    print(x/y)
else:
    print ("not valid operator")
