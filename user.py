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
    def find_by_user_name(cls,user_name):
        '''
        method that takes in a user_name and returns a user that matches that user_name.
        
        Args:
        user_name: user_name to search for
        Returns:
        User of that match the user_name
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user
