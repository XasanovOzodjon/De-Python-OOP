class Book:
    books = []
    def __init__(self, title: str, author: str,) -> None:
        self.title = title
        self.author = author
        self.is_read = False
        Book.books.append(self)

    @classmethod
    def get_books(cls):
        return cls.books
    
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
    book5 = Book("kitob", "muallif")
    
    book1.mark_as_read()
    book4.mark_as_read()
    
    books = Book.get_books()
    for book in books:
        if book.is_read:
            print(f"{book.title}")

if __name__ == "__main__":
    main()  