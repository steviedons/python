'''
When you’re testing your own classes, the setUp() method can make
your test methods easier to write. You make one set of instances and attri-
butes in setUp() and then use these instances in all your test methods. This
is much easier than making a new set of instances and attributes in each
test method.
'''

import unittest
from survey import AnonymousSurvey

class Test_AnnymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """ Create a survey and a set of responses for all tests to use """        
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'French', 'spanish']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """Test 3 responses is stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
