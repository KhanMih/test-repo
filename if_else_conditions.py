marks=int(input("Enter your marks"))

if (marks >= 50 and marks <=100):
    print("You passed")
    
    if(marks >=75):
        print("distinctions")
    else:
        print("Try harder")
    
elif (marks < 50 and marks >=0): #elif is else if
    print("You failed")
    print("This is something else")
    
else:
    print("Bad input")