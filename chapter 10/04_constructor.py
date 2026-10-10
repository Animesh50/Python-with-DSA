class Employe:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):## dunder method which is automaticely called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"the language is = {self.language}\nThe salary is = {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Day")

harry = Employe("Harry", 13000, "JavaScript")
harry.name = "Harry"
print(harry.name,harry.language, harry.salary)  