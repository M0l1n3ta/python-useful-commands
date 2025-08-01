class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name}, ${self.price}"
        
    def __repr__(self):
        return f"{self.name} ({self.product_id})"

products = [
    Product(1, "Headphones", 49.99),
    Product(2, "Monitor speaker", 150.0),
    Product(3, "Soundcard", 78.5),
]

for p in products:
    print(p)