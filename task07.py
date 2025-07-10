class Movie:
    def __init__(self, title, genre, director, rating):
        self.title = title
        self.genre = genre
        self.director = director
        self.rating = rating

    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")

def main():
    movie1 = Movie("Farsaj", "Fantastika", "Axad qayum", 8.8)
    movie2 = Movie("It is life", "Horror", "IZhdiiib lorem", 9.2)

    movie1.show_summary()
    movie2.show_summary()

if __name__ == "__main__":
    main()