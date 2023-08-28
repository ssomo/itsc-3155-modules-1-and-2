#Teammates: Oliver, Jorge

#Three empty lists
list1 = []
list2 = []
list3 = []

#Asks the user to enter 5 numbers and store them to the list
for i in range(5):
    num = int(input('Enter a number for the first list: '))
    list1.append(num)

for i in range(5):
    num = int(input('Enter a number for the second list: '))
    list2.append(num)

#Checks if an element exists in list2 for each element in list1
# and stores the common element in list3
for i in list1:
    if i in list2:
        list3.append(i)

#print out all of the lists
print('First List:',list1)
print('Second List:',list2)
print('Common List:',list3)