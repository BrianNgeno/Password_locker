import pyperclip
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
    @classmethod
    def delete_credential(cls,account):
        '''
        delete credential method deletes a saved contact from the credential_list
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                Credential.credential_list.remove(credential)
    

    @classmethod
    def find_by_account(cls,account):
        '''
        takes in account and returns a credential that matches
        arg:account 
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    @classmethod
    def copy_validation(cls,validation):
        credential_found = Credential.find_by_account(validation)

        pyperclip.copy(credential_found.validation) 
        return cls.credential_list

        
    @classmethod
    def credential_exist(cls,validation):
        '''
        method that checks if the credential exists
        Arg:
        account:passes the account to check if the account exists 
        returns:
        if a credential matches the methods return a true but if the method fails returns false
        '''
        for credential in cls.credential_list:
            if credential.validation == validation:
                return True
        return False 
   
    @classmethod
    def display_credential(cls):
        '''
        method that is used to display credentials
        '''
        return cls.credential_list

