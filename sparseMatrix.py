#Implementation of Array Representation of Sparse Matrix 
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

#Finding total non-zero values in the sparse matrix
size = 0
for i in range(0,rows):
    for j in range(0, cols):
        if(arr[i][j]!=0):
                size+=1;
#Defining result Matrix
triplet = [[0 for j in range(size)] for i in range(3)]   

#Generating result matrix
k = 0
for i in range(0,rows):
    for j in range(0, cols):
        if (arr[i][j] != 0):
            triplet[0][k] = i;
            triplet[1][k] = j;
            triplet[2][k] = arr[i][j];
            k+=1;
            
#Displaying result matrix
print("Triplet Representation : ")
for i in range(0,3):
    for j in range(0,size):
        print(triplet[i][j], end="  ")
    print()
