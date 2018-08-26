import unittest 
from user import User
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating  test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Brian","ng123")
        #create user object
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case
        '''
        User.user_list=[]

    def test_init(self):
        '''
        test_initial test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Brian")
        self.assertEqual(self.new_user.password,"ng123")



    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        '''
        test_save_multiple user to check if we can save multiple user object to our user list
        '''
        self.new_user.save_user()
        test_user= User("user","qw123")#new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from the user_list
        '''
        self.new_user.save_user()
        test_user = User("user","qw123")#new user
        test_user.save_user()
        self.new_user.delete_user()#deleting a user
        self.assertEqual(len(User.user_list),1)
    
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user user_name and display information
        '''
        self.new_user.save_user()
        test_user = User("user","qw123")#new user
        test_user.save_user()
        found_user = User.find_by_username("user")
        self.assertEqual(found_user.password,test_user.password)
    
    def test_user_exists(self):
        '''
        test to check if we return a boolean if we cannot find the user
        '''
        self.new_user.save_user()
        test_user = User("user","qw123")#new user
        test_user.save_user()
        user_exists= User.user_exist("user")
        self.assertTrue(user_exists)
    def test_copy_password(self):
        '''
        test if user is able to copy passwords from the user details
        '''
        
        self.new_user.save_user()
        User.copy_password("Brian")
        self.assertEqual(self.new_user.password,pyperclip.paste())

    def test_validate_user(self):
        '''
        test if user is valid
        '''
        self.new_user.save_user()
        user = User.validate_user("brian","ng123")
        self.assertTrue(user)
        
if __name__ == '__main__':
    unittest.main()