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
    def get_info(self):
        return f"Ombordagi {self.name} narxi: {self.price}$"

def main():
    product1 = Product("Laptop", 1500, "Electronics", True)
    product2 = Product("Smartphone", 800, "Electronics", False)
    product3 = Product("Tablet", 300, "Electronics", True)
    product4 = Product("Smartwatch", 200, "Electronics", True)
    product5 = Product("Headphones", 100, "Electronics", True)
    
    
    a = list(filter(lambda x: x.in_stock, [product1, product2, product3, product4, product5]))

    print(f"Ombordagi jami mahsulotlar narxi: {sum(item.price for item in a)}$")

if __name__ == "__main__":
    main()