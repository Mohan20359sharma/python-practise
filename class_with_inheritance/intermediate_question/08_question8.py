'''
8. Create a class Order with a static method validate_quantity() that checks if a given quantity is valid (greater than 0). Use it to validate the quantity before placing an order.
'''
class Order:
    @staticmethod
    def validate_quantity(quantity):
        return quantity > 0
    def __init__(self, product, quantity):
        if Order.validate_quantity(quantity):
            self.product = product
            self.quantity = quantity
        else:
            raise ValueError("Invalid Quantity")
        
order = Order("Laptop", 2)
print(f"Ordered {order.quantity} {order.product}(s) ")