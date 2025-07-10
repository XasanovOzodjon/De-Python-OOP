class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf o‘quvchisi.")

def main():
    student1 = Student("Malika", 20, "8B")
    student2 = Student("Ali", 22, "11A")
    student3 = Student("Ozodjon", 21, "5C")

if __name__ == "__main__":
    main()