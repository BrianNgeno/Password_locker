#!/usr/bin/env python3.6
import random
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

def save_credential(account,validation):
    account = Credential(account,validation)
    Credential.save_credential(account)

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

def display_credential():
    return Credential.display_credential()

def display_user():
    return User.display_user()

def validate_user(user_name,password):
    '''
    function that validates user
    '''
    user.validate_user(user_name,password)

def delete_credential(credential):
    '''
    function that saves new credentials
    '''
    Credential.delete_credential(credential)

def user_exist(user):
    '''
    function that checks if a user exists
    '''
    User.user_exist(user_name)

def copy_validation(account):
    '''
    function used to copy credential
    '''
    Credential.copy_validation(account)

def credential_exist(account):
    '''
    function that checks if credentials exist
    '''
    Credential.credential_exist
def find_by_user_name(user):
    '''
    '''
    return User.find_by_user_name(user)

def check_existing_user(password):
    return User.user_exist(password)

def main():
    print("\033[1;31;1m \n") 
    print("Hello user please input your name")
    user_name = input()
    print(f"\nWelcome -:{user_name}.Please use the short_codes provided")
    print('\n')

    while True:   
        print("\033[1;33;1m \n")   
        print("Use these short codes:\n cu- create new user. \n lg-login. \n ex-exit Locker.")
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

        elif short_code == "ex":
            print("Be sure to save more credentials later...")
            break

        # elif short_code == 'lg':
        #     print("Enter User_name")
        #     user_name = input()
        #     print("Enter password")
        #     print("-"*6)
        #     password = input()
        #     User.user_exist(user_name)
        #     print(f"\nUser :{user_name} Validated")
        elif short_code == 'lg':
            print("Enter the user you want to search for")
            search_password = input()
            if check_existing_user(search_password):
                search_user = find_by_user_name(search_password)
                print(f"{search_user.user_name} {search_user.password}")
                print('-' * 6)
                print("You are logged in succesfully")
                while True:
                    print("\n use these short codes to perform anything:\n cc- create new credential. \n dl- delete credentials. \n cp- copy credentials. \n vw- view credentials. \n ex- Exit credential_list")
                    user_choice = input("\n Enter your choice: ")
                    if user_choice == "cc":
                        print ("\n Enter Account")
                        account = input()
                        print("\n Your Password is..")
                        validation = ''
                        chars = "abcdefghijklmnopqrstuvwxyz1234567890!#.,?"
                        validation = ''.join(random.choice(chars)for _ in range(10))
                        print(validation, end='')
                        save_credential(account,validation)
                        
                        print(f"\n {account} Saved Succesfully")

                    if user_choice == "cp":
                        print("\n Enter credential you wish to copy")
                        account = input()
                        Credential.copy_validation(account)
                        print(f"\033[1;32;1m \n Credential-{account} copied succesfully")
                        # else:
                        #     print('\n')
                        #     print("You dont seem to have any credential saved yet")
                        #     print('\n')
                        

                    if user_choice == "dl":
                        print("\n Enter the credential you wish to delete")
                        acc_del = input()
                        delete_credential(acc_del)
                        print(f"\n Credential -{acc_del} -deleted succesfully")
                    
                    # if user_choice == "cd":
                    #     print("Enter user you wish to copy details")
                    #     user_name = input()
                    #     User.copy_password(user_name)

                    if user_choice == "ex":
                        print("\n Thanks For Checking In...")
                        break
                    

                    if user_choice == "vw":
                        print("\n Here is a list of all your credentials")
                        print('\n')
                        for credential in display_credential():
                            print(f"Account:{credential.account}Password:{credential.validation}")
                            print('\n')
                
                
                else:           
                    print("That user does not exist")
        
        else:
            print("\033[1;32;1m \n I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
