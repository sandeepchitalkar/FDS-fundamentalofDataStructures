#Program to read matrix and display on screen
rows = int(input("Enter total number of rows:"))
cols = int(input("Enter total number of Column:"))
M1 = [[0 for j in range(cols)] for i in range(rows)] #initailze all value to 0
M2 = [[0 for j in range(cols)] for i in range(rows)] #initailze all value to 0
#accepting a matrix from user
for i in range(0,rows):
    for j in range(0,cols):
        arr[i][j]=int(input(f"Enter the value for index[{i}][{j}]="))

 #display a matrix
print("Entered Matrix:")
for row in arr:
    print(' '.join([str(elem) for elem in row]))
