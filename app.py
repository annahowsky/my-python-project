#print('Anna Wehowsky') # print string in the ''
#print('o----')
#print(' ||||')
#print('*' * 10) # this is called an expression - it produces a value
#####
#####
#####
# variables
#price = 10 # integer
#print(price) # we are printing the value of the variable
#rating = 4.9 # float number
# name = 'Anna' # string
#is_published = False # boolean = True or False # also this is case-sensitive
# practice using variables
#patient_name = 'John Smith'
#age = 20
#new_patient = True
#name = input('What is your name? ') # naming a new variable using an expression
#color = input('What is your favorite color? ') # input expression asks for user input.
#print('Hi ' + name + '!') # concatenate
#print(name+ ' likes ' + color + '.')
#####
#####
#####
#birth_year = input('What is your birth year? ') # anything typed as a response to this is always treated as a string
#print(type(birth_year))
#age = 2025 - int(birth_year)
#print(type(age))
#print(age)
#weight_lbs = input("Enter your weight in lbs: ")
#weight_kg = int(weight_lbs) * 0.45359237
#print(weight_kg, 'kg ')
#####
#####
#####
# can use triple quotes for a long string ex. email thread
#course = 'Python for Beginners'
# indexing in square brackets
#print(course[0]) # indexing begins at 0, we are printing the first character in the string
#print(course[-1]) # indexing with negative will get the first character at the end
#print(course[0:3]) # indexing with characters in slot 012 (3 is excluded)
#another = course[:] # a new variable that copies our first string
###### test
#name = 'Jennifer'
#print(name[1:-1]) # see how it excludes the character at the end
######
######
######
#first = 'John'
#last = 'Smith'
#message = first + ' [' + last + '] is a coder'
#print(message)
# concatenating strings is fun but let's use formatted strings for cleaner code
#msg = f'{first} [{last}] is a coder'
# formatted string has curly brackets for placeholders for variables
#print(msg)
course = 'Python for Beginners'
print(len(course)) #printing the length of the characters in the string
# len is a gen purpose function for counting
#print(course.upper()) #this function is a method (upper method)
# creates a new string and prints it
#print(course) #the original is preserved
#print(course.lower()) #new method for lowercase
print(course.find('P')) #prints the result of the method for finding the index of P
#print(course.find('p'))# returns an error because there is no lowercase p - case-sensitive!
print(course.find('Beginners')) #returns 11 because the string begins with character B on index 11
# replace
print(course.replace('Beginners', 'Absolute Beginners')) # replace method is also case-sensitive but there is no error
print(course.replace('n','l')) # replace method will replace ALL characters with the new string. teehee Pythol for Begillers
#check to see if the string is in a variable - Boolean
print('Python' in course) #True
print('python' in course) #False
######
######
######
