import pandas as pd
import os
import hashlib

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

    def find_DB_user(self):
        if os.path.exists("users.csv"):
            df = pd.read_csv("users.csv")
            return df
        else:
            df = pd.DataFrame(columns = ["Name", "Surname", "Username", "Email", "Password"])
            return df
        
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
            input("Press Enter to continue...")
            clear_terminal()
            return cuser

        else:
            print("Username or Password incorrect. Try again.")
            input("Press Enter to continue...")
            clear_terminal()
            return None