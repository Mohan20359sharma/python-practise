'''
You have a list of dictionaries where each dictionary represents a product with name, price, and quantity. Write a Python program to:

Find the product with the highest price.
Calculate the total value of all products (price × quantity).
'''
products = [
    {"name":"laptop",  "price":60000, "quentity":2},
    {"name":"Smartphone", "price":15000, "quentity":3},
    {"name":"Tablete", "price":20000, "quentity":0}
]
# most expensive product
most_expensive = max(products,key=lambda p: p["price"])
print("Most expensive product:", most_expensive["name"])

# claculate 
total_value = sum(p["price"] * p["quentity"] for p in products)
print("Total  value of all product:", total_value)