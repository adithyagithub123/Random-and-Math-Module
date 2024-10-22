import random
options = [ "Rock" , "Paper" , "Scissor" ]
user_input = input("choose rock , paper or scissor : ")
computer_choice = random.choice(options)

print("You choose ", user_input )
print("The computer chose " , computer_choice )

if user_input == computer_choice :
    print("It's a tie")
elif user_input == "rock" and computer_choice == "scissor" :
    print("You win !!")
elif user_input == "scissor" and computer_choice == "paper" :
    print("You win !!")
elif user_input == "paper" and computer_choice == "rock" :
    print("You win !!")
else :
    print("You lose ")
