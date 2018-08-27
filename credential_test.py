import unittest
from credential import Credential
import pyperclip

class TestCredential(unittest.TestCase):
    '''
    Test that defines test cases for the credentials class behaviour.
    
    Args:
        unittest.TestCase:TestCase class that help in creating relating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credential("facebook","123qwe")#create credential object
    def test_init(self):
        '''
        test if the object is imitialized properly
        '''
        self.assertEqual(self.new_credential.account,"facebook")
        self.assertEqual(self.new_credential.validation,"123qwe")
    def tearDown(self):
        '''
        used to clear the list after every run
        '''
        Credential.credential_list=[]

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential_list
        '''
        self.new_credential.save_credential()#saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        test case to test if mulitple_credential objects can be saved into the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("facebook","123qwe")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
    
    def test_delete_credential(self):
        '''
        test delete is to check if a user can delete a credential
        '''
        self.new_credential.save_credential()
        test_credential= Credential("facebook","123qwe")#new credential
        test_credential.save_credential()
        self.new_credential.delete_credential()#delete credential
        self.assertEqual(len(Credential.credential_list),1)
        
   
    def test_find_credential_by_account(self):
        '''
        test to check for credential by the account and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("facebook","123qwe")#new credential
        test_credential.save_credential()
        found_credential = Credential.find_by_account("facebook")
        self.assertEqual(found_credential.validation,test_credential.validation)

    def test_copy_validation(self):
        '''
        test if user is able to copy validation from the credential details
        '''
        self.new_credential.save_credential()
        Credential.copy_validation("facebook")
        self.assertEqual(self.new_credential.validation,pyperclip.paste())

    def test_credential_exist(self):
        '''
        test to check if we return a boolean if we cannot find the user
        '''
        self.new_credential.save_credential()
        test_credential = Credential("facebook","123qw")#new credential
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("credential")
        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        self.assertEqual(Credential.display_credential(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()



