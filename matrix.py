''' Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.'''
#Program to read matrix and display on screen
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
#initailze all value to 0 in matrix name arr
arr = [[0 for j in range(cols)] for i in range(rows)] 

#accepting a matrix from user
for i in range(0,rows):
    for j in range(0,cols):
        arr[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))

 #display a matrix
print("Entered Matrix:")
for row in arr:
    print(' '.join([str(elem) for elem in row]))
