#Question 1: Employee Salary Management
#Concepts: Classes, objects, inheritance, function overriding
#Scenario: A company has different types of employees. A regular employee
#receives a fixed salary, while a sales employee receives a fixed salary plus
#commission. Create a parent class Employee and a child class SalesEmployee
#that overrides the calculate_salary() method.
#Task: Calculate the total salary of a sales employee.
#Sample input:
#Employee Name: Rahul
#Basic Salary: 30000
#Commission: 5000
#Expected output:
#Employee: Rahul
#Total Salary: 35000



class Employee:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary
class SalesEmployee(Employee):
    def __init__(self,name,basic_salary,commission):
        super().__init__(name,basic_salary)
        self.commission = commission 

    def calculate_salary(self):
        return self.basic_salary + self.commission

emp = SalesEmployee("Rahul",30000,5000)

print("Employee:",emp.name)
print("Total Salary:",emp.calculate_salary())
        