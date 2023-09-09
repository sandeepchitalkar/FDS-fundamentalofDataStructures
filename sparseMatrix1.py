#Implementation of Array Representation of Sparse Matrix 
import numpy as np
from scipy import sparse
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
arr = [[0 for j in range(cols)] for i in range(rows)] #initailze matrix to 0 
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

# You can convert a normal matrix to a compressed sparse row matrix using the 
#csr_matrix() method defined in Python’s scipy module.
sparse_matrix = sparse.csr_matrix(arr)
print("The sparse matrix is:")
print(sparse_matrix)

#The csc_matrix() method accepts a normal matrix as an input argument and returns a sparse matrix below.
sparse_matrix1 = sparse.csc_matrix(arr)
print("The sparse matrix is:")
print(sparse_matrix1)

#The coo_matrix() accepts a normal matrix as an input argument and returns a sparse matrix 
#in the coordinate format, as shown below.
sparse_matrix2 = sparse.coo_matrix(arr)
print("The sparse matrix is:")
print(sparse_matrix2)
