#Teammates: Oliver, Jorge

#Prompt the user to enter a number 
# and stores the number in a variable
n = int(input('Enter a number: '))
#Empty list
my_list = []
#Each iteration of the for loop asks the user to enter a value 
# and stores the value in a list
for i in range(n):
    idx = i + 1
    print('Enter number',idx, ':')
    num = float(input())
    my_list.append(num)
#Displays the contents of the list
print('List:',my_list)
#Calculates the average of the list values
avg = sum(my_list) / len(my_list)
#Prints the averages
print('Average:', avg)