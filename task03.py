class User:
    
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        self.is_active = False
    
    def is_active(self,a) -> bool:
        self.is_active = bool(a)
        return self.is_active
    
    def get_info(self) -> str:
        return f"Username: {self.username},\nEmail: {self.email},\nActive: {self.is_active}"

def main() -> None:
    user = User("john_doe", "john@example.com")
    user.is_active(True)
    print(user.get_info())

if __name__ == "__main__":
    main()