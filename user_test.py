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


if __name__ == '__main__':
    unittest.main()