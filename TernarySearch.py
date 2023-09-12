#header file declaration 
import array as arr 
def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate midpoints
        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3

        # Check if the target is at mid1 or mid2
        if arr[mid1] == target:
            return mid1
            
        if arr[mid2] == target:
            return mid2

        # Adjust the search space
        if target < arr[mid1]:
            right = mid1 - 1
            
        elif target > arr[mid2]:
            left = mid2 + 1
            
        else:
            left = mid1 + 1
            right = mid2 - 1

    # Target not found in the list
    return -1


num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))

num=sorted(num)
#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")

key=int(input("Enter element you want to search"))

result = ternary_search(num, key)
if result != -1:
    print(f"Target {key} found at index {key}")
else:
    print("Data not found in the list")
