class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year



def main() -> None:
    car1 = Car("BMW", "M5", 2024)


if __name__ == "__main__":
    main()