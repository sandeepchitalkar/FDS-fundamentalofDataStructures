''' In this section, we are going to look at and understand how matrix addition in Python works and what are the various methods of doing so.
Similar to any other type of addition, adding up the elements of one matrix to that of another is known as matrix addition. 
For eg., if elements of matrix A are added to the elements of matrix B, then matrix C would store the result of the addition i.e., C= A+B.
In Python, matrix addition can be performed only on matrices with the same shape, 
i.e., if A is a 2*3 matrix, then it can be added with the matrix B, which is also 2*3 but not with C that is a 3*3 matrix.
Another important note to keep in mind about matrix addition in Python is that in this particular language, the flow of addition is only one-way. 
It implies that the first element of matrix A[1,1] can only be added to the first element of matrix B[1,1]'''

rows = int(input("Enter total number of rows for matrix1:"))
cols = int(input("Enter total number of Column for matrix1:"))
rows1 = int(input("Enter total number of rows for matrix2:"))
cols1 = int(input("Enter total number of Column for matrix2:"))
if(rows==rows1 and cols==cols1):
    M1 = [[0 for j in range(cols)] for i in range(rows)] #initailze all value to 0
    M2 = [[0 for j in range(cols)] for i in range(rows)] #initailze all value to 0
    M3 = [[0 for j in range(cols)] for i in range(rows)] #initailze all value to 0
    #accepting a matrix from user
    print("Enter first Matrix1 :")
    for i in range(0,rows):
        for j in range(0,cols):
            M1[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))

    #accepting a matrix from user
    print("Enter Second Matrix1 :")
    for i in range(0,rows):
        for j in range(0,cols):
            M2[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))
        
    #display a matrix
    print("Entered Matrix1:")
    for row in M1:
        print(' '.join([str(elem) for elem in row]))
    
    print("Entered Matrix2:")
    for row in M2:
        print(' '.join([str(elem) for elem in row]))
    
    #addition of 2 matrix 
    print("Enter Second Matrix1 :")
    for i in range(0,rows):
        for j in range(0,cols):
            M3[i][j]=M1[i][j]+M2[i][j]

    print("Addition of Matrix 1 and  Matrix2:")
    for row in M3:
        print(' '.join([str(elem) for elem in row]))
else:
    print("matrix addition cannot perform")
