
import os
class User:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None

    def entering(self):
        self.clear_console()
        print("""
        Tizimga hush kelibsiz:
        
        1. SignIn
        2. SignUp
        """)

        enter = input("Tanlash [1/2]: ").strip()
        while enter not in ['1', '2'] or enter == "":
            self.clear_console()
            enter = input("Tanlash [1/2]: ").strip()

        if enter == '1':
            self.signin()
        else:
            self.signup()

    def signin(self):
        self.clear_console()
        print("Bu login qismi")

        self.input_old_email = input("Emailingizni kiriting: ").strip()
        while self.input_old_email == "":
            self.clear_console()
            print("Invalid email please repeat")
            self.input_old_email = input("Emailingizni kiriting: ").strip()

        self.input_old_password = input("Passwordingizni kiriting: ").strip()
        while self.input_old_password == "":
            self.clear_console()
            print("Invalid password please repeat")
            self.input_old_password = input("Passwordingizni kiriting: ").strip()



    def signup(self):
        self.clear_console()
        print("Bu registration qismi")

        self.input_username = input("Username ni kiriting: ").strip()
        while self.input_username == "":
            self.clear_console()
            print("Invalid user name ")
            self.input_username = input("User name ni qayta kiriting: ").strip()

        self.input_email = input("Emailingizni kiriting: ").strip()
        while self.input_email == "":
            self.clear_console()
            print("Invalid email")
            self.input_email = input("Emailingizni kiriting: ").strip()

        self.input_password = input("Passwordingizni kiriting: ").strip()
        while self.input_password == "":
            self.clear_console()
            print("Invalid password please repeat input")
            self.input_password = input("Passwordingizni kiriting: ").strip()



    def clear_console(self):
        os.system("cls")


user = User()

user.entering()