import random
number = random.randint(0,100)
attempts = 0
while True:
    guess = int(input("Enter a number: "))
    attempts += 1
    if guess < number:
        print("Higher number.")
    elif guess > number:
        print("Lower number.")
    else:
        print(f"Congratulation! you guesses the numbers in {attempts} tries")
        break