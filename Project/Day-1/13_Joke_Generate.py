import random

jokes ={
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get if you cross a snowman and a vampire? Frostbite!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
}
def tell_jokes():
    print(random.choice(jokes))

while True:
    request = input("Do you want to joke(Yes/No)?: ").lower()
    if request == 'yes':
      tell_jokes()
    elif request == 'no':
       print("GoodBye!")
       break
    else:
        print('Please Enter Yes/No. ')

