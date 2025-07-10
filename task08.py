class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")
        else:
            print(f"{self.name} hozirda tugagan ❌")

def main():
    product1 = Product("Laptop", 1500, "Electronics", True)
    product2 = Product("Smartphone", 800, "Electronics", False)

    product1.check_stock()
    product2.check_stock()

if __name__ == "__main__":
    main()