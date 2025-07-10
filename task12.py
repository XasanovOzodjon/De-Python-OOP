class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Pul qo'shildi. Hisobingizda mavjud: {self.balance}$")
        else:
            print("Mablag musbat son bo'lmasin")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Xisobingizda yetarlicha mablag mavjud emas!!")
        else:
            self.balance -= amount
            print(f"Pul chiqarildi. Hisobingizda mavjud: {self.balance}$")
        
    def show_balance(self):
        print(f"{self.owner} hisobidagi mablag: {self.balance}$")
            
def main():
    account1 = BankAccount("Ozodjon", 1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(1500)
    account1.show_balance()
    
    account2 = BankAccount("Faridun", 2000)
    account2.deposit(300)
    account2.withdraw(1000)
    account2.show_balance()
    
    account3 = BankAccount("Dilshod", 1500)
    account3.deposit(700)
    account3.withdraw(500)
    account3.withdraw(2000)
    account3.show_balance()

if __name__ == "__main__":
    main()  