balance = 0

def check_balance():
    print(f"Your balance is: ${balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"${amount} deposited. New balance{balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Inflience Found!")
    else:
        balance -= amount
        print(f"${amount} Money Withdraw. New balance{balance}")

while True:
    print("1. check balance.")
    print("2. Deposit Money.")
    print("3. Withdraw Money.")
    print("4. Exit")
    choice = input("Choose your option.")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to Withdraw: "))
        withdraw(amount)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")