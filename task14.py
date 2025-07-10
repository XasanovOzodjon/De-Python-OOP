class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} yoshda.")

def main():
    student1 = Student("Malika", 20)
    student2 = Student("Ali", 25)
    student3 = Student("Ozodjon", 21)
    student4 = Student("Faridun", 22)
    student5 = Student("Diyor", 23)

    max([student1, student2, student3, student4, student5], key= lambda i:i.age).show_info()

if __name__ == "__main__":
    main()