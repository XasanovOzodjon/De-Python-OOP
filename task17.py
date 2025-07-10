class BankAccount:
    accounts = []
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.accounts.append(self)
        
    def show_balance(self):
        print(f"{self.owner} hisobidagi mablag: {self.balance}$")

    def get_balance(self):
        return self.balance

    @classmethod
    def get_accounts(cls):
        return cls.accounts

def main():
    account1 = BankAccount("Ozodjon", 1000) 
    account2 = BankAccount("Faridun", 2000)
    account3 = BankAccount("Dilshod", 1500)
    account4 = BankAccount("Malika", 2500)
    account5 = BankAccount("Diyor", 3000)
    
    accounts = BankAccount.get_accounts()

    summa = 0
    for account in accounts:
        summa += account.get_balance()
        
    print(f"Jami balance: {summa}$")

if __name__ == "__main__":
    main()