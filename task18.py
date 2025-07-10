class Product:
    products = []
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        Product.products.append(self)

    @classmethod
    def get_products(cls):
        return cls.products

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
    product6 = Product("Monitor", 250, "Electronics", True)
    
    
    products = Product.get_products()
    
    mac_price = max(products, key=lambda x: x.price)

    print(f"Ombordagi eng qimmat mahsulot: {mac_price.get_info()}")
    
if __name__ == "__main__":
    main()