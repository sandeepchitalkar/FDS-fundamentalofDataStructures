#Fibonacci Search Algorithm
import array as arr #header file declaration 
def fibonacci_search(lst, target):
    size = len(lst)
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
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
result = fibonacci_search(num, key)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
    
