import random
number = random.randint(0,10)
playing = 0

while playing < 5:
    guess = int(input("Guess a number between 0 to 10 : "))
    if number == guess :
        print("You win the game the guessed number was " , number)
        break
    else :
        print("You lose , please try again")