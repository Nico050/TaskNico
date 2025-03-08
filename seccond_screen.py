import os
from account import *
from first_screen import *

def menu(db, cuser):
    call_account = Conta()
    while True:
        print(f"Hello {cuser["Name"]}! Lets get started! what do you want to do?")
        print("For add a task type 'add_task'")
        print("For see your tasks type 'see_tasks'")
        print("For delete a task type 'delete_task'")
        print("For add a project type 'add_project'")
        print("For see your projects type 'see_projects'")
        print("For delete a project type 'delete_project'")
        print("For see your account type 'see_account'")
        print("For modify an account type 'modify_account'")
        print("For delete an account type 'delete_account'")
        print("For logout type 'logout'")
        print("For exit type 'exit'")
        choice = str(input().lower())

        if choice == "add_task":
            print("in working...")

        elif choice == "see_tasks":
            print("in working...")

        elif choice == "delete_task":
            print("in working...")

        elif choice == "add_project":
            print("in working...")

        elif choice == "see_projects":
            print("in working...")

        elif choice == "delete_project":
            print("in working...")

        elif choice == "see_account":
            print(cuser)
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == "modify_account":
            db, cuser = call_account.modify(db, cuser)

        elif choice == "delete_account":
            delete_choice = call_account.delete(db, cuser)
            if delete_choice == True:
                db, cuser = login_register_screen()
                menu(db, cuser)

        elif choice == "logout":
            logout_choice = call_account.logout()
            if logout_choice == True:
                db, cuser = login_register_screen()
                menu(db, cuser)

        elif choice == "exit":
            print("Exiting...")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')