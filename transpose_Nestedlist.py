'''Transpose operation using iterative method and 
transpose of a matrix in python using the 
Matrix transpose using Nested List Comprehension..'''
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
#initailze all value to 0 in matrix name arr
arr = [[0 for j in range(cols)] for i in range(rows)] 

#accepting a matrix from user
for i in range(0,rows):
    for j in range(0,cols):
        arr[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))

#printing original array
print("Matrix Entered:")
for i in range(0,rows):
    for j in range(0,cols):
        print(arr[i][j], end="  ")
    print()

#Matrix transpose using Nested List Comprehension.
result = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
for r in result:
   print(r)
