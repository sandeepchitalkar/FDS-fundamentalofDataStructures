import array as arr #header file declaration 

def quick_sort(array, start, end):
	if start < end:
		Pivot_index = partition(array, start, end)
		quick_sort(array, start, Pivot_index-1)
		quick_sort(array, Pivot_index+1, end)
		
def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high

    while i<=j:
        while i <= j and array[i] <= pivot:
            i = i + 1
        while i <= j and array[j] >= pivot:
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        if(i>j):
            array[low], array[j] = array[j], array[low]
    return j



# Function to print an array
def print_arr(arr, n):
	for i in range(n):
		print(arr[i], end=" ")
	print()

# Driver Code
print("Program to Perform Quick Sort")
num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))
print("Before Sorting")
print_arr(num, len(num))
quick_sort(num, 0, len(num)-1)
print("After Sorting")
print_arr(num, len(num))

