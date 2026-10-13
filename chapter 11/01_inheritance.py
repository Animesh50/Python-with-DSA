class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} amd the salary is {self.salary}")

#class programer:
#    company = "ITC Infotech"
#    def show(self):
#        print(f"The name is {self.name} amd the salary is {self.salary}")

#    def showLanguage(self):
#        print(f"The name is {self.name} and he is good boy {self.language} language")

class programer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good boy {self.language} language")


a = Employee()
b = programer()

print(a.company, b.company)