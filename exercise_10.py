#Teammates: Oliver, Jorge

#Takes in a string from the user
string = str(input('Enter a string: '))
#Breaks the string into a list of characters
str_list = list(string)
split_list = [] #Empty array
#Loop from 0 to the length of str_list
for i in range(0, len(str_list), 3):
    #Specify the range of i to i+3 index from str_list
    # and append those values to split_list
    split_list.append(str_list[i: i + 3])
#Prints out the list of the split characters
print(split_list)