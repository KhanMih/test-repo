x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. modulus")
c=0
z=int(input("enter your choice"))

if (z == 1):
    c=x+y
    d=x-y
    print("the addition is {} and subtraction is {}".format(c,d)) #.format() is for printing multiple variables
    
elif (z == 2):
    c=x-y
    print("the subtraction of {} - {} is {}".format(x,y,c))
    
elif (z == 3):
    c=x*y
    print("the multiplication is")
    print(c)

elif (z == 4):
    c=x/y
    print("the division is")
    print(c)
    
elif (z == 5):
    c=x%y
    print("the remainder is")
    print(c)
    
else:
    print("invalid choice")