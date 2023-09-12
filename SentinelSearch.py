#Sentinel Searching used to reduce comparision 
#header file declaration 
import array as arr
def sentinelSearch(lst, target):
    size = len(lst)
    lst.append(target)
    i = 0
    while(lst[i] != target):
        i += 1
    if(i == size):
        return -1
    else:
        return i

num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))

#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")

key=int(input("Enter element you want to search"))

result = sentinelSearch(num,key)
if result != -1:
    print(f"Target {key} found at index {result}")
else:
    print("Data not found in the list")
