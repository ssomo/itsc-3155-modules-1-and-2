#list for all of the numbers
arr = []
#list for all of the even numbers
even = []

#Teammates: Oliver, Jorge

#While loop
while True:
    str = (input('Enter a number or QUIT to quit: '))
    #Stops the while loop if the user entered QUIT
    if str == 'QUIT':
        break
    #Converts the user input to an int
    number = int(str)
    #Appends the number to the list
    arr.append(number)
    #Checks if the number is even
    if number % 2 == 0:
        #Appends the number to the even list
        even.append(number)

#Prints out the lists
print('All Nums:', arr)
print('Even Nums:', even)
