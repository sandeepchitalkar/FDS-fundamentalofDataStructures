''' Create an array by asking an input from user and display 
search an element present in array or not using binary search recursive'''
import array as arr #header file declaration 
def binarySearch(array, x, low, high):
    if high >= low:
        mid = (low+high)//2
        # If found at mid, then return it
        if array[mid] == x:
            return mid
        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1

num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))
#Sort the original array as binary search work on sorted data
num=sorted(num)
#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")
#read key to be search in array
key=int(input("Enter element you want to search"))
result = binarySearch(num, key, 0, len(num)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
