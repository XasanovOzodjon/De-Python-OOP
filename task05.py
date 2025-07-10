class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def get_info(self):
        return f"Product(\nname={self.name},\nprice={self.price}\n)"
    
def main():
    product1 = Product("Laptop", 1500, "Electronics", True)
    product2 = Product("Smartphone", 800, "Electronics", True)
    
    print(product1.get_info())
    print(product2.get_info())
    
if __name__ == "__main__":
    main()