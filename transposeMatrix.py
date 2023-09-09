'''Transpose operation using iterative method and 
transpose of a matrix in python using the map() function and zip() function.'''
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
#initailze all value to 0 in matrix name arr
arr = [[0 for j in range(cols)] for i in range(rows)] 

# initializing another matrix to store the result or transpose matrix.
# exchange is done if matrix is 2*3 then result matrix must be 3*2
rows1=cols
cols1=rows
transpose = [[0 for j in range(cols1)] for i in range(rows1)] 

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

#transpose of original array
print("Matrix Entered:")
for i in range(0,cols1):
    for j in range(0,rows1):
        transpose[j][i]=arr[i][j]
        
# print the transpose of original array
print("Transpose of matrix:")
for i in range(0,rows1):
    for j in range(0,cols1):
        print(transpose[i][j], end="  ")
    print()
 
