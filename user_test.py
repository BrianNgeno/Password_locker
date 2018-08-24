import unittest 
from user import User

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

    def test_init(self):
        '''
        test_initial test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Brian")
        self.assertEqual(self.new_user.password,"ng123")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case
        '''
        User.user_list=[]

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
    
    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user user_name and display information
        '''
        self.new_user.save_user()
        test_user = User("user","qw123")#new user
        test_user.save_user()
        found_user = User.find_by_user_name("user")
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

if __name__ == '__main__':
    unittest.main()