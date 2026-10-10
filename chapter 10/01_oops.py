class Employee:
    language = "py"  ## This is the class attribute 
    salary = 1200000

harry = Employee()
harry.name = "Animesh"  ## Thsi is an instance attribute
print(harry.name,harry.language,harry.salary)

rohan = Employee()
rohan.name = "Rohan bhai sahab"
print(rohan.name,rohan.salary, rohan.language)

## Here name is object and salary and language are class attribute as they directly belongs to the class