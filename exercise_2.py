#Takes in a string from the user
string = str(input('Enter a string: '))
#Breaks the string into a list of character
str_list = list(string)
#Empty String
lower = "" #for lower case letters
cap = "" #for upper case letters

for i in str_list:
    if i.islower():
        #Appends lower case letters together
        lower += i
    elif i.istitle():
        #Appends uppercase letters together
        cap += i
    
#Prints a combined string of lower and uppercase letters
print(lower + cap)