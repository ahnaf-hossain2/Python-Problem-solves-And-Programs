# Create a Class "Programmer" for storing information of new programmers
# working at Microsoft.
class Programmer:
    company = "Microsoft"
    name = ""
    age = ""
    language = ""
    salary = ""
    def __init__(self, company, name, age, language, salary):
        self.company = company
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary

    def display(self):
        print("Company: ", self.company)
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Language: ", self.language)
        print("Salary: ", self.salary)
person1 = Programmer("Microsoft", "Ahnaf", 20, "Python", 60000)
person1.display()
