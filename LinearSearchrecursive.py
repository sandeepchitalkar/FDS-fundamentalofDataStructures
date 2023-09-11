''' Create an array by asking an input from user and display 
search an element present in array or not using linear search Recursively'''
#header file declaration 
import array as arr 

def linear_search(arr, size, key):
    # If the array is empty we will return -1
    if (size == 0):
        return -1
    elif (arr[size - 1] == key):
        # Return the index of found key.
        return size - 1
    return linear_search(arr, size - 1, key)

print("Program to show how to create an array")
num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))
#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")
#read key to be search in array
key=int(input("Enter element you want to search"))

# Calling the Function
ans = linear_search(num, n, key)
if ans != -1:
    print("The element", key, "is found at",ans, "index of the given array.")
else:
    print("The element", key, "is not found.")
