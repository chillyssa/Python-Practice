import random 

# input
print("Let's play rock, paper, scissors!")
user_choice = input("What do you choose - rock, paper, or scissors?\n")
computer_choice = random.choice(["scissors", "rock", "paper"])
result = ""

# process
if computer_choice == user_choice: 
    result = "It's a tie game!"
elif user_choice == "rock" and computer_choice == "scissors":
    result = "YOU WIN!"
elif user_choice == "paper" and computer_choice == "rock":
    result = "YOU WIN!"
elif user_choice == "scissors" and computer_choice == "paper":
    result = "YOU WIN!"
else: 
    result = "YOU LOSE :("

# output
print("You chose: " + user_choice)
print("The computer chose: " + computer_choice)
print(result)