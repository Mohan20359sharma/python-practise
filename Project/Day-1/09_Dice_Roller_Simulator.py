import random
def roll_dice():
    return random.randint(1,6)
while True:
    roll = input("Roll the dice? (Yes/No): ").lower()
    if roll == "yes":
        print(f"you rolled:{roll_dice()}")
    elif roll == "no":
        print("Good Bye!")
        break
    else:
        print("Please type 'yes' or 'no'.")