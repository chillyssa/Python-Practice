import random

roll = random.randint(1,6)

user_guess = int(input("Guess the dice roll:\n"))
if user_guess == roll: 
    message = "Correct!"
else: 
    message = "Wrong :("
print(message, " The computer rolled a ", roll)