from validator.tests import *

class TestDummyController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='dummy'))
        # Test response...
