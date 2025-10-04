# Employees_System
class Employee:
    def __init__(self,name,age,salary):
        self.name = str(name)
        self.age = int(age)
        self.salary = float(salary)

    def get_employee_data(self):
        return (self.name,self.age,self.salary)    