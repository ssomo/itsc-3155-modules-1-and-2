#Teammates: Oliver, Jorge

#Prompts the user input
num = int(input('Enter an integer greater than 1: '))
#Checks if the integer is greater than 1
if(num <= 1):
    print('This integer is not greater than 1. Please try again')
    num = int(input('Enter an integer greater than 1: '))

for i in range(num + 1):
    cube = i ** 3 #cubes the index number
    #prints the result
    print('The cube of ', i, ' is ', cube)
