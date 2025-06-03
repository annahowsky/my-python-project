### While loops to execute a block of code multiple times
# while condition is true, code block and repeatedly execute it
#i = 1
#while i <=5:
#    print('*' * i) #adding a string which will be run through the while loop
#    i = i + 1 #rewriting i iteratively
#print("Done") #prints done only after the while loop terminates
#####
#####
#####
# exercise
# use while loop to build a guessing game
winning_number = 9
attempts = 0
guess_limit = 3
while attempts < guess_limit:
    guess = int(input("Guess a number between 1-10: "))
    attempts += 1
    if guess == winning_number:
        print("Congratulations, you guessed it!")
        break #terminate the loop immediately
else:
    print("Sorry, try again next time.")