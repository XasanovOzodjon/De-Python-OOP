class User:
    
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        self.is_active = False
    
    def activate(self):
        self.is_active = True
        print(f"Foydalanuvchi: {self.username} faollashtirildi.")
    
    def deactivate(self):
        self.is_active = False
        print(f"Foydalanuvchi: {self.username} bloklangandi")

    
def main() -> None:
    user = User("Faridun", "GG@Gamil.com")
    user.activate()
    user = User("Ozodjon", "Ozod@Gamil.com")
    user.deactivate()

if __name__ == "__main__":
    main()