import pyperclip
class User:
    '''
    class that generates new instance of user
    '''
    user_list = [] #empty user list
    def __init__(self,user_name,password):
        '''
        __init__method that helps us define properties for our objects.
        Args:
        user_name:New user user_name.
        password:New user password.
        '''
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
        '''
        save user method saves user object into user_list
        '''
        User.user_list.append(self)

    
    def delete_user(self):
        '''
        delete user method that deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes in a user_name and returns a user that matches that user_name.
        
        Args:
        user_name: user_name to search for
        Returns:
        User of that match the user_name
        '''
        for user in cls.user_list:
            if user.user_name == username:
                return user

    @classmethod
    def user_exist(cls,user_name):
        '''
        method that checks if the user exists
        Arg:
        user_name:passes the user_name to check if the user exists 
        returns:
        if a user matches the methods return a true but if the method fails returns false
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
            return False   

    @classmethod
    def copy_password(cls,user):
        user_found= User.find_by_user_name(user)

        pyperclip.copy(user_found.password)
        return cls.user_list    


    @classmethod
    def find_by_user_name(cls,user):
        for user in User.user_list:
            user.user_name = user
            return user
    @classmethod
    def validate_user(cls,user_name,password):
        '''
        method that validates a user 
        '''
        for user in User.user_list:
            if user:
                    return True
            else:
                return False
    @classmethod
    def display_user(cls):
        '''
        method that is used to display users
        '''
        return cls.user_list
