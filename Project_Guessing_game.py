count_guess = 0
count_limit = 3

while count_guess < count_limit:
    guess = int(input("Guess: "))
    answer = 10
    if guess == answer:
        print("Correctly Guessed answer!")
        break
    elif count_guess == (count_limit - 1):
        print("You Failed!!!")
        break
    else:
        count_guess = count_guess + 1


#note you can also use else statement in while loop if the condition is stoped
#when break is called in while loop, else statement is ignored.      
message ="""
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(int("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Sorry, you failed")        
"""        
print(message)