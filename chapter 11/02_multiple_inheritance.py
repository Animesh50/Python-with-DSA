class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} amd the salary is {self.company}")

class coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all the languages here is your lnguages: { self.language}")


class programer(Employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good boy {self.language} language")


a = Employee()
b = programer()

b.show()
b.printLanguages()
b.showLanguage()
