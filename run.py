#!/usr/bin/env python3.6
from user import User
from credential import Credential
def create_user(user_name,password):
    '''
    function that creates a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    function to save new user
    '''
    user.save_user()


def delete_user(user):
    '''
    function that delete user
     '''
    user.delete_user()

def copy_password(user):
    '''
    function that copies password
    '''
    user.copy_password()

def validate_user(user_name,password):
    '''
    function that validates user
    '''
    user.validate_user(user_name,password)


def main():
    print("Hello user please input your name")
    user_name = input()
    print(f"Welcome{user_name}.Please Choose what what you wish to do?")
    print('\n')
    while True:      
        print("Use these short codes: cu- create new user,lg-login")
        short_code=input().lower()
        if short_code == 'cu':
            print("New User_name")
            u_name = input()

            print("New Password")
            print("-"*6)
            password = input()
            save_user(create_user(u_name,password))
            print('\n')
            print(f"New User{user_name}{password}created")
            print('\n')
            print(f"User{u_name}.You were succesfully Created")

        elif short_code == 'lg':
            print("Enter User_name")
            user_name = input()
            print("Enter password")
            print("-"*6)
            password = input()
            User.validate_user(user_name,password)
            while True:
                print("use these short codes to perform anything: cc- create new credential, dl- delete credentials, cp- copy credentials, vw- view credentials")
                user_choice = input("Enter your choice: ")
                if user_choice == "cc":
                    print ("here comes trouble")
                else:
                    print("hv")
        # if short_code == 'lg'
        else:
            print("bora uhaio")
if __name__ == '__main__':

    main()
