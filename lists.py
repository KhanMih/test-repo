mylist=[] #python now knows it is a 1D list

mylist.append(5) #append is to add a thing to the end
print(mylist) #will print only 5
mylist.append(6)
print(mylist) #will print 5 AND 6
mylist[1]=7 #value 7 will overwrite the value in position 1 of mylist (which is 6)

num=int(input("Enter number to append to the list"))
mylist.append(num) #whatever user enters will be added to end of list
print("Unsorted List is ",mylist)

print(mylist[2]) #prints elemt in position 2

mylist.sort()
print("Sorted list is ",mylist)

looplist=[]
for i in range(10):
    looplist.append(int(input("Enter element to append to the list in a loop:")))
    
print("Unsorted list is",looplist)
looplist.sort()
print("Sorted list is ",looplist)

# for element in looplist:
#     element+=1
    
print(looplist)