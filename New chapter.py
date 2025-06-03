# Logical Operators ###################################################################
# AND
# combines two conditions
#has_high_income = False
#has_good_credit = True
#has_criminal_record = True
#if has_high_income and has_good_credit:
#    print("Eligible for loan.")
#you see how both variables need to be true in the AND operator
#OR
#if has_good_credit or has_high_income:
#    print("Eligible for a different type of loan.")
#if has_good_credit and not has_criminal_record:
#    print("Eligible for a different type of loan.")
#else:
#    print("Not eligible for loan.")
# nice
#NOT
#####
#####
#####
# comparison operators ################################################################
#compare a variable with a value
#temperature = 70
#if temperature == 70: #need to use two equals signs as equality operator
    #!= is the not equal signs
#    print("It's a warm day")
#else:
#    print("It's not a warm day")

####
####
####
#exercise for name-filling on form
#name = input("What is your name?")
#if (len(name)) < 3:
#    print("Your name must be at least 3 characters long")
#elif (len(name)) > 50:
#    print("Your name must be less than 50 characters long")
#else:
#    print("nice name!")
#####
#####
#####
#exercise for weight conversion
weight = int(input("Enter your Weight: "))
l_or_k = input("Lbs or kg: ")
if l_or_k.lower() == "lbs":
    k_weight = (weight)*0.453592
    print(f"Your weight is {k_weight} kg.")
elif l_or_k.lower() == "kg":
    l_weight = (weight)/0.453592
    print(f"Your weight is {l_weight} lbs.")
# the responses are case sensitive..... so we use a method to lowercase all use input.
#####
#####