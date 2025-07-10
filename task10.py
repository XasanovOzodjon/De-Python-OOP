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
            
def main():
    account = BankAccount("Ozodjon", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)

if __name__ == "__main__":
    main()  