#Teammates: Oliver, Jorge

#Prompt user to enter a value from 0-100
value = int(input('Enter a grade from 0-100: '))
#Calculate the user's grade
grade = ''
if value >= 90:
    grade = 'A'
elif value >= 80:
    grade = 'B'
elif value >= 70:
    grade = 'C'
elif value >= 60:
    grade = 'D'
else:
    grade = 'F'
#Print the grade
print('Your grade is ' + grade)
