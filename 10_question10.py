'''
10. Create a class Product with an attribute price. Implement a method apply_discount() that takes a percentage and reduces the price accordingly.
'''
class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name
    
    def apply_discount(self, discount_percente):
        discount = self.price * (discount_percente / 100)
        self.price -= discount
        return f"Price after {discount_percente}% discount:{self.price}"

product = Product("Laptop", 1000)
print(product.apply_discount(10))