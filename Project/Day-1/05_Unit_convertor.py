def km_to_miles(km):
    return km*0.621371
def calcuse_to_farhenite(celcuse):
    return (celcuse*(9/5))+32
km = float(input("Enter kilometer: "))
print(f"{km} kilometers is {km_to_miles(km)} miles")
calcuse = float(input("Enter tempraure in calcius: "))
print(f"{calcuse} calcius is {calcuse_to_farhenite(calcuse)} Fehrenneit.")