# Employees_System

from system_classes.employee_manager import EmployeesManager
EmpMgr = EmployeesManager()

class FrontendManager:
    def __init__(self):
        pass
    def print_dachbord():
        msgs = ["Programe options:","1) Add a new employee","2) List all employees",
        "3) Delete by age range","4) Update salary given a name","5) End the program"]
        print('\n'.join(item for item in msgs)
        )

    def choice_valid(self,choice):
        return 48 < ord(choice[0]) <= 53  
          

    def show_menu(self,choice):    
        choice = int(choice)
        if choice == 1:
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            salary = input("Enter employee salary: ")
            EmpMgr.add_new_employee(name,age,salary)
        elif choice == 2:
            EmpMgr.list_all_employees()    
        elif choice == 3:
            start_age = int(input("from age: ")) 
            end_age = int(input("to age: "))    
            EmpMgr.delete_by_age(start_age,end_age)
        elif choice == 4:
            name = input("Enter employee name: ")  
            EmpMgr.update_salary_by_name(name)
        elif choice == 5:
            EmpMgr.end_program()