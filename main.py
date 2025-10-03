# Employees_System
def print_dachbord():
    msgs = ["Programe options:","1) Add a new employee","2) List all employees",
    "3) Delete by age range","4) Update salary given a name","5) End the program"]
    print('\n'.join(item for item in msgs)
    )
def choice_valid(choice):
    return 0 < choice <= 5
def add_new_employee():
    pass
def list_all_employees():
    pass
def delete_by_age():
    pass    
def update_salary_by_name():
    pass 
def end_program():
    pass       

if __name__ == "main":    
    while True:
        print_dachbord()
        choice = int(input("Enter your choice (from 1 to 5): "))
        if not choice_valid(choice):
            print("Invalid range. Try again!")
            continue
        else:
            if choice == 1:
                add_new_employee()
            elif choice == 2:
                list_all_employees()    
            elif choice == 3:
                delete_by_age()
            elif choice == 4:
                update_salary_by_name()
            elif choice == 5:
                end_program()
