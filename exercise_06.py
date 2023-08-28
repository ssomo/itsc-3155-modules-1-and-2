#Teammates: Oliver, Jorge

#Prompts the user to enter a row num and stores it 
row = int(input('Enter a row num from 1 to 5: '))
#Prompts the user to 
col = int(input('Enter a col num from 1 to 5: '))

#Row for loop
for i in range(5):
    #Columns for loop
    for j in range(5):
        i_idx = i + 1 #i index
        j_idx = j + 1 #j index
        #Checks if the row and column numbers matches with the index
        if i_idx == row and j_idx == col :
            #Prints 1
            print('1', end=' ')
        else:
            #Prints 0
            print('0', end=' ')
    #Formats a new line for the grid
    print(' ')