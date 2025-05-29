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
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
# concatenating strings is fun but let's use formatted strings for cleaner code
msg = f'{first} [{last}] is a coder'
# formatted string has curly brackets for placeholders for variables
print(msg)
######
######
######