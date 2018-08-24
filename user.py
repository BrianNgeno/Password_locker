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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case
        '''
        User.user_list=[]
    
    

