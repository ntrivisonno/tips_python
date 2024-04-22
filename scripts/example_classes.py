# example of Class, Inheritance, Encapsulation, Polymorphism, Abstraction, Method Overloading in python


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Inheritance
class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.department}"

# Encapsulation
class Payroll:
    def __init__(self):
        self.salary = 0

    def set_salary(self, ammount):
        self.salary = ammount
    def get_salary(self):
        return self.salary

# Polymorphism
class HRSystem:
    def calculate_salary(self, employee):
        if isinstance(employee, Manager):
            # Calculate salary for manager
            return 50000 + (employee.age * 1000)
        elif isinstance(employee, Intern):
            # Calculate salary for intern
            return 20000 + (employee.age * 500)
        elif isinstance(employee, Employee):
            return 30000 + (employee.age * 800)
        else:
            # Handle unknown employee types
            raise ValueError("Unknown employee type")

# Abstraction
class EmployeeDatabase:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)
    def get_employees(self):
        return self.__employees

# Method Overriding
class Intern(Employee):
        def __init__(self, name, age, school):
            super().__init__(name, age)
            self.school = school
        def display_info(self):
            return f"Name: {self.name}, Age: {self.age}, School: {self.school}"

# Method OverLoading (Not natively supported in Python)
class HRAnalytics:
    def analyze_employee(self, employee=None):
        if employee is None:
            # Do analysis for all employees
            pass
        else:
            # Do analysis for specific employee
            pass

# Composition
class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

# Example usage
# Creating objects
employee1 = Employee("John Doe", 30)
manager1 = Manager("Jane Smith", 35, "HR")
intern1 = Intern("Alice", 20, "XYZ University")
department1 = Department("HR Department", manager1)

# Encapsulation Example
payroll = Payroll()
payroll.set_salary(50000)
print(manager1.display_info())
print("Salary:", payroll.get_salary())
# Method overriding example
print("# Method overriding example")
print(intern1.display_info())
# composition example
print("# composition example")
print(department1.manager.name) # accesing manager's name throught department


# ver mejor eso de método overloading, xq si bien así como está funciona: no es muy correcto que digamos. Funciona por la flexibilidad de python. ver con chatGTP
