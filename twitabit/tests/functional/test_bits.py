from twitabit.tests import *

class TestBitsController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='bits'))
        # Test response...
