#Takes in a string from a user and stores it in the string variable
string = str(input('Enter a string: '))
#Empty String
backwards = ""
#Breaks the string up into a list of characters
string_list = list(string)
#Index number (Last character in the list)
idx = len(string_list) - 1

for i in range(len(string_list)):
    #Concatenate the value of the current index to the string
    backwards += string_list[idx]
    #Subtract the index by 1 
    idx -= 1
#Print the backwards string
print(backwards)


