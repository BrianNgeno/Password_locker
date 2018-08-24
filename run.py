#!/usr/bin/env python3.6
from user import User
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

def copy_password(user)
    '''
    function that copies password
    '''
    user.copy_password()
