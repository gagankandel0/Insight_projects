list1=[]
 
num=int(input("Enter no. of elements in list:"))
for i in range(1,num+1):
    numbers=int(input("Enter the list numbers:"))
    list1.append(numbers)
    
print("the maximum element is: ",max(list1))
