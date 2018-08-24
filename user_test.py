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
    def test_unit(self):
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
if __name__ == '__main__':
    unittest.main()