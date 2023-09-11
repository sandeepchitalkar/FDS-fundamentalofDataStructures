''' Create an array by asking an input from user and display 
search an element present in array or not using linear search'''
#header file declaration 
import array as arr 

def LinearSearch(l1, element):
    for i in range(len(l1)):
        if l1[i] == element:
            return i   #return index value
    return -1  # if element is not found then it return -1
    
print("Program to show how to create an array")
num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))

#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")

key=int(input("Enter element you want to search"))
flag=LinearSearch(num,key)
if(flag==-1):
    print("element is not found")
else:
    print("element found at index",flag)
