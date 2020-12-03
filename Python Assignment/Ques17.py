input_str=input("enter a list of numbers seperated by space")
userList=input_str.split()
print("user list is: ",userList)
mul=1
for n in userList:
    mul*=int(n)
print("the product is: ",mul)
