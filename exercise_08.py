#Original List
og_list = []
#Teammates: Oliver, Jorge

#New List
new_list = []

#Takes in 10 integers from the user and appends each integer to the og list
for i in range(1, 11):
    print('Enter number', i, ':')
    num = int(input())
    og_list.append(num)

#Checks if an element in og_list has a count of 1
for i in og_list:
    if og_list.count(i) == 1:
        #Appends elements that appear once to the new list
        new_list.append(i)

#Print the lists
print('Original List:',og_list)
print('Nums that appear once:',new_list)