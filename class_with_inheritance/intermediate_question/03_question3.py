'''
3. Create a class Book with attributes title, author, and price. Implement a class method set_discount() that applies a discount to all book prices.
'''

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_price(self):
        return self.price - (self.price * (Book.discount / 100))

    @classmethod
    def set_discount(cls, discount):
        cls.discount = discount

book1  = Book("1984", "George Orwell", 20)
book2 = Book("Chals Vabes", "Novel", 15)

Book.set_discount(10)
print(book1.get_price())
print(book2.get_price())