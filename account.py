import pandas as pd
import os
import hashlib
from notify import *

def find_DB_user():
    if os.path.exists("users.csv"):
        df = pd.read_csv("users.csv")
        return df
    else:
        df = pd.DataFrame(columns = ["Name", "Surname", "Username", "Email", "Password"])
        return df

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Conta:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.username = ""
        self.email = ""
        self.password = ""
        
    def register(self, db):
        print("Register your account now!")
        self.name = str(input("Type your Name: "))
        self.surname = str(input("Type your Surname: "))
        self.username = str(input("Type your Username (without spaces): ")).lower()
        self.email = str(input("Type your Email: "))
        self.password = hash_password(str(input("Type your Password: ")))

        if self.username in db["Username"].values or self.email in db["Email"].values:
            print("Username or Email already exists. Try another one.")
            input("Press Enter to continue...")
            clear_terminal()
            return db, None

        if " " in self.username:
            print("Username must not contain spaces. Try another one.")
            input("Press Enter to continue...")
            clear_terminal()
            return db, None

        if "@" not in self.email:
            print("Invalid email. Try another one.")
            input("Press Enter to continue...")
            clear_terminal()
            return db, None

        cuser = {}
        cuser["Name"] = self.name
        cuser["Surname"] = self.surname
        cuser["Username"] = self.username
        cuser["Email"] = self.email

        tempDB = pd.DataFrame({"Name": [self.name], "Surname": [self.surname], "Username": [self.username], "Email": [self.email], "Password": [self.password]})
        db = pd.concat([db, tempDB], ignore_index = True)
        db.to_csv("users.csv", index = False)

        print("Account created successfully!")
        registration_email(self.email, self.name, self.surname)
        input("Press Enter to continue...")
        clear_terminal()

        return db, cuser
    
    def login(self, db):
        print("Login to your account now!")
        u = str(input("Type your Username: ")).lower()
        p = str(input("Type your Password: "))

        pointeru = db[db["Username"]==u]

        if not pointeru.empty and pointeru.iloc[0]["Password"] == hash_password(p):
            print("Login successful!")
            cuser = {}
            cuser["Name"] = pointeru["Name"].values[0]
            cuser["Surname"] = pointeru["Surname"].values[0]
            cuser["Username"] = pointeru["Username"].values[0]
            cuser["Email"] = pointeru["Email"].values[0]
            login_email(cuser["Email"], cuser["Name"], cuser["Surname"])
            input("Press Enter to continue...")
            clear_terminal()
            return cuser

        else:
            print("Username or Password incorrect. Try again.")
            input("Press Enter to continue...")
            clear_terminal()
            return None
        
    def modify(self, db, cuser):
        print("Modify your account now!")
        while True:
            print("What do you want to modify?")
            choice = str(input().lower())
            choose = False

            if choice == "name":
                new_name = str(input("Type your new Name: "))
                db.loc[db["Name"] == cuser["Name"], "Name"] = new_name
                cuser["Name"] = new_name
                db.to_csv("users.csv", index = False)
                db = pd.read_csv("users.csv")
                choose = True
                print("Name modified sucessfully!")
            
            elif choice == "surname":
                new_surname = str(input("Type your new Surname: "))
                db.loc[db["Surname"] == cuser["Surname"], "Surname"] = new_surname
                cuser["Surname"] = new_surname
                db.to_csv("users.csv", index = False)
                db = pd.read_csv("users.csv")
                choose = True
                print("Surname modified sucessfully!")

            elif choice == "email":
                while True:
                    new_email = str(input("Type your new Email: "))
                    if new_email in db["Email"].values and "@" not in new_email:
                        print("Email already exists. Try another one.")

                    else:
                        db.loc[db["Email"] == cuser["Email"], "Email"] = new_email
                        cuser["Email"] = new_email
                        db.to_csv("users.csv", index = False)
                        db = pd.read_csv("users.csv")
                        choose = True
                        print("Email modified sucessfully!")
                        break

            else:
                print("Invalid choice. Try again.")
                choose = False
            
            if choose == True:
                print("Do you want to modify another field? (yes/no)")
                answer = str(input().lower())
                if answer == "no":
                    print("Account modified successfully!")
                    input("Press Enter to continue...")
                    clear_terminal()
                    break
        return db, cuser

    def logout(self):
        print("Do you want to logout? (yes/no)")
        choice = str(input().lower())
        if choice == "yes":
            print("Logging out...")
            input("Press Enter to continue...")
            clear_terminal()
            return True
        else:
            input("Press Enter to continue...")
            clear_terminal()
            return False
        
    def delete(self, db, cuser):
        print("To delete your account type your password.")
        p = str(input("Type your Password: "))
        pointeru = db[db["Username"]==cuser["Username"]]
        if pointeru.iloc[0]["Password"] == hash_password(p):
            db = db[db["Username"] != cuser["Username"]]
            db.to_csv("users.csv", index = False)
            print("Account deleted successfully!")
            input("Press Enter to continue...")
            clear_terminal()
            return True
        else:
            print("Password incorrect. Try again.")
            input("Press Enter to continue...")
            clear_terminal()