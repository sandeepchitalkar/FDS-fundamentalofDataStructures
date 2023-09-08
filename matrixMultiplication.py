rows = int(input("Enter total number of rows for matrix1:"))
cols = int(input("Enter total number of Column for matrix1:"))
rows1 = int(input("Enter total number of rows for matrix2:"))
cols1 = int(input("Enter total number of Column for matrix2:"))
'''check if number of columns in first matrix 
   is same as number of rows in second matrix.
    If not, then matrices can not be multiplied'''
if(cols!=rows1):
    print("Matrices can not be multiplied !!")
else:
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
    for i in range(0,rows1):
        for j in range(0,cols1):
            M2[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))
        
    #display a matrix
    print("Matrix1=")
    for i in range(0,rows):
        for j in range(0,cols):
            print(M1[i][j],end=" ")
        print()
    print("Matrix2=")
    for i in range(0,rows1):
        for j in range(0,cols1):
            print(M2[i][j],end=" ")
        print()                  
       
    #multiplication of 2 matrix 
    for i in range(0,rows):
        for j in range(0,cols1):
            for k in range(0,rows1):
                M3[i][j]+=M1[i][k]*M2[k][j]

    print("Multiplication of Matrix 1 and  Matrix2:")
    for i in range(0,rows):
        for j in range(0,cols1):
            print(M3[i][j],end="   ")
        print()
