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
# IF STATEMENTS
#is_hot = False
#is_cold = False
#if is_hot:
#    print("It's a hot day.")
#    print("Drink plenty of water!")
#else if
#elif is_cold:
#    print("It's a cold day.")
#    print("Wear warm clothes.")
#else:
#    print("It's a lovely day.")
#print("Enjoy your day.")
#### Credit exercise
price = 1000000
amount_good = price*.1
amount_else = price*.2
credit_good = False

if credit_good:
    print("Your down payment is " + f"${amount_good:,.0f}.")
else:
    print("Your down payment is " + f"${amount_else:,.0f}.")
####
####
####
#the other solution
has_good_credit = True
if has_good_credit:
    down_payment = 0.1* price
else:
    down_payment = 0.2* price
print(f"Down payment is ${down_payment}")
