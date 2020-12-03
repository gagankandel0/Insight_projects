input_str=input("enter a list of numbers seperated by space")
userList=input_str.split()
print("user list is: ",userList)
sum1=0
for n in userList:
    sum1+=int(n)
print("the sum is: ",sum1)
