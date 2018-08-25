import unittest
from credential import Credential
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

     def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential_list
        '''
        self.new_credential.save_credential()#saving the new credential
        self.assertEqual(len(Credentail.credentail_list),1)

if __name__ == "__main__":
    unittest.main() 