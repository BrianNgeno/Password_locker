class User:
    '''
    class that generates new instance of user
    '''
    user_list = [] #empty user list
    def __init__(self,user_name,password):
        '''
        __init__method that helps us define properties for our objects.
        Args:
        user_name:New contact user_name.
        password:New contact password.
        '''
        self.user_name = user_name
        self.password = password