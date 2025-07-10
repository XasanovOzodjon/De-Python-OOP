class Movie:
    def __init__(self, title, genre, director, rating):
        self.title = title
        self.genre = genre
        self.director = director
        self.rating = rating

    def get_info(self):
        return f"Title: {self.title},\nGenre: {self.genre},\nDirector: {self.director},\nRating: {self.rating}"

def main():
    movie1 = Movie("Farsaj", "Fantastika", "Axad qayum", 8.8)
    movie2 = Movie("It is life", "Horror", "Angeline white", 9.2)

    print(movie1.get_info())
    print(movie2.get_info())

if __name__ == "__main__":
    main()