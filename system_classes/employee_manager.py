# Employees_System
from system_classes.employees import Employee


class EmployeesManager:
    def __init__(self):
        self.data = []

    def add_new_employee(self,name,age,salary):
        emp = Employee(name,age,salary)
        self.data.append(emp.get_employee_data())

    def list_all_employees(self):
        if self.data: 
            for idx,employee in enumerate(self.data):
                print(f"Employee name: {employee[0]} has age: {employee[1]} and salary: {employee[2]}") 
        else:
            print("No employees at this moment")

    def delete_by_age(self,start_age , end_age):
        self.data = [employee for employee in self.data if not int(start_age) <= employee[1] <= int(end_age)]

    def update_salary_by_name(self,name):
        for idx,employee in enumerate(self.data):
            if name == employee[0]:
                salary_update = float(input("Enter the new salary: "))
                self.data[idx] = (employee[0],employee[1],salary_update)
                print(f"Salary of {employee[0]} updated to {salary_update}")
                break
        else:
            print("No employee with such a name")       
    def end_program(self):
        print("Thank you for using our system")
        exit(1) 


