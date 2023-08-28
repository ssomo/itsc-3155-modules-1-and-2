#Teammates: Oliver, Jorge

#List to hold the strings
arr = []
#Empty string
string = ""
#Takes in 5 words from the user
for i in range(5):
    word = str(input('Enter a word: '))
    #Concentate the words into the string
    string += word + " "
    #Add the word to the list
    arr.append(word) 
#Print the words
print('Words:', arr)
#Print out the string
print('One String:',string)