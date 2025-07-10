class Student:
    def __init__(self, name: str, age: int, class_: str):
        self.name = name
        self.age = age
        self.class_ = class_



def main():
    student1 = Student("Malika", 20, "8B")
    student2 = Student("Ali", 22, "11A")
    student3 = Student("Ozodjon", 21, "5C")

if __name__ == "__main__":
    main()