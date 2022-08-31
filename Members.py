import getpass

class Members:

    count_members = []
    member_data = {}

    def __init__(self):
        print("Sign Up Section")
        Members.count_members.append(self)

        username = input('\t Enter your username:')

        if username in Members.member_data:
            print('your chosen username is already exit...')
            quit()
        else:
            self.username = username
            self.phone_number = input('\t Enter your phone number:')
            password = getpass.getpass(prompt='\t Enter your password>>>')

            if Members.is_valid_pw(password):
                self.__password = password
            else: 
                print('your password must be more than 4 digits...')
                Members.quit()

        self.user_id = Members.count_members.index(self)

        Members.member_data[self.username] = {"id": self.user_id, "phone number": self.phone_number, "password": self.__password}
        print('\n your subscription was successfull')
        Members.main_menu()
        
    @classmethod
    def main_menu(cls):
        """"Main Menu Section"""

        print("Main menu")
        while True:
            msg = "\t Enter Your Option (0: quit, 1: sign up, 2: sign in): "
            user_input = input(msg)

            if user_input == '0':
                cls.quit()

            elif user_input == '1':
                return cls()

            elif user_input == '2':
                print("\n login section")
                cls.login()

            else:
                print("invalid option!!! try again...")
                continue

    @classmethod
    def login(cls):
        """"login section"""

        username = input("\t Enter your username: ")
        password = getpass.getpass(prompt = "\t Etner your password>>> ")

        if cls.is_valid_user(username, password):
            print("You have successfullty logged in \n")
            cls.user_panel(username)

        else:
            print("The password or username entered is incorrect\n")

    @classmethod
    def user_panel(cls, un=None):
        """user panel section"""
        print("user panel")
        print("1: Get user info\n 2: Change password\n 3: Back to main menu\n")

        index = cls.member_data[un]['id']
        obj = cls.count_members[index]

        while True:

            user_input = input("\t<loggeed> Enter your option: ")

            if user_input == '1':
                print(cls.__str__(obj))

            elif user_input == "2":
                cls.change_password(obj)

            elif user_input == '3':
                print("logged out\n")
                cls.main_menu()

            else:
                print("Invalid option!!! try againl...")

    
    def change_password(self):
        """for changing password in user panel"""
        print ("\n change password\n")
        old_password = getpass.getpass(prompt="\t Enter your old password>>>")
        new_password = getpass.getpass(prompt="\t Enter your new password>>>")

        if old_password == self.__password:
            if self.is_valid_pw(new_password):

                self.__password = new_password
                Members.member_data[self.username]['password'] = new_password
                print("Your password was changerd successfully\n")

            else:
                print("New password is invalid, must be more than 4 digits\n")

        else:
            print("The old password is incorrect !!!")


    @staticmethod
    def is_valid_user(user: str, pw: str):
        """take two parameterm and check them for exist"""
        
        if user in Members.member_data and Members.member_data[user]["password"] == pw:
            return True
        else:
            return False

    @staticmethod
    def is_valid_pw(password: str):
        """take one parameter and check it for validation"""

        if len(password) < 4:
            return False
        else:
            return True

    def __str__(self):
        uid = self.user_id
        username = self.username
        phone_number = self.phone_number

        return f"\tuser ID : {uid}\n\tUsername : {username}\n\tPhone Number : {phone_number}\n"

    @classmethod
    def quit(cls):
        """Exit the program"""
        print(cls.member_data)          # to get log of program
        print("\nGoodbye")
        exit()


members = Members()
