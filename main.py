# Employees_System

from system_classes.front_end_manager import FrontendManager as FE
frontend = FE() 

if __name__ == "__main__":    
    while True:
        FE.print_dachbord()
        choice = input("Enter your choice (from 1 to 5): ")
        if not frontend.choice_valid(choice):
            print("Invalid range. Try again!")
            continue
        else:        
            frontend.show_menu(choice)
