def tip_calculator(total, percentage):
    return total * (percentage / 100)

total = float(input("Enter Total Bill: $"))
percenteage = float(input("Enter your percentage: "))
tip = tip_calculator(total,percenteage)

print(f"Tip:${tip:.2f}")
print(f"Total amount with tip: ${total + tip:.2f}")
