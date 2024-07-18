#SPPU-DSA-practicals- Group A- Number-5 
# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string.

loop=True
print(" String Operation using pyton")

while loop:
    print("\n 1.To display word with the longest length ")
    print(" 2.To determines the frequency of occurrence of particular character in the string") 
    print(" 3.To check whether given string is palindrome or not") 
    print(" 4.To display index of first appearance of the substring") 
    print(" 5.To count the occurrences of each word in a given string.")
    print(" 6. Exit from the code")
    ch=int(input("Enter your choice to perform string operation"))
    if(ch==1):
        print("\n Display word with the longest length ")
        sentence = input("Enter sentence: ")
        longest = max(sentence.split(), key=len)
        print("\nLongest word is: ", longest)
        print("\nAnd its length is: ", len(longest))
        
    elif(ch==2):
        sentence = input("Enter sentence to check frequency of occurrence of particular character in the string: ")
        # using naive method to get count of each element in string
        all_freq = {}

        for i in sentence:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        # printing result
        print("\nCount of all characters in sentence is :\n "  + str(all_freq))
        
    elif(ch==3):
        text=input("Enter string To check whether given string is palindrome or not")
        print("\n Given text is "+text)
        rev=reversed(text)
        if list(text)==list(rev):
            print("String is a palindrome")
        else:
            print("String is not a palindrome")
            
            
    elif(ch==4):
        print(" Display index of first appearance of the substring")
        sentence = input("Enter sentence: ")
        sub_str1 =str(input("Enter substring to find in string:"))
        print("\n Index of first appearance of the substring "+sub_str1+" is")
        print(sentence.find(sub_str1))
        #check if Substring found or not.
        if(sentence.find(sub_str1)==-1):
            print("\n Substring Not Found")
        else:
            print("\n Substring found")
    elif(ch==5):
        print(" Count the occurrences of each word in a given string.")
        sentence = input("Enter sentence: ")
        # break the string into list of words
        sentence = sentence.split()
        str2 = []
        # loop till string values present in list str
        for i in sentence:
            # checking for the duplicacy
            if i not in str2:
                # insert value in str2
                str2.append(i)
        for i in range(0, len(str2)):
            # count the frequency of each word(present in str2) in sentence and print
            print('count of frequency', str2[i], 'is :', sentence.count(str2[i]))
        
    elif(ch==6):
        loop=False
        break
    else:
        print("\n Enter an wrong choice")
