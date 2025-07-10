class Book:
    def __init__(self, title: str, author: str,) -> None:
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o‘qilgan deb belgilandi")

    def status(self):
        if self.is_read:
            print("O‘qilgan")
        else:
            print("O‘qilmagan")
            
def main():
    book1 = Book("O'tgan kunlar", "Abdulla Qodiriy")
    book2 = Book("Sariq devni minib", "O'tkir xoshimov")
    book3 = Book("Yulduzlar", "Hamid Olimjon")
    book4 = Book("Yoshlik", "Abdulla Qodiriy")
    
    
    book1.mark_as_read()
    book4.mark_as_read()
    
    book1.status()
    book2.status()
    book3.status()
    book4.status()

if __name__ == "__main__":
    main()  