class Employe:
    language = "Python"
    salary = 1200000

    def getinfo(self):
        print(f"the language is = {self.language}\nThe salary is = {self.salary}")

    def greet(self):
        print("Good Day")

harry = Employe()
harry.language = "javascript"
harry.getinfo()
harry.greet()