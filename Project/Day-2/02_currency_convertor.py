def currency_convertor(rate, amount):
    return rate*amount

print('1. USD to INR')
print('2. INR to USD')

choise = int(input('Choise Convertion(1/2): '))
amount = float(input('Enter amount:'))

if choise == 1:
        rate = 88
        print(f'{amount} in USD is {currency_convertor(rate,amount)} IND')
elif choise == 2:
      rate = 1/88
      print(f'{amount} in IND {currency_convertor(rate,amount)} EUR')
