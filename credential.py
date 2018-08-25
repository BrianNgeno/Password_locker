class Credential:
    '''
    class that generates instance of an account
    '''
    credential_list = [] #Empty credential_list
    def __init__(self,account,validation):
        '''
        method that helps us define our object
        Args:
        account= new credential account.
        validation= new crederntial password.
        '''
        self.account = account
        self.validation = validation
    def save_credential(self):
        '''
        function that saves object details into credentials_list
        '''
        Credential.credential_list.append(self)
    
   

