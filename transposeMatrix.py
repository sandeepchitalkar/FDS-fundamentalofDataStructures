'''Transpose operation using iterative method and 
transpose of a matrix in python using the map() function and zip() function.'''
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
#initailze all value to 0 in matrix name arr
arr = [[0 for j in range(cols)] for i in range(rows)] 
# initializing another (2 x 3) matrix to store the result.
transpose = [[0 for j in range(cols)] for i in range(rows)] 

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

# iterating the rows and then columns of each row
for i in range(0,rows):
    for j in range(0,cols):
        transpose[j][i] = arr[i][j]
        
'''#transpose of a matrix in python using the map() function and zip() function.
transpose = map(list, zip(*arr))'''
#printing transposed array
print("Transposed of Matrix:")
for i in range(0,rows):
    for j in range(0,cols):
        print(transpose[i][j], end="  ")
    print()
