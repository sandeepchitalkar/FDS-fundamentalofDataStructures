#header file declaration 
import array as arr

def TernarySearch(l, r, key, array):
    if (r >= l):
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        if (array[mid1] == key): 
            return mid1
        if (array[mid2] == key): 
            return mid2
        if (key < array[mid1]): 
            return ternarySearch(l,mid1 - 1, key,array)
        elif (key > array[mid2]): 
            return ternarySearch(mid2 + 1,r,key, array)
        else: 
            return ternarySearch(mid1+1,mid2 - 1,key,array)
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

result = TernarySearch(0,len(num)-1, key, num)
if result != -1:
    print(f"Target {key} found at index {key}")
else:
    print("Data not found in the list")
