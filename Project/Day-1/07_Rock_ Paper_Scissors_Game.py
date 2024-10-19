import random

choices = ['rock', 'paper', 'scissors']

def play_game():
    computer_choice = random.choice(choices)
    user_choise = input("Enter rock paper or scissors: ")

    if user_choise == computer_choice:
        return "It's a tie!"
    elif (user_choise == 'paper' and computer_choice == 'rock') or (user_choise == 'rock' and computer_choice == 'scissors') or (user_choise == 'scissors' and computer_choice == 'paper'):
        print("You Win!")
    else:
         return 'You Lose!'

print(play_game())