# (Celsius to Fahrenheit and vice versa)
def celsius_to_fehrenheit(celsius):
    return (celsius * 9/5) +32
def fehrenheit_to_celsius(fehrenheit):
    return (fehrenheit - 32) * 5/9

print('1. Celsius to Fehrenheit')
print('2. Fehrenheit to Celsius')

choice = int(input('Choose Option(1/2): '))

if choice == 1:
    celsius = float(input('Enter Temprature in Celsius. '))
    print(f'{celsius}°C is {celsius_to_fehrenheit(celsius)}°F')

elif choice == 2:
    fehrenheit = float(input('Enter Temprature in Fehrenheit: '))
    print(f'{fehrenheit}°F is {fehrenheit_to_celsius(fehrenheit)}°C')
