''' Create an array by asking an input from user and display '''
#header file declaration 
import array as arr 

print("Program to show how to create an array")
num=arr.array('i',()) #creating an empty array
n=int(input("Enter how many element you want in array"))
#reading the data and stored in array
for i in range(0,n):
    num.append(int(input("Enter Data to be placed in array=")))

#display the data and stored in array
for i in range(0,n):
    print(f"Index[{i}] value is={num[i]}")
