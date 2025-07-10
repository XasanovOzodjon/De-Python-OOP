class Book:
    def __init__(self, title: str, author: str, is_read: bool = False,) -> None:
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o‘qilgan deb belgilandi")

    def status(self):
        if self.is_read:
            print("O‘qilgan")
        else:
            print("O‘qilmagan")
            
def main():
    book1 = Book("O'tgan kunlar", "Abdulla Qodiriy", False)
    book2 = Book("Sariq devni minib", "O'tkir xoshimov", True)

    book1.mark_as_read()
    book1.status()
    book2.status()

if __name__ == "__main__":
    main()  