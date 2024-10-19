import random
def guess_number():
    round = int(input("How many round do you want to play? "))
    for i in range(1,round+1):
        print(f"\nRound {i}")
        number = random.randint(1,100)
        attempt = 0
        while True:
            guess = int(input("Guess the number between 1 to 100. "))
            attempt += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too High!")
            else:
                print(f"Congratulation You won this game in {attempt} attempt.")
                break
guess_number()