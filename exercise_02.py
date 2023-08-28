#Teammates: Oliver, Jorge

#Prompt user input
str = input('Enter a string: ')
str2 = input('Enter another string: ')

#Checks if a string is a suffix of the other string
if str2.endswith(str) | str.endswith(str2):
    #Prints true 
    print('true')
else:
    #Print false 
    print('false')
