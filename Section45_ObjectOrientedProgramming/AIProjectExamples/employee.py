class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

employee = Employee("John Doe", 50000)
print(f"{employee.get_name()} earns ${employee.get_salary()} per year.")
